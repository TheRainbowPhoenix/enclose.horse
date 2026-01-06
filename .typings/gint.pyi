# Generated automatically from modgint.c

from typing import Any, List, Literal, Optional, Tuple, Union

BufferLike = Any

class KeyEvent:
    time: int
    mod: bool
    shift: bool
    alpha: bool
    type: int
    key: int
    x: int
    y: int

class image:
    """
    Represents a graphical image in VRAM. On black-and-white models:
    - Supports 2-5 colors via different profiles
    - Data stored in packed row-major format (32 pixels per 4-byte word)

    Attributes:
        profile: IMAGE_MONO | IMAGE_MONO_ALPHA | IMAGE_GRAY | IMAGE_GRAY_ALPHA
        width: Image width in pixels
        height: Image height in pixels
        data: Raw pixel buffer (read-only)

    Example:
        # Create 32x32 mono image
        img_data = b'\x00\x1F...'  # 32x32//8 = 128 bytes
        mono_img = image(IMAGE_MONO, 32, 32, img_data)
    """

    def __init__(self, profile: int, color_count: int, width: int, height: int, 
                stride: int, 
                data: BufferLike, palette: BufferLike):
        """Constructs an image from pixel data and palette information.
        
        Args:
            - profile: Image format constant (IMAGE_MONO, IMAGE_GRAY_ALPHA, etc.)
            - width: Image width in pixels
            - height: Image height in pixels
            - stride: Bytes per row (typically width * bpp // 8)
            - color_count: Number of colors in palette
            - data: Raw pixel data in packed format (32 pixels per 4-byte word)
            - palette: Color palette data (format depends on profile)
            
        Example:
        ```py
        # Create 79x12 MONO image with explicit stride

        img_data = b'\x00\x1F...' 
        palette_data = b'\xFF\xCF...'
        mono_img = image(IMAGE_MONO, 79, 12, 16, 2, img_data, palette_data)
            
        # Create 16x64 GRAY image with automatic stride
        gray_img = image(IMAGE_GRAY, 16, 64, 32, 4, gray_data, gray_palette)
        ```

        Generate:
        ```bash
        fxconv --bopti-image cg_image_puzzle.png -o puzzle.py --cg profile:p4_rgb565 name:puzzle 
        ```

        The option `--py-compact` is recommended to reduce code size
        """
        ...

    format: int      # IMAGE_* constant
    flags: int
    color_count: int
    width: int
    height: int
    stride: int
    data: BufferLike        # Buffer-like
    palette: BufferLike     # Buffer-like


# --- from gint/keyboard.h ---

# Reading keyboard events in real time
    
def clearevents() -> None: 
    """
    Clear all pending keyboard events from the event queue.
    
    Reads and discards all events currently in the keyboard buffer.
    Useful when you want to check the immediate keyboard state with
    functions like `keydown()` without historical events interfering.
    
    Equivalent to:
    while pollevent().type != KEYEV_NONE: pass
    """
    ...
def pollevent() -> KeyEvent:
    """
    Retrieve the oldest unread keyboard event from the queue.
    
    Returns:
        KeyEvent: 
        - Contains event details if available
        - Returns a dummy event with type=KEYEV_NONE if queue is empty
    
    This function is non-blocking and should be used in loops to
    process all pending events efficiently.
    
    Example:
        # Process all queued events
        while True:
            ev = pollevent()
            if ev.type == KEYEV_NONE:
                break
            # Handle event
    """
    ...

# Reading the immediate state of the keyboard

def keydown(key: int) -> bool:
    """
    Check if a specific key is currently pressed.
    
    Args:
        key: KEY_* constant to check
    Returns:
        True if pressed, False otherwise
    Note:
        Requires prior event reading (clearevents()/pollevent())
    Example:
        if keydown(KEY_LEFT): move_left()
    """
    ...
def keydown_all(keys: List[int]) -> bool:
    """
    Check if ALL specified keys are pressed.
    
    Args:
        keys: One or more KEY_* constants
    Example:
        if keydown_all(KEY_SHIFT, KEY_ALPHA): print("Both pressed")
    """
    ...
