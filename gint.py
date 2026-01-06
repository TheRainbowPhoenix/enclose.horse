import time
import pygame
from pygame.locals import *
import sys
import struct
from typing import List, Optional, Tuple


# Display dimensions
DWIDTH = 320
DHEIGHT = 528

C_WHITE = 0xFFFF
C_LIGHT = 0xad55
C_DARK  = 0x528a
C_BLACK = 0x0000
C_RED = 0b11111_000000_00000
C_GREEN = 0b00000_111111_00000
C_BLUE = 0b00000_000000_11111
C_NONE = -1
C_INVERT = -2

# Text alignment constants
DTEXT_LEFT = 'left'
DTEXT_CENTER = 'center'
DTEXT_RIGHT = 'right'
DTEXT_TOP = 'top'
DTEXT_MIDDLE = 'middle'
DTEXT_BOTTOM = 'bottom'

# Image stuff
IMAGE_MONO = 0
IMAGE_P4_RGB565 = 1
IMAGE_RGB565 = 2

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((DWIDTH, DHEIGHT))
pygame.display.set_caption("ClassPad")
vram = pygame.Surface((DWIDTH, DHEIGHT))
clock = pygame.time.Clock()
FPS = 100  # Adjust to control game speed

# --- NEW: Window Clipping State ---
_dwindow = (0, 0, DWIDTH, DHEIGHT)

def _to_rgb(color: int) -> tuple:
    """Convert RGB888 int to pygame color tuple"""
    # return ((color >> 16) & 0xFF, (color >> 8) & 0xFF, color & 0xFF)
    # if it fits in 16 bits, decode RGB565 → RGB888
    if 0 <= color <= 0xFFFF:
        r5 = (color >> 11) & 0x1F
        g6 = (color >>  5) & 0x3F
        b5 =  color        & 0x1F
        # expand to 8 bits:   abcde → abcde00 | abcde>>3
        r8 = (r5 << 3) | (r5 >> 2)
        g8 = (g6 << 2) | (g6 >> 4)
        b8 = (b5 << 3) | (b5 >> 2)
        return (r8, g8, b8)
    # otherwise assume it’s already RGB888
    return ((color >> 16) & 0xFF,
            (color >>  8) & 0xFF,
             color        & 0xFF)

def _from_rgb(pixel: pygame.Color) -> int:
    """Convert pygame color to RGB888 int"""
    return (pixel[0] << 16) | (pixel[1] << 8) | pixel[2]

def C_RGB(r: int, g: int, b: int) -> int:
    """Create RGB888 from RGB555 components"""
    # r8 = (r << 3) | (r >> 2)
    # g8 = (g << 3) | (g >> 2)
    # b8 = (b << 3) | (b >> 2)
    # return (r8 << 16) | (g8 << 8) | b8
    return ((r & 0x1F) << 11) | ((g & 0x3F) << 6) | (b & 0x1F)

def dwindow_get() -> Tuple[int, int, int, int]:
    """Get the current rendering window clipping rectangle."""
    return _dwindow

def dwindow_set(left: int, top: int, right: int, bottom: int):
    """Set the rendering window to clip drawing operations."""
    global _dwindow
    _dwindow = (left, top, right, bottom)
    
    # Use pygame's built-in clipping for efficiency
    clip_rect = pygame.Rect(left, top, right - left, bottom - top)
    vram.set_clip(clip_rect)

# Drawing functions
def dclear(color: int):
    if color == C_NONE:
        return
    vram.fill(_to_rgb(color))

def dupdate():
    """Update display with VRAM changes"""
    screen.blit(vram, (0, 0))
    pygame.display.flip()
    clock.tick(FPS)

def dpixel(x: int, y: int, color: int):
    if color == C_NONE or not (0 <= x < DWIDTH and 0 <= y < DHEIGHT):
        return
    vram.set_at((x, y), _to_rgb(color))

def dgetpixel(x: int, y: int) -> int:
    if not (0 <= x < DWIDTH and 0 <= y < DHEIGHT):
        return C_NONE
    return _from_rgb(vram.get_at((x, y)))

def drect(x1: int, y1: int, x2: int, y2: int, color: int):
    if color == C_NONE:
        return
    x = min(x1, x2)
    y = min(y1, y2)
    w = abs(x2 - x1) + 1
    h = abs(y2 - y1) + 1
    pygame.draw.rect(vram, _to_rgb(color), pygame.Rect(x, y, w, h))

def drect_border(x1: int, y1: int, x2: int, y2: int,
               fill: int, border_width: int, border: int):
    if fill != C_NONE:
        drect(x1, y1, x2, y2, fill)
    
    if border != C_NONE and border_width > 0:
        x = min(x1, x2)
        y = min(y1, y2)
        w = abs(x2 - x1)
        h = abs(y2 - y1)
        pygame.draw.rect(vram, _to_rgb(border), pygame.Rect(x, y, w, h), border_width)

def dline(x1: int, y1: int, x2: int, y2: int, color: int):
    if color == C_NONE:
        return
    pygame.draw.line(vram, _to_rgb(color), (x1, y1), (x2, y2))

