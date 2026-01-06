import gint

# Simple logo (monochrome, black on white)
DVD = [
    "                       ",
    "   ####    ####        ",
    "  #       #    #       ",
    "  #       #    #       ",
    "  #       ######   ### ",
    "  #       #            ",
    "  #       #            ",
    "   ###    #            ",
    "                       ",
    "  ####   #####  #   #  ",
    "  #   #  #      #   #  ",
    "  #   #  #      #   #  ",
    "  #   #  #####  #   #  ",
    "  #   #  #       # #   ",
    "  #   #  #       # #   ",
    "  ####   #####    #    ",
]

DVD_W = 23
DVD_H = 16

# Draw the logo at (x, y)
def draw_logo(x, y, color=gint.C_BLACK, bg=gint.C_WHITE):
    for dy in range(DVD_H):
        for dx in range(DVD_W):
            if 0 <= x+dx < gint.DWIDTH and 0 <= y+dy < gint.DHEIGHT:
                pixel = DVD[dy][dx]
                gint.dpixel(x+dx, y+dy, color if pixel == '#' else bg)

# Initial position and speed
x, y = 50, 50
dx, dy = 2, 2

# Colors for visual fun
bg = gint.C_WHITE
fg = gint.C_BLACK



while True:
    gint.dclear(bg)
    draw_logo(x, y, fg, bg)
    gint.dupdate()

    # Move
    x += dx
    y += dy

    # Bounce
    if x <= 0 or x + DVD_W >= gint.DWIDTH:
        dx = -dx
    if y <= 0 or y + DVD_H >= gint.DHEIGHT:
        dy = -dy

    # Exit if any key pressed
    ev = gint.pollevent()
    if ev.type == gint.KEYEV_DOWN and ev.key == gint.KEY_EXIT:
        break