def keydown_any(keys: List[int]) -> bool:
    """
    Check if ANY specified key is pressed.
    
    Args:
        keys: One or more KEY_* constants
    Example:
        if keydown_any(KEY_UP, KEY_DOWN): handle_movement()
    """
    ...

# Quickly querying key state changes

def cleareventflips() -> None: 
    """
    Reset press/release tracking state.
    
    Clears all remembered key transitions. Call before checking new
    presses/releases with keypressed()/keyreleased().
    Example:
        cleareventflips()  # Do this at start of each game frame
    """
    ...
def keypressed(key: int) -> bool:
    """
    Check if key was pressed since last cleareventflips().
    
    Args:
        key: KEY_* constant to check
    Returns:
        True if key transitioned from released to pressed
    Example:
        if keypressed(KEY_SHIFT): start_sprint()
    """
    ...
def keyreleased(key: int) -> bool:
    """
    Check if key was released since last cleareventflips().
    
    Args:
        key: KEY_* constant to check
    Returns:
        True if key transitioned from pressed to released
    Example:
        if keyreleased(KEY_JUMP): end_jump_animation()
    """
    ...

# Waiting for a key press

def getkey() -> KeyEvent:
    """
    Wait for a key press or repeat, returning the event.
    
    Blocks until:
    - Key pressed (KEYEV_DOWN)
    - Key repeated (KEYEV_HOLD for arrows after 400ms+40ms)
    - System action (MENU/power-off exits program)
    
    Returns:
        KeyEvent with shift/alpha modifiers if used
    
    Example:
        >>> ev = getkey()
        >>> if ev.key == KEY_EXE: validate()
    """
    ...
def getkey_opt(options: GETKEY_Option, timeout_ms: int | None) -> KeyEvent:
    """
    Configurable version of getkey() with timeout.
    
    Args:
        options: GETKEY_* flags combined with | 
        timeout_ms: Max wait (None=forever)
    
    Returns:
        KeyEvent or KEYEV_NONE if timeout
    
    Example:
        # Get key with 2s timeout
        ev = getkey_opt(GETKEY_MOD_SHIFT, 2000)
    """
    ...

# Miscellaneous keyboard functions

def keycode_function(keycode: int) -> int: 
    """
    Get the F-key number associated with a key code.
    
    Args:
        key: Key code constant (e.g. KEY_F1, KEY_F2)
    
    Returns:
        int: F-key number (1 for KEY_F1, 2 for KEY_F2, etc.) 
             or -1 if not an F-key
             
    Example:
        >>> keycode_function(KEY_F1)
        1
        >>> keycode_function(KEY_UP)
        -1
    """
    ...
def keycode_digit(keycode: int) -> int:
    """
    Get the digit value associated with a numeric key code.
    
    Args:
        key: Key code constant (e.g. KEY_0, KEY_1)
    
    Returns:
        int: Digit value (0 for KEY_0, 1 for KEY_1, etc.)
             or -1 if not a digit key
             
    Example:
        >>> keycode_digit(KEY_5)
        5
        >>> keycode_digit(KEY_EXE)
        -1
    """
    ...

# --- from gint/display.h ---
def __init__() -> None: ...
def C_RGB(r: int, g: int, b: int) -> int:
    """
    Create color from RGB components (0-31 each).
    
    
    Example:
        red = C_RGB(31, 0, 0)
    """
    ...

# Basic rendering functions

def dclear(color: int) -> None:
    """
    Fill screen with color. 
    
    Example:
        dclear(C_WHITE)  # Clear to white
    """
    ...
def dupdate() -> None:
    """
    Update display with VRAM changes.
    
    Call after drawing and before print() statements.
    
    Example:
        dupdate()  # Show drawn frame
    """
    ...
def dpixel(x: int, y: int, color: int) -> None:
    """
    Draw pixel at (x,y). 
    
    Coordinates: 0 ≤ x < DWIDTH, 0 ≤ y < DHEIGHT
    
    Example:
        dpixel(10, 20, C_BLACK)  # Black pixel
    """
    ...
def dgetpixel(x: int, y: int) -> Any:
    """
    Get pixel color from VRAM (not display).
    
    Returns:
        int: Color value or -1 if out of bounds
    """
    ...