def dhline(y: int, color: int):
    dline(0, y, DWIDTH-1, y, color)

def dvline(x: int, color: int):
    dline(x, 0, x, DHEIGHT-1, color)

def dcircle(x: int, y: int, r: int, fill: int, border: int):
    if fill != C_NONE:
        pygame.draw.circle(vram, _to_rgb(fill), (x, y), r)
    if border != C_NONE:
        pygame.draw.circle(vram, _to_rgb(border), (x, y), r, 1)

def dellipse(x1: int, y1: int, x2: int, y2: int, fill: int, border: int):
    rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2-x1), abs(y2-y1))
    if fill != C_NONE:
        pygame.draw.ellipse(vram, _to_rgb(fill), rect)
    if border != C_NONE:
        pygame.draw.ellipse(vram, _to_rgb(border), rect, 1)

def dpoly(vertices: List[int], fill: int, border: int):
    """Draw polygon with fill and border"""
    if len(vertices) % 2 != 0:
        raise ValueError("Vertices must contain even number of coordinates")
    
    points = [(vertices[i], vertices[i+1]) for i in range(0, len(vertices), 2)]
    
    # Draw filled polygon
    if fill != C_NONE:
        pygame.draw.polygon(vram, _to_rgb(fill), points, 0)
    
    # Draw border
    if border != C_NONE:
        pygame.draw.polygon(vram, _to_rgb(border), points, 1)



# ------------------------------------------------------------------------------

# Fonts
        

class GintFont:
    def __init__(self, prop, line_height, data_height, block_count, glyph_count,
                 char_spacing, line_distance, blocks, data, width, storage_size,
                 glyph_index, glyph_width):
        self.prop = prop
        self.line_height = line_height
        self.data_height = data_height
        self.block_count = block_count
        self.glyph_count = glyph_count
        self.char_spacing = char_spacing
        self.line_distance = line_distance
        self.blocks = blocks
        self.data = data
        self.width = width
        self.storage_size = storage_size
        self.glyph_index = glyph_index
        self.glyph_width = glyph_width


_default_font = GintFont(  # Create a default font object
    prop=1, line_height=9, data_height=9, block_count=1,
    glyph_count=95, char_spacing=1, line_distance=14,
    blocks=b'', data=b'', width=0, storage_size=0,
    glyph_index=b'', glyph_width=b''
)
_current_font = _default_font

def dfont(font: GintFont):
    global _current_font
    _current_font = font

# ------------------------------------------------------------------------------

# Load bitmap font
_uf8x9_font = pygame.image.load("_data/font8x9.png").convert()
# _uf8x9_font = pygame.image.load("_data/uf8x9.png").convert()
_uf8x9_font.set_colorkey((255, 255, 255))  # Make white transparent
_uf8x9_font = _uf8x9_font.convert_alpha()

# Font character cache {unicode_code: (surface, width)}
_font_cache = {}

# Font grid constants
GLYPH_WIDTH = 8
GLYPH_HEIGHT = 10
GAP = 1
FONT_CELL_WIDTH = GLYPH_WIDTH + GAP*2
FONT_CELL_HEIGHT = GAP + GLYPH_HEIGHT + GAP*2

# Line definitions (start code, chars per line)
LINE_DEFS = [
    (0x0020, 16),  # Space to / (16 chars)
    (0x0030, 16),  # 0 to ? 
    (0x0040, 16),  # @ to O
    (0x0050, 16),  # P to _
    (0x0060, 16),  # ` to o
    (0x0070, 16)   # p to DEL
]

def _get_glyph(font: GintFont, char: str):
    """Get glyph surface and width with 1px gap grid layout"""
    code = ord(char)
    
    if code in _font_cache:
        return _font_cache[code]
    
    # Find which line the character is in
    line_index = -1
    for i, (start, count) in enumerate(LINE_DEFS):
        if start <= code < start + count:
            line_index = i
            break
    
    if line_index == -1:
        return _get_glyph(font, ' ')  # Fallback to space
    
    # Calculate grid position
    col = code - LINE_DEFS[line_index][0]
    row = line_index
    
    # Calculate coordinates in texture (with 1px gaps)
    x = (col * FONT_CELL_WIDTH) - GAP  # Compensate left offset
    y = (row * FONT_CELL_HEIGHT) - GAP  # Compensate top offset
    
    try:
        # Extract glyph (8x9 area inside cell)
        glyph = _uf8x9_font.subsurface(
            x + GAP,  # Original GAP compensation
            y + GAP,   # Original GAP compensation
            GLYPH_WIDTH + GAP, 
            GLYPH_HEIGHT + GAP
        )
    except ValueError:
        return _get_glyph(font, ' ')  # Fallback
    
    # Calculate proportional width
    width = GLYPH_WIDTH + 1
    for x_pos in reversed(range(GLYPH_WIDTH)):
        if any(glyph.get_at((x_pos, y_pos))[3] > 0 
               for y_pos in range(GLYPH_HEIGHT)):
            width = x_pos + 1
            break
    
    _font_cache[code] = (glyph, width)
    return glyph, width