def dwindow_get() -> Tuple[int, int, int, int]:
    """Get the current rendering window clipping rectangle.
    
    Returns:
        Tuple[int, int, int, int]: (left, top, right, bottom)
    """
    ...

def dwindow_set(left: int, top: int, right: int, bottom: int) -> None:
    """Set the rendering window to clip drawing operations.
    
    Rendering will be limited to the rectangle from (left, top) included
    to (right, bottom) excluded.
    
    Example:
        # Clip to a 100x50 box at (10, 20)
        gint.dwindow_set(10, 20, 110, 70)
        # ... draw clipped content ...
        # Restore full window
        gint.dwindow_set(0, 0, gint.DWIDTH, gint.DHEIGHT)
    """
    ...

# Geometric shape rendering functions

def drect(x1: int, y1: int, x2: int, y2: int, color: int) -> None:
    """
    Draw rectangle between (x1,y1) and (x2,y2) (inclusive).
    
    Coordinates can be in any order.
    
    Example:
        drect(10, 20, 30, 40, C_BLACK)
    """
    ...
def drect_border(x1: int, y1: int, x2: int, y2: int, fill_color: int, border_width: int, border_color: int) -> None:
    """
    Draw rectangle with inner border.

    Border is drawn inside the rectangle bounds.

    Example:
        drect_border(10,10,50,50, C_WHITE, 2, C_BLACK)
    """
    ...
def dline(x1: int, y1: int, x2: int, y2: int, color: int) -> None:
    """
    Draw straight line between two points.
    
    Example:
        dline(0,0, DWIDTH-1, DHEIGHT-1, C_RED)
    """
    ...
def dhline(y: int, color: int) -> None:
    """
    Draw horizontal line across entire screen at y.
    
    Example:
        dhline(DHEIGHT//2, C_BLUE)  # Center line
    """
    ...
def dvline(x: int, color: int) -> None:
    """
    Draw vertical line across entire screen at x.
    
    Example:
        dvline(DWIDTH//2, C_GREEN)  # Center line
    """
    ...
def dcircle(x: int, y: int, r: int, fill: int, border: int) -> None:
    """
    Draw circle with center (x,y) and radius r.
    Use C_NONE for transparent fill/border.
    
    Example:
        dcircle(100, 100, 20, C_RED, C_NONE)
    """
    ...
def dellipse(x1: int, y1: int, x2: int, y2: int, fill: int, border: int) -> None:
    """
    Draw ellipse fitting bounding box (x1,y1)-(x2,y2).
    
    Example:
        dellipse(90,90,110,110, C_BLUE, C_WHITE)
    """
    ...

def dpoly(vertices: list[int], fill: int, border: int) -> Any:
    """Draw a polygon with specified fill and border colors.
    
    Args:
        vertices: Flat list of (x,y) coordinate pairs defining the polygon.
                  Example: [x0,y0, x1,y1, ..., xn,yn]
        fill_color: Fill color (use C_NONE for transparent interior)
        border_color: Border color (use C_NONE for no border)

    Example:
        # Draw red quadrilateral with blue border
        dpoly([0,0, 100,0, 100,50, 0,50], C_RED, C_BLUE)
        
        # Draw unclosed black border triangle (automatically closed)
        dpoly([50,50, 100,100, 150,50], C_NONE, C_BLACK)
    """
    ...

def dsize(text: str, font: Optional["GintFont"]) -> Tuple[int, int]:
    """Get the width and height of rendered text.
    
    Computes the size the string would occupy if rendered.
    
    Args:
        text: The string to measure.
        font: The font to use. If None, the current default font is used.
        
    Returns:
        Tuple[int, int]: (width, height) in pixels.
        
    Example:
        tw, th = gint.dsize("Hello World", my_font)
    """
    ...

def dnsize(text: str, size: int, font: Optional["GintFont"]) -> Tuple[int, int]:
    """Get the width and height of a prefix of a rendered text.
    
    Similar to dsize(), but stops after 'size' bytes of the input string.
    If 'size' is negative, it's identical to dsize().
    
    Args:
        text: The string to measure.
        size: The maximum number of bytes to read from the string.
        font: The font to use. If None, the current default font is used.
        
    Returns:
        Tuple[int, int]: (width, height) in pixels.
    """
    ...