def dsize(text: str, font: Optional[GintFont]) -> Tuple[int, int]:
    """Get the width and height of rendered text."""
    if not text:
        return 0, GLYPH_HEIGHT
    
    font = font or _current_font
    
    widths = [_get_glyph(font, c)[1] for c in text]
    # Sum of glyph widths + spacing between them
    total_width = sum(widths) + (len(text) - 1) * font.char_spacing
    
    return total_width, GLYPH_HEIGHT

def dnsize(text: str, size: int, font: Optional[GintFont]) -> Tuple[int, int]:
    """Get the width and height of a prefix of a rendered text."""
    if size < 0:
        return dsize(text, font)
    
    # Simulate byte limit by encoding, slicing, and decoding
    limited_text = text.encode('utf-8')[:size].decode('utf-8', errors='ignore')
    return dsize(limited_text, font)

def drsize(text: str, font: Optional[GintFont], width: int) -> Tuple[int, int]:
    """
    Determine how many characters fit in a given width.

    Note:
        The returned byte_offset is not reliable for slicing strings that
        contain multi-byte Unicode characters. Slicing with `str[:offset]`
        may fail. This is a known issue.
    """
    font = font or _current_font
    byte_offset = 0
    actual_width = 0
    
    for i, char in enumerate(text):
        glyph_w = _get_glyph(font, char)[1]
        
        # Width this character would occupy (including preceding space)
        char_total_w = glyph_w + (font.char_spacing if i > 0 else 0)
        
        if actual_width + char_total_w > width:
            break # Character does not fit, stop here.
        
        # It fits, commit the changes
        actual_width += char_total_w
        byte_offset += len(char.encode('utf-8'))
        
    return byte_offset, actual_width


# Updated text rendering with precise spacing
def dtext(x: int, y: int, color: int, text: str,
          align=DTEXT_LEFT, valign=DTEXT_TOP):
    if color == C_NONE or not text:
        return
    
    font = _current_font or _default_font
    
    # Calculate total width and heights
    # widths = [_get_glyph(font, c)[1] for c in text]
    # total_width = sum(widths)
    # total_height = GLYPH_HEIGHT
    total_width, total_height = dsize(text, font)
    
    # Horizontal alignment
    if align == DTEXT_CENTER:
        x -= total_width // 2
    elif align == DTEXT_RIGHT:
        x -= total_width
    
    # Vertical alignment
    if valign == DTEXT_MIDDLE:
        y -= total_height // 2
    elif valign == DTEXT_BOTTOM:
        y -= total_height
    
    # Draw each character
    cursor_x = x
    for char in text:
        glyph, width = _get_glyph(font, char)
        
        # Create colored glyph
        mask = pygame.mask.from_surface(glyph)
        colored = pygame.Surface(glyph.get_size(), pygame.SRCALPHA)
        mask.to_surface(colored, setcolor=_to_rgb(color), unsetcolor=(0,0,0,0))
        
        vram.blit(colored, (cursor_x - GAP, y - GAP))
        cursor_x += width + font.char_spacing


def dtext_opt(x: int, y: int, fg: int, bg: int, 
            halign: str, valign: str, text: str, size: int = -1):
    if not text:
        return
    
    font = _current_font or _default_font
    total_width, total_height = dsize(text, font)


    # Horizontal alignment
    if halign == DTEXT_CENTER:
        x -= total_width // 2
    elif halign == DTEXT_RIGHT:
        x -= total_width
    
    # Vertical alignment
    if valign == DTEXT_MIDDLE:
        y -= total_height // 2
    elif valign == DTEXT_BOTTOM:
        y -= total_height
    
    
    # Draw background (if requested)
    if bg != C_NONE:
        bg_rect = pygame.Rect(
            x - 1, y - 1,
            total_width + 2, total_height + 2
        )
        pygame.draw.rect(vram, _to_rgb(bg), bg_rect)
    
    # Draw text characters
    cursor_x = x
    for char in text:
        glyph, width = _get_glyph(font, char)
        
        # Create colored glyph
        mask = pygame.mask.from_surface(glyph)
        colored = pygame.Surface(glyph.get_size(), pygame.SRCALPHA)
        mask.to_surface(colored, setcolor=_to_rgb(fg), unsetcolor=(0,0,0,0))
        
        vram.blit(colored, (cursor_x - GAP, y - GAP))
        cursor_x += width + font.char_spacing

# Key Events

pygame.event.set_allowed([
    QUIT, KEYDOWN, KEYUP,
    ACTIVEEVENT, VIDEORESIZE, VIDEOEXPOSE,
    MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION
])

# Key constants
KEY_F1		= 0x91
KEY_F2		= 0x92
KEY_F3		= 0x93
KEY_F4		= 0x94
KEY_F5		= 0x95
KEY_F6		= 0x96

KEY_SHIFT	= 0x81
KEY_OPTN	= 0x82
KEY_VARS	= 0x83
KEY_MENU	= 0x84
KEY_LEFT	= 0x85
KEY_UP		= 0x86

KEY_ALPHA	= 0x71
KEY_SQUARE	= 0x72
KEY_POWER	= 0x73
KEY_EXIT	= 0x74
KEY_DOWN	= 0x75
KEY_RIGHT	= 0x76