def drsize(text: str, font: Optional["GintFont"], width: int) -> Tuple[int, int]:
    """Determine how many characters fit in a given width.
    
    Calculates the portion of the string that fits within the specified
    pixel width.
    
    Args:
        text: The string to measure.
        font: The font to use. If None, the current default font is used.
        width: The maximum width in pixels.
        
    Returns:
        Tuple[int, int]: (byte_offset, actual_width)
            - byte_offset: The number of bytes from the start of the string
              to the last visible character.
            - actual_width: The pixel width actually used by that part of the string.
            
    Note:
        The returned byte_offset is not reliable for slicing strings that
        contain multi-byte Unicode characters. Slicing with `str[:offset]`
        may fail. This is a known issue.
    """
    ...

def dtext_opt(x: int, y: int, fg: int, bg: int, halign: int, valign: int, text: str, size: int) -> None:
    """Draw text with advanced positioning and background.
    
    Args:
        x: Reference X position
        y: Reference Y position
        fg: Text color
        bg: Background color (use C_NONE for transparent)
        halign: Horizontal alignment (DTEXT_LEFT/CENTER/RIGHT)
        valign: Vertical alignment (DTEXT_TOP/CENTER/BOTTOM)
        text: String to display
        size: Maximum width for wrapping (-1 = no wrap)
    
    Example:
        # Centered title with background
        dtext_opt(DWIDTH//2, 15, C_WHITE, C_BLUE,
                 DTEXT_CENTER, DTEXT_BOTTOM,
                 "Main Menu", -1)
    """
    ...
def dtext(x: int, y: int, fg: int, text: str) -> None:
    """Draw text at specified coordinates with foreground color.
    
    Args:
        x: Left starting position (pixels)
        y: Top starting position (pixels)
        fg: Text color (C_* constant)
        text: String to display
    
    Example:
        dtext(10, 20, C_BLACK, "Score: 100")
    """
    ...



def image_rgb565(width: int, height: int, data: BufferLike) -> image: ...
def image_rgb565a(width: int, height: int, data: BufferLike) -> image: ...
def image_p8_rgb565(width: int, height: int, data: BufferLike, palette: BufferLike) -> image: ...
def image_p8_rgb565a(width: int, height: int, data: BufferLike, palette: BufferLike) -> image: ...
def image_p4_rgb565(width: int, height: int, data: BufferLike, palette: BufferLike) -> image: ...
def image_p4_rgb565a(width: int, height: int, data: BufferLike, palette: BufferLike) -> image: ...


def dimage(x: int, y: int, img: image) -> None:
    """Draw an entire image at specified coordinates.
    
    Args:
        x: Left position (0 = screen left)
        y: Top position (0 = screen top)
        img: Image to draw (mono/gray profile)
    
    Example:
        dimage(50, 20, logo_img)  # Draw logo at (50,20)
    """
    ...
def dsubimage(x: int, y: int, img: image, left: int, top: int, width: int, height: int) -> None:
    """Draw a subregion of an image.
    
    Args:
        x: Destination left position
        y: Destination top position
        img: Source image
        left: Subregion left (pixels)
        top: Subregion top (pixels)
        width: Subregion width
        height: Subregion height
    
    Example:
        # Draw 16x16 tile from sprite sheet
        dsubimage(100, 50, sprites, 32, 0, 16, 16)
    """
    ...

# --- Constants ---
I: int
KEY_F1: int
KEY_F2: int
KEY_F3: int
KEY_F4: int
KEY_F5: int
KEY_F6: int
KEY_SHIFT: int
KEY_OPTN: int
KEY_VARS: int
KEY_MENU: int
KEY_LEFT: int
KEY_UP: int
KEY_ALPHA: int
KEY_SQUARE: int
KEY_POWER: int
KEY_EXIT: int
KEY_DOWN: int
KEY_RIGHT: int
KEY_XOT: int
KEY_LOG: int
KEY_LN: int
KEY_SIN: int
KEY_COS: int
KEY_TAN: int
KEY_FRAC: int
KEY_FD: int
KEY_LEFTP: int
KEY_RIGHTP: int
KEY_COMMA: int
KEY_ARROW: int
KEY_7: int
KEY_8: int
KEY_9: int
KEY_DEL: int
KEY_4: int
KEY_5: int
KEY_6: int
KEY_MUL: int
KEY_DIV: int
KEY_1: int
KEY_2: int
KEY_3: int
KEY_ADD: int
KEY_SUB: int
KEY_0: int
KEY_DOT: int
KEY_EXP: int
KEY_NEG: int
KEY_EXE: int
KEY_ACON: int
KEY_HELP: int
KEY_LIGHT: int
KEY_X2: int
KEY_CARET: int
KEY_SWITCH: int
KEY_LEFTPAR: int
KEY_RIGHTPAR: int
KEY_STORE: int
KEY_TIMES: int
KEY_PLUS: int
KEY_MINUS: int
KEY_KBD: int
KEY_EQUALS: int
KEYEV_NONE: int
KEYEV_DOWN: int
KEYEV_UP: int
KEYEV_HOLD: int
KEYEV_TOUCH_DOWN: int
KEYEV_TOUCH_UP: int
KEYEV_TOUCH_DRAG: int

GETKEY_MOD_SHIFT: int
GETKEY_MOD_ALPHA: int
GETKEY_BACKLIGHT: int
GETKEY_MENU: int
GETKEY_REP_ARROWS: int
GETKEY_REP_ALL: int
GETKEY_REP_PROFILE: int
GETKEY_FEATURES: int
GETKEY_NONE: int
GETKEY_DEFAULT: int

GETKEY_Option = Union[
    type(GETKEY_MOD_SHIFT),
    type(GETKEY_MOD_ALPHA),
    type(GETKEY_BACKLIGHT),
    type(GETKEY_MENU),
    type(GETKEY_REP_ARROWS),
    type(GETKEY_REP_ALL),
    type(GETKEY_REP_PROFILE),
    type(GETKEY_FEATURES),
    type(GETKEY_NONE),
    type(GETKEY_DEFAULT)
]

DWIDTH: int   # 320 (classpad) - others: 128 (b/w) or 396 (color) or 
DHEIGHT: int  # 528 (classpad) - others: 64 (b/w) or 224 (color)

DTEXT_LEFT: int
DTEXT_CENTER: int
DTEXT_RIGHT: int
DTEXT_TOP: int
DTEXT_MIDDLE: int
DTEXT_BOTTOM: int

C_WHITE: int
C_LIGHT: int
C_DARK: int
C_BLACK: int
C_INVERT: int
C_NONE: int
C_LIGHTEN: int
C_DARKEN: int
C_RED: int
C_GREEN: int
C_BLUE: int

IMAGE_MONO: int
IMAGE_MONO_ALPHA: int
IMAGE_GRAY: int
IMAGE_GRAY_ALPHA: int
IMAGE_RGB565: int
IMAGE_RGB565A: int
IMAGE_P8_RGB565: int
IMAGE_P8_RGB565A: int
IMAGE_P4_RGB565: int
IMAGE_P4_RGB565A: int
IMAGE_FLAGS_DATA_RO: int
IMAGE_FLAGS_PALETTE_RO: int
IMAGE_FLAGS_DATA_ALLOC: int
IMAGE_FLAGS_PALETTE_ALLOC: int

# Custom fonts

def font(
    prop: int,
    line_height: int,
    data_height: int,
    block_count: int,
    glyph_count: int,
    char_spacing: int,
    line_distance: int,
    blocks: bytes,
    data: bytes,
    # Monospaced fonts
    width: int,
    storage_size: int,
    # Proportional fonts
    glyph_index: bytes,
    glyph_width: bytes
) -> GintFont: ...

class GintFont:
    prop: int
    line_height: int
    data_height: int
    block_count: int
    glyph_count: int
    char_spacing: int
    line_distance: int
    blocks: bytes
    data: bytes
    width: int
    storage_size: int
    glyph_index: bytes
    glyph_width: bytes