KEY_XOT		= 0x61
KEY_LOG		= 0x62
KEY_LN		= 0x63
KEY_SIN		= 0x64
KEY_COS		= 0x65
KEY_TAN		= 0x66

KEY_FRAC	= 0x51
KEY_FD		= 0x52
KEY_LEFTP	= 0x53
KEY_RIGHTP	= 0x54
KEY_COMMA	= 0x55
KEY_ARROW	= 0x56

KEY_7		= 0x41
KEY_8		= 0x42
KEY_9		= 0x43
KEY_DEL		= 0x44
# AC/ON has keycode 0x07 instead of 0x45

KEY_4		= 0x31
KEY_5		= 0x32
KEY_6		= 0x33
KEY_MUL		= 0x34
KEY_DIV		= 0x35

KEY_1		= 0x21
KEY_2		= 0x22
KEY_3		= 0x23
KEY_ADD		= 0x24
KEY_SUB		= 0x25

KEY_0		= 0x11
KEY_DOT		= 0x12
KEY_EXP		= 0x13
KEY_NEG		= 0x14
KEY_EXE		= 0x15

# Why is AC/ON not 0x45? Because it must be on a row/column of its
#   own. It's used to power up the calculator; if it were in the middle
#   of the matrix one could use a ghosting effect to boot the calc.
KEY_ACON	= 0x07

# Virtual key codes
KEY_HELP	= 0x20 # fx-9860G Slim: 0x75 */
KEY_LIGHT	= 0x10 # fx-9860G Slim: 0x76 */

# Key codes for the CP-400
KEY_KBD		= 0xa1
KEY_X		= 0xa2
KEY_Y		= 0xa3
KEY_Z		= 0xa4
KEY_EQUALS	= 0xa5
KEY_CLEAR   = KEY_EXIT

# Key aliases (handle with care =D)
KEY_X2		= KEY_SQUARE
KEY_CARET	= KEY_POWER
KEY_SWITCH	= KEY_FD
KEY_LEFTPAR	= KEY_LEFTP
KEY_RIGHTPAR	= KEY_RIGHTP
KEY_STORE	= KEY_ARROW
KEY_TIMES	= KEY_MUL
KEY_PLUS	= KEY_ADD
KEY_MINUS	= KEY_SUB

# Key event types
KEYEV_NONE: int = 0
KEYEV_DOWN: int = 1
KEYEV_UP: int = 2
KEYEV_HOLD: int = 3

KEYEV_TOUCH_DOWN = 10
KEYEV_TOUCH_UP = 11
KEYEV_TOUCH_DRAG = 12

KEY_NONE = None

# Key options flags
GETKEY_DEFAULT = 0
GETKEY_MOD_SHIFT = 1
GETKEY_MOD_ALPHA = 2

# Map Pygame keys to gint keys
_key_mapping = {
    K_UP: KEY_UP,
    K_DOWN: KEY_DOWN,
    K_LEFT: KEY_LEFT,
    K_RIGHT: KEY_RIGHT,
    K_ESCAPE: KEY_EXIT,
    K_F4: KEY_EXIT,
    K_a: KEY_ALPHA,
    K_EQUALS: KEY_EQUALS,
    K_x: KEY_X,
    K_y: KEY_Y,
    K_z: KEY_Z,
    K_POWER: KEY_POWER,
    K_KP_DIVIDE: KEY_DIV,
    K_LEFTPAREN: KEY_LEFTPAR,
    K_RIGHTPAREN: KEY_RIGHTPAR,
    K_COMMA: KEY_COMMA,
    K_PLUS: KEY_ADD,
    K_KP_PLUS: KEY_ADD,
    K_MINUS: KEY_MINUS,
    K_KP_MINUS: KEY_MINUS,
    # (-) ?
    K_CARET: KEY_NEG,
    K_SPACE: KEY_EXE,
    K_9: KEY_9,
    K_KP_9: KEY_9,
    K_8: KEY_8,
    K_KP_8: KEY_8,
    K_7: KEY_7,
    K_KP_7: KEY_7,
    K_6: KEY_6,
    K_KP_6: KEY_6,
    K_5: KEY_5,
    K_KP_5: KEY_5,
    K_4: KEY_4,
    K_KP_4: KEY_4,
    K_3: KEY_3,
    K_KP_3: KEY_3,
    K_2: KEY_2,
    K_KP_2: KEY_2,
    K_1: KEY_1,
    K_KP_1: KEY_1,
    K_0: KEY_0,
    K_KP_0: KEY_0,
    # Key dot ?
    K_KP_MULTIPLY: KEY_MUL,
    K_KP_ENTER: KEY_EXE,
    K_KP_PERIOD: KEY_DOT,
    K_PERIOD: KEY_DOT,
    K_e: KEY_EXP,
    K_BACKSPACE: KEY_DEL,
    K_LSHIFT: KEY_SHIFT,
    K_RSHIFT: KEY_SHIFT,
    K_RETURN: KEY_EXE,
    K_RALT: KEY_KBD,
    K_LALT: KEY_KBD
}

# State tracking
_key_states = {}
_modifiers = {'shift': False, 'alpha': False}
_last_key_time = 0
_repeat_delay = 400  # ms
_repeat_interval = 40  # ms

class _Event:
    def __init__(self, type=None, key=None):
        self.type = type
        self.key = key

class KeyEvent(_Event):
    def __init__(self, event_type=KEYEV_NONE, key=None, pos=(0, 0)):
        super().__init__(event_type, key)

        self.time = int(time.monotonic() * 1000)
        self.mod = False
        self.shift = _modifiers['shift']
        self.alpha = _modifiers['alpha']
        self.type = event_type
        self.key = key
        self.x, self.y = pos

    time: int
    mod: bool
    shift: bool
    alpha: bool
    type: int
    key: Optional[int]
    x: int
    y: int

    def __repr__(self):
        return f"KeyEvent(type={self.type}, key={self.key}, shift={self.shift}, alpha={self.alpha})"

class NoneEvent(KeyEvent):
    def __init__(self):
        super().__init__(KEYEV_NONE, None)


def _update_modifiers():
    """Update modifier states from keyboard"""
    mods = pygame.key.get_mods()
    _modifiers['shift'] = bool(mods & KMOD_SHIFT)
    # Alpha state tracking (using Caps Lock as example)
    _modifiers['alpha'] = bool(pygame.key.get_mods() & KMOD_CAPS)

# Reverse mapping from gint keys to Pygame keys
_inverse_key_mapping = {}
for pg_key, custom_key in _key_mapping.items():
    if custom_key not in _inverse_key_mapping:
        _inverse_key_mapping[custom_key] = []
    _inverse_key_mapping[custom_key].append(pg_key)

# Add special case for mouse position tracking
MOUSE_X = 2000
MOUSE_Y = 2001
_inverse_key_mapping.update({
    MOUSE_X: [K_UNKNOWN],  # Placeholders
    MOUSE_Y: [K_UNKNOWN]
})


def pollevent():
    global _key_states
    _update_modifiers()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            return KeyEvent(KEYEV_DOWN, KEY_EXIT)
        
        elif event.type == VIDEOEXPOSE:  # <-- Triggered when window needs redraw
            dupdate()

        elif event.type == ACTIVEEVENT:
            # Redraw when window gains focus (optional)
            if event.gain == 1:  # 1 = window activated
                dupdate()
        
        # Handle mouse events as touch input
        elif event.type == MOUSEBUTTONDOWN:
            return KeyEvent(KEYEV_TOUCH_DOWN, None, event.pos)
            
        elif event.type == MOUSEBUTTONUP:
            return KeyEvent(KEYEV_TOUCH_UP, None, event.pos)
            
        elif event.type == MOUSEMOTION:
            if event.buttons[0]:  # Left mouse button dragged
                return KeyEvent(KEYEV_TOUCH_DRAG, None, event.pos)
            
        elif event.type == KEYDOWN:
            # Capture Print Screen key to save VRAM
            if event.key == pygame.K_PRINTSCREEN:  # <-- Add this block
                pygame.image.save(vram, "screenshot.png")
                continue  # Skip further processing for this event
                
            if event.key in _key_mapping:
                mapped = _key_mapping[event.key]
                _key_states[mapped] = {
                    'time': pygame.time.get_ticks(),
                    'last_repeat': pygame.time.get_ticks()
                }
                return KeyEvent(KEYEV_DOWN, mapped)
                
        elif event.type == KEYUP:
            if event.key in _key_mapping:
                mapped = _key_mapping[event.key]
                if mapped in _key_states:
                    del _key_states[mapped]
                return KeyEvent(KEYEV_UP, mapped)
    
    return KeyEvent(KEYEV_NONE, None)

def getkey() -> KeyEvent:
    return getkey_opt(GETKEY_DEFAULT, None)

def getkey_opt(options: int, timeout_ms: Optional[int] = 2000) -> KeyEvent:
    start_time = pygame.time.get_ticks()
    
    while True:
        # Process existing events first
        ev = pollevent()
        if ev.type != KEYEV_NONE:
            if ev.key == KEY_EXIT and not ev.shift and not ev.alpha:
                pygame.quit()
                sys.exit()
            return ev
        
        # Check timeout
        if timeout_ms is not None and (pygame.time.get_ticks() - start_time) > timeout_ms:
            return KeyEvent(KEYEV_NONE, None)
        
        # Handle key repeats
        current_time = pygame.time.get_ticks()
        for key in list(_key_states.keys()):
            state = _key_states[key]
            if (current_time - state['time']) > _repeat_delay:
                if (current_time - state['last_repeat']) > _repeat_interval:
                    _key_states[key]['last_repeat'] = current_time
                    return KeyEvent(KEYEV_HOLD, key)
        
        # Prevent CPU hogging
        pygame.time.wait(10)

def keydown(key: int) -> bool:
    """Check if a specific key is currently pressed"""
    pressed = pygame.key.get_pressed()
    return any(pressed[pg_key] for pg_key in _inverse_key_mapping.get(key, []))

def keydown_all(*keys: int) -> bool:
    """Check if all specified keys are pressed"""
    pressed = pygame.key.get_pressed()
    return all(any(pressed[pg_key] for pg_key in _inverse_key_mapping.get(key, [])) 
                for key in keys)

def keydown_any(*keys: int) -> bool:
    """Check if any of specified keys are pressed"""
    pressed = pygame.key.get_pressed()
    return any(any(pressed[pg_key] for pg_key in _inverse_key_mapping.get(key, [])) 
               for key in keys)

def clearevents():
    """Clear all pending events from the queue"""
    pygame.event.clear()

def cleareventflips():
    global _key_states
    global _modifiers
    
    _key_states = {}
    _modifiers = {'shift': False, 'alpha': False}

# --------------------------------------------------------------
# Image stuff
IMAGE_MONO = 0
IMAGE_RGB565 = 1
IMAGE_RGB565A = 2
IMAGE_P8_RGB565 = 3
IMAGE_P8_RGB565A = 4
IMAGE_P4_RGB565 = 5
IMAGE_P4_RGB565A = 6

class Image:
    """Represents a graphical image in VRAM"""
    def __init__(self, format: int, profile: int, color_count: int, width: int, height: int, 
                stride: int, data: bytes, palette: bytes):
        self.format = format
        self.profile = profile
        self.color_count = color_count
        self.width = width
        self.height = height
        self.stride = stride
        self.data = data
        self.palette = palette
        self.surface = self._decode_image()

    def _decode_image(self) -> pygame.Surface:
        surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pixels = pygame.PixelArray(surface)
        
        if self.profile == IMAGE_MONO:
            # 1‑bpp: bit 0 = black, bit 1 = white
            for y in range(self.height):
                row = y * self.stride
                for x in range(self.width):
                    byte = self.data[row + (x >> 3)]
                    bit  = (byte >> (7 - (x & 7))) & 1
                    pixels[x, y] = (255,255,255) if bit else (0,0,0)
        
        elif self.profile == IMAGE_RGB565:
            # Decode 16bpp direct color
            for y in range(self.height):
                for x in range(self.width):
                    px_idx = (y * self.width + x) * 2
                    rgb565 = struct.unpack('>H', self.data[px_idx:px_idx+2])[0]
                    r = (rgb565 >> 11) * 255 // 31
                    g = ((rgb565 >> 5) & 0x3F) * 255 // 63
                    b = (rgb565 & 0x1F) * 255 // 31
                    pixels[x, y] = (r, g, b)
        
        elif self.profile == IMAGE_RGB565A:
            # 16‑bpp with 1-bit alpha
            ALPHA_VAL = 0x0001   # as in fxconv’s CgProfile
            for y in range(self.height):
                for x in range(self.width):
                    off = y * self.stride + x*2
                    c = struct.unpack('>H', self.data[off:off+2])[0]
                    if c == ALPHA_VAL:
                        # leave pixel transparent
                        continue
                    # if c collided with alpha value, fxconv flips its low‑bit
                    # but you can ignore that here
                    r = (c >> 11) * 255 // 31
                    g = ((c >> 5) & 0x3F) * 255 // 63
                    b = (c & 0x1F) * 255 // 31
                    pixels[x, y] = (r, g, b, 255)
        
        elif self.profile in (IMAGE_P8_RGB565, IMAGE_P8_RGB565A):
            # 8‑bpp indexed
            PALETTE_BASE = 0x80  # for RGB565; 0x81 if you’re using the ‘a’ profile
            ALPHA_IDX    = 0x80  # only for IMAGE_P8_RGB565A
            # build 256‑entry palette from your 2‑byte‑per‑entry self.palette
            palette = []
            for i in range(0, len(self.palette), 2):
                rgb565 = struct.unpack('>H', self.palette[i:i+2])[0]
                r = (rgb565 >> 11) * 255 // 31
                g = ((rgb565 >> 5) & 0x3F) * 255 // 63
                b = (rgb565 & 0x1F) * 255 // 31
                palette.append((r, g, b))
            for y in range(self.height):
                row = y * self.stride
                for x in range(self.width):
                    c = self.data[row + x]
                    if self.profile == IMAGE_P8_RGB565A and c == ALPHA_IDX:
                        continue
                    idx = c - PALETTE_BASE
                    pixels[x, y] = palette[idx]

        elif self.profile in (IMAGE_P4_RGB565, IMAGE_P4_RGB565A):
            # 4‑bpp indexed: two pixels per byte
            PALETTE_BASE = 0     # for non‑alpha; 1 for the ‘a’ profile
            ALPHA_IDX    = 0     # only for IMAGE_P4_RGB565A
            palette = []
            for i in range(0, len(self.palette), 2):
                rgb565 = struct.unpack('>H', self.palette[i:i+2])[0]
                r = (rgb565 >> 11) * 255 // 31
                g = ((rgb565 >> 5) & 0x3F) * 255 // 63
                b = (rgb565 & 0x1F) * 255 // 31
                palette.append((r, g, b))
            for y in range(self.height):
                row = y * self.stride
                for x in range(self.width):
                    byte = self.data[row + (x >> 1)]
                    # even pixel in high nibble, odd in low
                    nibble = (byte >> 4) if (x & 1)==0 else (byte & 0xF)
                    if self.profile == IMAGE_P4_RGB565A and nibble == ALPHA_IDX:
                        continue
                    idx = nibble - PALETTE_BASE
                    pixels[x, y] = palette[idx]

        elif self.profile == IMAGE_P4_RGB565:
            # Decode 4bpp palette-based image
            palette = []
            for i in range(0, len(self.palette), 2):
                rgb565 = struct.unpack('>H', self.palette[i:i+2])[0]
                r = (rgb565 >> 11) * 255 // 31
                g = ((rgb565 >> 5) & 0x3F) * 255 // 63
                b = (rgb565 & 0x1F) * 255 // 31
                palette.append((r, g, b))
            
            for y in range(self.height):
                for x in range(self.width):
                    byte_idx = y * self.stride + (x // 2)
                    byte = self.data[byte_idx]
                    nibble = (byte >> 4) if x % 2 == 0 else (byte & 0x0F)
                    
                    pixels[x, y] = palette[nibble]

        
        
        elif self.profile == IMAGE_P8_RGB565:
            # 8‑bit palette‑based image -----------------------------------------
            # The converter stores indices that start at 0x80 (palette_base)      # ←
            # so we must subtract that offset before looking them up.             #
            PALETTE_BASE = 0x80                                                   # |
            palette = []
            for i in range(0, len(self.palette), 2):
                rgb565 = struct.unpack('>H', self.palette[i:i+2])[0]
                r = (rgb565 >> 11) * 255 // 31
                g = ((rgb565 >> 5) & 0x3F) * 255 // 63
                b = (rgb565 & 0x1F) * 255 // 31
                palette.append((r, g, b))

            for y in range(self.height):
                row = y * self.stride
                for x in range(self.width):
                    idx = self.data[row + x] - PALETTE_BASE
                    pixels[x, y] = palette[idx]
        
        pixels.close()
        return surface

def image(profile: int, color_count: int, width: int, height: int, 
                stride: int, data: bytearray, palette: bytearray) -> Image:
    return Image(IMAGE_RGB565, profile, color_count, width, height, stride, data, palette)

def image_rgb565(width: int, height: int, data: bytes) -> Image:
    """
    16‑bpp RGB565, tightly packed (no alpha, no padding)
    """
    stride = width * 2
    return Image(
        format=IMAGE_RGB565,
        profile=IMAGE_RGB565,
        color_count=0,
        width=width,
        height=height,
        stride=stride,
        data=data,
        palette=b''
    )

def image_rgb565a(width: int, height: int, data: bytes) -> Image:
    """
    16‑bpp RGB565 + 1‑bit alpha (alpha index == 0x0001)
    """
    stride = width * 2
    return Image(
        format=IMAGE_RGB565A,
        profile=IMAGE_RGB565A,
        color_count=0,
        width=width,
        height=height,
        stride=stride,
        data=data,
        palette=b''
    )

def image_p8_rgb565(width: int, height: int, data: bytes, palette: bytes) -> Image:
    """
    8‑bpp palette (indices 0x80…0xFF) RGB565
    """
    stride      = width         # one byte per pixel
    color_count = len(palette) // 2
    return Image(
        format=IMAGE_P8_RGB565,
        profile=IMAGE_P8_RGB565,
        color_count=color_count,
        width=width,
        height=height,
        stride=stride,
        data=data,
        palette=palette
    )


def image_p8_rgb565a(width: int, height: int, data: bytes, palette: bytes) -> Image:
    """
    8‑bpp palette (0x81…0xFF), RGB565 + transparent index (0x80)
    """
    stride      = width
    color_count = len(palette) // 2
    return Image(
        format=IMAGE_P8_RGB565A,
        profile=IMAGE_P8_RGB565A,
        color_count=color_count,
        width=width,
        height=height,
        stride=stride,
        data=data,
        palette=palette
    )

def image_p4_rgb565(width: int, height: int, data: bytes, palette: bytes) -> Image:
    """
    4‑bpp palette (16 entries) RGB565
    """
    stride      = (width + 1) // 2   # two pixels per byte
    color_count = len(palette) // 2
    return Image(
        format=IMAGE_P4_RGB565,
        profile=IMAGE_P4_RGB565,
        color_count=color_count,
        width=width,
        height=height,
        stride=stride,
        data=data,
        palette=palette
    )

def image_p4_rgb565a(width: int, height: int, data: bytes, palette: bytes) -> Image:
    """
    4‑bpp palette (16 entries) RGB565 + transparent entry at index 0
    """
    stride      = (width + 1) // 2
    color_count = len(palette) // 2
    return Image(
        format=IMAGE_P4_RGB565A,
        profile=IMAGE_P4_RGB565A,
        color_count=color_count,
        width=width,
        height=height,
        stride=stride,
        data=data,
        palette=palette
    )

def dimage(x: int, y: int, img: Image):
    """Draw entire image at specified coordinates"""
    vram.blit(img.surface, (x, y))

def dsubimage(x: int, y: int, img: Image,
             left: int, top: int, width: int, height: int):
    """Draw subregion of image"""
    sub_rect = pygame.Rect(left, top, width, height)
    sub_surf = img.surface.subsurface(sub_rect)
    vram.blit(sub_surf, (x, y))

#  --- Polyfill
    
import time
import gc
import sys
import traceback
from typing import Any, Optional

# Polyfill for time.sleep_ms() and time.sleep_us()
if not hasattr(time, 'sleep_ms'):
    def time_sleep_ms(ms: int):
        """Polyfill for time.sleep_ms. Pauses execution for a number of milliseconds."""
        time.sleep(ms / 1000.0)
    time.sleep_ms = time_sleep_ms

if not hasattr(time, 'sleep_us'):
    def time_sleep_us(us: int):
        """Polyfill for time.sleep_us. Pauses execution for a number of microseconds."""
        time.sleep(us / 1_000_000.0)
    time.sleep_us = time_sleep_us

if not hasattr(time, 'ticks_ms'):
    TICKS_PERIOD = 2**30
    TICKS_MAX = TICKS_PERIOD - 1
    TICKS_HALF_PERIOD = TICKS_PERIOD // 2

    def ticks_ms() -> int:
        """Polyfill for time.ticks_ms. Returns a wrapping millisecond counter."""
        return int(time.monotonic() * 1000) & TICKS_MAX

    def ticks_us() -> int:
        """Polyfill for time.ticks_us. Returns a wrapping microsecond counter."""
        return int(time.monotonic() * 1_000_000) & TICKS_MAX

    def ticks_cpu() -> int:
        """Polyfill for time.ticks_cpu. Alias to ticks_us for simulation."""
        return ticks_us()

    def ticks_add(ticks: int, delta: int) -> int:
        """Polyfill for time.ticks_add. Correctly adds a value to a wrapping ticks counter."""
        return (ticks + delta) & TICKS_MAX

    def ticks_diff(ticks1: int, ticks2: int) -> int:
        """Polyfill for time.ticks_diff. Correctly finds the difference between two wrapping ticks values."""
        return ((ticks1 - ticks2 + TICKS_HALF_PERIOD) & TICKS_MAX) - TICKS_HALF_PERIOD

    time.ticks_ms = ticks_ms
    time.ticks_us = ticks_us
    time.ticks_cpu = ticks_cpu
    time.ticks_add = ticks_add
    time.ticks_diff = ticks_diff

# Polyfills for MicroPython-specific gc functions
if not hasattr(gc, 'mem_alloc'):
    def gc_mem_alloc() -> int:
        """Polyfill for gc.mem_alloc. Not implementable in CPython, returns 0."""
        print("Warning: gc.mem_alloc() is a MicroPython-specific function. Returning 0.")
        return 0
    gc.mem_alloc = gc_mem_alloc

if not hasattr(gc, 'mem_free'):
    def gc_mem_free() -> int:
        """Polyfill for gc.mem_free. Not implementable in CPython, returns a large number."""
        print("Warning: gc.mem_free() is a MicroPython-specific function. Returning a dummy value.")
        # Return a large number to avoid false "out of memory" errors in simulations
        return 1024 * 1024
    gc.mem_free = gc_mem_free

if not hasattr(gc, 'threshold'):
    def gc_threshold(amount: Optional[int] = None) -> int:
        """Polyfill for gc.threshold. Simulates getting/setting the threshold."""
        current_thresholds = gc.get_threshold()
        if amount is not None:
            print(f"Warning: gc.threshold() is a MicroPython-specific function. Setting a dummy value.")
            # We can't really set it in the same way, but we can fake it.
            # This doesn't actually do anything in CPython.
            pass
        return current_thresholds[0]
    gc.threshold = gc_threshold

# Create a dummy micropython module since it doesn't exist in standard Python
class MicroPythonModule:
    def const(self, expr: Any) -> Any:
        """Polyfill for micropython.const. Returns the expression as-is."""
        return expr

    def opt_level(self, level: Optional[int] = None) -> int:
        """Polyfill for micropython.opt_level. Does nothing and returns 0."""
        if level is not None:
            print(f"Warning: micropython.opt_level({level}) called. No effect in CPython.")
        return 0

    def heap_lock(self) -> int:
        """Polyfill for micropython.heap_lock. Does nothing and returns 0."""
        return 0

    def heap_unlock(self) -> int:
        """Polyfill for micropython.heap_unlock. Does nothing and returns 0."""
        return 0
    
    def kbd_intr(self, chr_val: int):
        """Polyfill for micropython.kbd_intr. Does nothing."""
        pass

# Add the dummy module to sys.modules
if 'micropython' not in sys.modules:
    sys.modules['micropython'] = MicroPythonModule()


if not hasattr(sys, 'print_exception'):
    def sys_print_exception(exc: Exception, file=sys.stdout):
        """
        Polyfill for sys.print_exception. Uses the standard `traceback` module.
        """
        traceback.print_exception(type(exc), exc, exc.__traceback__, file=file)
    sys.print_exception = sys_print_exception

#  --- INIT STUFF
    
vram.fill(C_WHITE)
dupdate()