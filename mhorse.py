# Enclose the Horse
from gint import *
import sys

# 1. Configuration & Colors

COL_BACKGROUND   = C_RGB(4, 14, 8)
COL_GRASS        = C_RGB(4, 14, 8)
COL_GRASS_DETAIL = C_RGB(6, 16, 10)
COL_WATER        = C_RGB(1, 7, 10)
COL_WATER_BORDER = C_RGB(5, 10, 13) 
COL_WALL         = C_RGB(12, 24, 12)
COL_HORSE        = C_WHITE
COL_ENCLOSED     = C_RGB(31, 55, 0)
COL_TEXT         = C_WHITE
COL_ALERT        = C_RGB(31, 5, 5)
COL_UI_BG        = C_RGB(2, 8, 4)
COL_BTN_BG       = C_RGB(6, 12, 6)
COL_MODAL_BG     = C_WHITE
COL_MODAL_TEXT   = C_BLACK

# 2. Level Data

LEVELS = [
    {"id": "E03KkY", "day": 1, "opt": 68, "budget": 10, "map": "~~~~....~~~~.~~~~~~\n~~~~...~~~~..~~~~~~\n..~.~...~~~..~..~~~\n~.........~......~~\n~............~~....\n....~~~.~..~~~~....\n~..~~~~....~~......\n....~~~..H......~..\n....~~~....~~.....~\n.~~........~~~~...~\n.~~...~~...~~~~...~\n....~~~...........~\n~..~~~...~~......~~\n..~~....~~~......~~\n.~~~...~~~~...~..~~"},
    {"id": "Kj7mXp", "day": 2, "opt": 90, "budget": 14, "map": "..~~~.~.........~\n..~.~...~~~~.~~..\n~.~~~...~~~~.~~..\n........~~~~....~\n........~~~.....~\n~~~~............~\n~~~~.~~..........\n~~~~.~~..~~~.....\n~~~~.....~~~..~~.\n.........~~~..~~.\n....~~~..........\n~~..~~~.~.H......\n~~..~~~.......~.~\n.................\n~..~~..~~~.~.~~~~\n...~~..~.~...~~~~\n~......~~~...~~~~"},
    {"id": "Qn9vLs", "day": 3, "opt": 74, "budget": 11, "map": "..~~...~~~~......~~\n.~~~~..~~~....~~~~~\n~~~~~..~~~~..~~~~~.\n~~~~~..~~~~..~~~~~.\n~~~~~...~~...~~~~..\n...................\n.~.......H.~......~\n...................\n..~.~~~.~.~.~.~.~..\n....~...~.~.~.~.~..\n..~.~.~.~.~.~.~....\n..~.~...~.~.~.~~~..\n..~.~~~.~...~...~..\n..~...~.~.~.~.~.~.~\n..~.~.~.~.~.....~..\n~.~.~...~.~.~.~~~..\n..~.~.~...~.~......\n....~.~.~.~.~.~.~..\n..~.~...~.~.~.~.~.."},
    {"id": "tnLvlG", "day": 4, "opt": 51, "budget": 8, "map": ".................\n.~..~~~~...~~~~~.\n.~..~~~....~~~~~.\n.~...~~....~~~~~.\n.~...~~..~~~~~...\n.~...~~~.~.......\n.~....~~.~.......\n.~~~~........~~~.\n.~~~~~~...~~~~~~.\n.~...~~...~......\n........H........\n......~...~...~~.\n.~~~~~~...~~~~~~.\n.~~..~.........~.\n.~.....~~~~....~.\n.~~....~~~~......\n.~~~...~~~~......\n........~~~......\n.~~~..~.....~..~.\n.~~~..~~~~~~~..~.\n................."},
    {"id": "CNtGPI", "day": 5, "opt": 116, "budget": 12, "map": ".~~......~.........\n.~~..~..~~.......~.\n....~~..~~..~...~~.\n.~..~~.....~~...~~.\n~~.......H.~~......\n~~.....~......~....\n...~..~~..~..~~....\n..~~..~~.~~..~~..~.\n..~~.....~~.....~~.\n................~~.\n...................\n.~~~~~~~~..........\n.~......~..~~.~~..~\n.~.~~~~.~..~~.~~.~~\n.~.~..~.~..~..~..~~\n.~.~.~~.~..~..~....\n.~.~....~.~~.~~.~..\n.~.~~~~~~..........\n.~.................\n~~~~~~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~~~~~~"},
    {"id": "VfWi_1", "day": 6, "opt": 77, "budget": 11, "map": "~~....~~...~~~~~~~~\n~~....~~~~.~~~~~..~\n~~~...~....~~~~~~~~\n~.~...~~~.....~~~~~\n~~~....~~~~....~~~~\n~~...~...~~~.......\n.....~........~....\n...........~~......\n~~.~~..~...~~..~.~~\n~~.~~~......~....~~\n~~..~~.........~.~~\n~~...~.~~~~..H.....\n~~~....~~~....~..~~\n~.~..~...........~~\n~~~~............~~~\n~~~~~....~~....~~~~\n~~~~~~........~~~.~\n~~~~.~.~..~~..~~~~~\n~~~~~~.~..~~..~~~~~"},
    {"id": "6UV4Yw", "day": 7, "opt": 95, "budget": 13, "map": "~....~~...~~~~..~~~\n~....~~~.........~~\n~~....~~~.~~..~~...\n~~~.~...~.~~.......\n~~~...............~\n~~.....~~~~........\n~~.~~..~...........\n~~.~~..~~~.......~~\n...~~...........~~.\n...~~..........~~..\n~...~..~~..~~.~~~.~\n~~~...~.~.~.~.~~..~\n~~~...~~~.~~~......\n.~~...H.......~...~\n....~~~~..~.......~\n....~~~~....~~~~...\n.~~..~~~.~~.~~~~~.~\n~~~~.~~..~~.~~~~~.~\n~~~.........~~~~~.~\n........~~~..~~~~.~\n..~~.~~~~~~~.~~~..~\n~~~~..~~~~~......~~\n~~~~...~~~~.~~~.~~~"},
    {"id": "FswXDo", "day": 8, "opt": 86, "budget": 11, "map": "~~~~~~..~..~~~~~~\n~~~~~.....~..~~~~\n~~~~..~.~...~.~~~\n~~~.......~....~~\n~~~..~.~~......~~\n.......~~....~...\n~~..~.....~~...~~\n~~........~~...~~\n...~..~~.......~~\n......~~..~..~.~~\n~~......H....~.~~\n~~....~..~...~...\n~~..~...~..~...~~\n.....~....~..~.~~\n...~.~.~..~.~~.~~\n~~...........~.~~\n~~.....~.~.....~~\n~~.~~~.....~~~.~~\n~~.~~~~...~~~~C~~\n~~...~~~.~~~...~~"},
    {"id": "ZtiI9g", "day": 9, "opt": 66, "budget": 12, "map": "~~..~~~.~~~~\n~C.C.......~\n..C......~..\n.C.C~~..~~.~\n~.~.~~.....~\n~..........~\n....~.~~...~\n~...~~H~....\n~...........\n~.....~~...~\n..~~..~~C.C~\n~.~......C.~\n~.......C.C~\n~.~~.~.~...~"},
    {"id": "xPt_fu", "day": 10, "opt": 73, "budget": 10, "map": "~~~~~~.~...~~~~~~~~\n~~~~~~.......~~~~~~\n~~~~...~~.~....~~~~\n~~~..~~~~.~.~~..~~~\n~~..~~~~~........~~\n~~.....H....~~.~.~~\n...~~~.~~...~~.~...\n~..~~~.~~.........~\n~............~~~.~~\n~...~~~~....~~~~...\n....~~.....~~~....~\n~~.....~...~~..~~.~\n....~~.~......~~...\n~~..~~.~.....~~~.~~\n~~..........~~~..~~\n~~~~.~~~....~~..~~~\n~~~~...~~......~~~~\n~~~~~~.......~~~~~~\n~~~~~~~.~.~~.~~~~~~"},
    {"id": "ZWuYxG", "day": 11, "opt": 103, "budget": 13, "map": "~~~~~~~~~...~...~~~~~\n~~~~~~~~~........~~~~\n~~~~~~~~~.........~~~\n~~~~~~~~.....~~~~..~~\n~~~~~~~.....~~~~~~..~\n~~~~........~~~~~~...\n............~~~~~~...\n............~~~~~~...\n....~~~~.....~~~~...~\n...~~~~~~...........~\n~..~~~~~~.H..........\n~..~~~~~~............\n~~.~~~~~~............\n~~..~~~~........~~~..\n~~........~~...~~~~~.\n~........~~~~..~~~~~.\n~........~~~~..~~~~~.\n...~~~~~..~~....~~~..\n..~~~~~~~............\n.~~~~~~~~~.....~~~~..\n.~~~~~~~~~....~~~~~~."},
    {"id": "x6q-c6", "day": 12, "opt": 94, "budget": 10, "map": "~.~~.~~~~..~.~~\n~......~......~\n~...~~.~..~...~\n~......~.~~~..~\n..~~...~..~....\n~......~......~\n~......~....~..\n...~~..~...~~~.\n~......~....~.~\n~.........~...~\n....~~.~.~~~...\n.~~....~..~...~\n.......~......~\n~...0..~..0.H.~\n~......~......~\n~......~......~\n~~.~~~~~~~~~.~~"},
    {"id": "-fR-Iq", "day": 13, "opt": 54, "budget": 10, "map": "~~~...~~.~~.~~~\n~.....~..~~..~~\n..~~~.........~\n..~~0.~~~..~...\n~.~~~..~~H~~..~\n~.~~C..~..~~...\n~.............~\n~..~~~.......~~\n~.~~~~..~2~..~~\n...~~1..~~~..~~\n.........~~~..~\n...............\n~~~~~~~~~~~~~~~\n~~~~01~~~2~~~~~"},
    {"id": "xKrORQ", "day": 14, "opt": 0, "budget": 12, "map": "~~~~~~~~~~~~~~~~~~~\n~CCC0~CC~C~~~~~~...\n~CCC~~CC~C~~~~~...~\n~CCC~1CC~C2~~....~~\n~~~~~~~~~~~~...2.~~\n~.......~....~...~~\n...~~~~.....~~....~\n..~~~~~...~~~~~....\n~.~~~~....~~~~.....\n~.~~~......~~~..~..\n~...~.....H....~~~.\n~..............~~~~\n...1..~~....~..~~~~\n~....~~~~..~~~..~~.\n~~.~~~~~~..~~~.....\n~~..~~~~~..~~......\n............0.....~\n~~.......~~......~~\n~~~~..~.~~~~~~...~~"},
    {"id": "JSOiHt", "day": 15, "opt": 0, "budget": 10, "map": "~~~.~~.~~.~~~~~~.~~\n~....~.~...~.......\n...C.~.~.C...C.~...\n~~...~.~...~...~..~\n~...~..~~.~~.~~~..~\n~~.~.............~~\n.......~...~......~\n~~~.~.~~~.~~~.~~.~~\n....~..~...~..~...~\n..C......H......C..\n~...~..~...~..~....\n~~~~~.~~~.~~~.~~...\n~......~...~......~\n...~~........~~.~~~\n~...~~.~~.~~.~.....\n~.C..~.~...~.~..C.~\n~....~.~.C.~.~~...~\n~....~.~...~....~.~\n~~~.~~.~~.~~.~~~~~~"},
    {"id": "ar8agB", "day": 16, "opt": 0, "budget": 11, "map": "~....~~..~.~.~~~.~~\n~~...~~..~...~.~...\n~.~......~~~.~~~.~~\n~~~............~.~~\n~~.~~~..~~~.~.....~\n~~~~~...~~~.~~~~~.~\n~...~.~......~..~..\n~~....~~.~~..~..~.~\n...~..~C.~~..~.~~.~\n~..~~.~..~.~.~~~..~\n~..~~.~~.~~~.....~~\n.......~......H.~~~\n...~.....~~~~..~~.~\n~.~~~~~...~.~~.....\n......~~~..~~~...~.\n~.~.~.~.~~.~...~~~~\n~.~.~.~.~..~~~....~\n~.~.........~..~~.~\n~~~~~.~~~.~~~...~~~"},
    {"id": "IePe4X", "day": 17, "opt": 0, "budget": 11, "map": ".~..~~~..~~~~......~...\n.~...~~..~~~.......~...\n.~.~..~........~~..~...\n.~~~..........~~~~.~...\n.~~~........~~~~~..~...\n.~~...~~....~~~....~...\n.~~...~~~..........~~..\n.~....~~~..~~~~......~.\n...2...~~...~~~~~..~.4.\n.~........~H..~~~~.~~.~\n........1.~~....~~.~.3~\n.~~.~~~~..~~.......~.~.\n.~........~~~...0....2.\n.~.4.5.~...~~~.....~...\n.~.....~~~~~~~.....~.1~\n.~~~~~~~~~~~~~~~~~~~~..\n.~5CCCCCCCCCCCCCCC3~.0.\n.~~~~~~~~~~~~~~~~~~~.~.\n~~~~~~~~~~~~~~~~~~~~~~~"},
    {"id": "YWoKSG", "day": 18, "opt": 0, "budget": 11, "map": "~~~~~~.~..~..~..~~~\n~~~~~~...........~~\n~~~~~....~..~...0.~\n~~~~..~....~~~.....\n~~........~~C~~...~\n....~..~.~~...~~...\n..~...~~~.~.0.~...~\n~....~~C~~~...~.~..\n....~~~.~~~~..~....\n.....~....~...~..~.\n.~...~....~...~..~.\n.~.....H......~..~.\n.~.~......~...~..~.\n~~~~~~~~~~~~~~~~~~~"},
    {"id": "Umm-qf", "day": 19, "opt": 0, "budget": 10, "map": "~.~.~~.~~.~...~\n~~~.~.....~~..~\n~.....~~~.....~\n~.~~~.~1~.~~~.~\n..~.........~.~\n~~~.~~.~~~~.~.~\n....~.....~....\n.~~...~H~.~.~~.\n.1~.~.~~~...~0.\n.~~.......~.~~.\n....~~~..~~....\n~~~.........~..\n..~.~.~0~.~.~..\n~...~.~~~.....~\n~~..~...~~..~~~"},
    {"id": "6GP657", "day": 20, "opt": 0, "budget": 10, "map": "~~~~~~~~~~~~~~~~~~~\n~CCC0~CC~C~~~~~~...\n~CCC~~CC~C~~~~~...~\n~CCC~1CC~C2~~....~~\n~~~~~~~~~~~~...2.~~\n~.......~....~...~~\n...~~~~.....~~....~\n..~~~~~...~~~~~....\n~.~~~~....~~~~.....\n~.~~~......~~~..~..\n~...~.....H....~~~.\n~..............~~~~\n...1..~~....~..~~~~\n~....~~~~..~~~..~~.\n~~.~~~~~~..~~~.....\n~~..~~~~~..~~......\n............0.....~\n~~.......~~......~~\n~~~~..~.~~~~~~...~~"},
    {"id": "gl7REy", "day": 21, "opt": 0, "budget": 9, "map": "~~.~~~~.....~\n~~.......~~..\n~...~~~~.~~.~\n..~.........~\n~.~~.~~~.~..~\n~........~..~\n~~.~.~H~.~.~~\n.....~~~...~~\n.~~......~...\n..~..~~~....~\n~.~..~...~~.~\n~....~.~~~~.~\n~...........~\n..~~~......~~\n.~~~~.~..~~~~"},
    {"id": "B6gH2w", "day": 22, "opt": 0, "budget": 10, "map": "~~.~.~~.~~~.~\n~0.~.~~~~1CC.\n.C~~..~.~.~~~\n~C..~...~.~..\n~~~..........\n.~.........~~\n.~.C~.C~....~\n...~~.~~...~~\n~~...H.......\n...~.~.~...~.\n~..~0~1~...~~\n~~.........~~\n.~.........~.\n....~.~.~.~~.\n~~.~...~~~.~~\n~~.~.~.~.~~~~"},
    {"id": "I5gIup", "day": 23, "opt": 0, "budget": 10, "map": "...~~~~~.S.~.\n~............\n~~..~~~~~..~.\n~~~.~SSS~.~~.\n~...~SSS~.~~~\n~S..~~.~~..~~\n.............\n.~~..H...~~.S\n~~~....~~~~.~\n~...~~.~~....\n.S.~~~....~~.\n....~~...~~~.\n~..~~~....~~.\n~~~~......S..\n~S~..S.~~~~~~"},
    {"id": "fKUrV1", "day": 24, "opt": 0, "budget": 9, "map": "~~~~.~~.~~~.~\n~.~..........\n~.~.~~~~..~..\n~2..........~\n~~~~~~~~~.~~~\n~2~..........\n..~...~~~...~\n~1........~..\n~~~~~~~~~~~.~\n~1~..........\n~.~.H..~...~.\n~0....~~.~...\n~~~~~~~~~~~~~\n~0~........~.\n~.~.~...~.G..\n~.....~.~....\n~~~~.~~~~.~.~"},
    {"id": "1XHKfu", "day": 25, "opt": 0, "budget": 11, "map": "~~S~~.~~~.~\n~~....~~~..\n...~~.~S~.~\n~~~~S......\n~~S~~.~C~.~\n.....H.....\n~~~.~.~~.~~\n~SS.~.S~...\n~S~.~.~~S~.\n~.~......~~\n....~.~....\n~~~.~.~.~~~"},
    {"id": "A6HuJY", "day": 26, "opt": 0, "budget": 9, "map": "...~~~~~...~~~~\n~.....~~~~..~~~\n~~~.....~~~....\n.~~~.~~...~.~~.\n.....~~~~...~~~\n~~....~~~~....~\n~~~~...~~~~....\n..~~~....~~~.~.\n~...~~.H..~~.~~\n~~~..~.~~..~.~~\n.......~~~....~\n~~~~~...~~~.C..\n..~~~~~..~~~...\n....~~~~..~~~..\n~~.....~....~~~\n~~~~~....~~...~\n...~~~~.~~~~~.."},
    {"id": "OAoNjv", "day": 27, "opt": 0, "budget": 9, "map": "...............\n.~~.~~~.~~.~~~.\n.~...........~.\n.~..~..~~...~~.\n.~.....~~....~.\n...~.......~~~.\n.~..~.~~~....~.\n.~.0...H~.~~.~.\n.~~~~~~~~......\n.~.......~~..~.\n...~~~.........\n.~.~.~..~~...~.\n.~.~~~.........\n.~.....~~....~.\n.~.0.~.......~.\n~~~~~~~~..~~~~~"},
    {"id": "xrktyY", "day": 28, "opt": 0, "budget": 10, "map": "...........~~~~\n.~~~~~.~~~..~~~\n.~.......~..~~~\n...............\n.~.......~.....\n.~...~~.~~~~.~.\n.....~...~.....\n.~...~.H.~...~.\n.~.......~...~.\n.~~~.~~.~~.....\n.....~.........\n.............~.\n~~.............\n~~~..~~~~.~~.~.\n~~~~..........."},
    {"id": "RAY8n3", "day": 29, "opt": 0, "budget": 10, "map": "~.~~~~~.~~\n~.S1~~0..~\n...~~~..H.\n...~1...~.\n~..~.S..S.\n..0~.~....\n~......S~.\n.....~..~~\n~G~.G~~G~~\n~.~~.~~.~~"},
    {"id": "mhbQDo", "day": 30, "opt": 0, "budget": 10, "map": "~~~~~.~~~~.~~~~\n~~~.....~0..~~~\n~~......0~...~~\n~...~~...~.~..~\n~...~~...~....~\n........~.~.~..\n~.......~.....~\n...~...~....~..\n~.....~...~...~\n......~.~.H.~.~\n..~..~...~~....\n~....~.~.~~...~\n~~...~1......~~\n~~~..1~..~..~~~\n~~~~.~~~....~~~"},
    {"id": "j7xEfA", "day": 31, "opt": 0, "budget": 13, "map": "~~~~~~~~~~~~~~~\n~........0~0GG~\n....S..~..~~GG~\n~.~~...S..~~~~~\n~.~~.~.S.....S~\n~.SS..S.~S.....\n~S..S......~~.~\n~.S~..~~.~.~~.~\n~..S..~~......~\n..S.~S.S..S...~\n~.....S.~.~~..~\n~.S~~S..S.~~..~\n~..~~.~....S~..\n~S.....H......~\n~~~~.~~.~~~.~~~"},
    {"id": "jVLkkX", "day": 32, "opt": 0, "budget": 12, "map": "~~...~...~.~~..~\n.....~..~~.....~\n~.~~....~~~...~~\n~......~~~~~...~\n..~~~....~....~~\n~.~~.........~..\n...~.~..H...~..~\n~~..~~~....~~.~~\n~~..............\n~~.........~~.~~\n.....~....~~....\n.....~...~~~~.~~\n............~.~.\n~.......~~~.....\n~......~.~~~~.~~\n~~............~~\n~~...~~.......~~"},
    {"id": "brDIYY", "day": 33, "opt": 0, "budget": 9, "map": "~.~~~~~..~~~~~\n.............~\n~.~~..~~..~~..\n~.~~..~~..~~.~\n~............~\n~.............\n~.~~..~H..~~..\n..~~..~~..~~.~\n~............~\n~............~\n~.~~..~~..~~.~\n~.~~..~~..~~.~\n~............~\n~~..~.~~~~~~.~"},
    {"id": "XZceoM", "day": 34, "opt": 0, "budget": 10, "map": "~~...~~~...~.\n.....~....~~.\n~......1~~~..\n~~..~~~~~....\n.~..........~\n.~~.~~.~~~..~\n..~.~1...~~.~\n~...~~.H.0~.~\n~~...~~~.~~..\n.~.~.........\n~~.~~.~~~~~.~\n~...~...0...~\n~..~~..~~~..."},
    {"id": "ECT9f-", "day": 35, "opt": 0, "budget": 10, "map": "...............\n.~.~.~...~.~.~.\n.~~.~~...~~.~~.\n.~...~.2.~...~.\n.....~~~.~...~.\n.~...~.2.~.....\n.~...~...~.....\n.~...~.H.....~.\n.~.......~...~.\n.....~...~...~.\n.~..0~0.1~1..~.\n.....~...~...~.\n.~...~...~.....\n.~...~...~...~.\n~~~.~~~~~~~~.~~"},
    {"id": "gkS8-B", "day": 36, "opt": 0, "budget": 10, "map": "~.~~~~.~~~~~.~~\n...~~~.~~~C..~~\n~...~...~~~...~\n~..............\n...~~C....~~~..\n~~.~~~...~~~~.~\n~~.............\n~......H.......\n~...........~~.\n..S.~~~..~~.~~.\n....~~~..~~....\n~~~..~........~\n.~~..~.~~~~...~\n........C~~~.~~\n~~.~.~~~.~~~.~~"},
    {"id": "p_Qh4C", "day": 37, "opt": 0, "budget": 10, "map": "~~~~~~~~~~~~~\n......C..~C.~\n.~~.~.~......\n..C.....C~~..\n...~~....~~..\n~...~.0.....~\n~~~~~~~~~~~~~\n~.~...0.~....\n..~.~.......~\n~.....H..~~..\n...~~.....~.~\n~..~..1......\n~~~~~~~~~~~~~\n~C.~..1.~..C~\n.............\n....~C.~.~~..\n~..~~~...C~..\n........~...~\n~~~~~~~~~~~~~"},
    {"id": "NXN0nq", "day": 38, "opt": 0, "budget": 9, "map": ".................\n..~~.........~~..\n...~.........~...\n..~~.........~~..\n.~~.....~~~...~~.\n~~......~.~....~~\n~...0...~~~.....~\n~...............~\n~..~.~~~.H.~~...~\n~..~~~~.~..~~...~\n~..~~~~~~.......~\n~~.~.~~~..~...1~~\n.~~...........~~.\n.0~~.........~~..\n...~~~~~~~~~~~..1"},
    {"id": "YDEMin", "day": 39, "opt": 0, "budget": 10, "map": "~~~~~..~.~~~~\n~.~.......~.~\n............~\n~.~.......~..\n~.~.~~~.~~~.~\n~.~...~...~.~\n~...G........\n~.~...~...~.~\n~.~~.~~~~~~~~\n~.~...~.....~\n..~.......~..\n~.~...~...~.~\n~.~~.~~.~~~.~\n..~.......~..\n........H.~.~\n~.~.......~.~\n~.~..~~~.~~~~"},
    {"id": "-1ngUe", "day": 40, "opt": 0, "budget": 11, "map": ".~~~..~..~~~~~\n.CCC.~~...~~~~\n.~~.....~.....\n.CC.~~.~~.~~..\n..~..S..~.~~~~\n~C...~~...~~~~\n.~.~SSSS~...~~\n...~~~~~~.....\n.....~~~~.H.~.\n..~~...~......\n..~~~.........\n..~~~~~...~~..\n..~~.~..~~~...\n.....~...~~..."},
    {"id": "qS_Kov", "day": 41, "opt": 0, "budget": 10, "map": "...............\n.~.~~~~..~~~~~.\n.~...~...~...~.\n.~.1.......0.~.\n.~...~...~.....\n.~~..~...~.~~~.\n.......~.....~.\n....~..H...~...\n.~.......~.....\n.~~.~~.....~.~.\n.....~...~...~.\n.~G0....~~.1G~.\n.~...~...~.....\n.~~~~~...~~~~~.\n.......~......."}
]
# 3. Game State

current_level_idx = 0
saves_data = {} 

grid_cols = 0
grid_rows = 0
terrain = []
walls = []
cherries = []
horse_pos = -1
budget = 0

tile_size = 16
grid_offset_x = 0
grid_offset_y = 35

visited_tiles = set()
is_escaped = True
current_score = 0
walls_used = 0

current_modal = None 

# State History for Optimization
prev_walls = []
prev_visited = set()
prev_escaped = True
prev_walls_used = -1
prev_score = -1

# 4. Save/Load

def load_saves():
    global saves_data
    saves_data = {}
    try:
        with open("horse.dat", "r") as f:
            content = f.read()
            if content:
                entries = content.split(';')
                for entry in entries:
                    if ':' in entry:
                        key, val = entry.split(':')
                        try:
                            saves_data[key] = int(val)
                        except:
                            pass
    except OSError:
        pass

def save_game_to_disk():
    try:
        data_str = ""
        for k, v in saves_data.items():
            data_str += "{}:{};".format(k, v)
        with open("horse.dat", "w") as f:
            f.write(data_str)
        return True
    except:
        return False

# 5. Logic Functions

def load_level(idx):
    global grid_cols, grid_rows, terrain, walls, cherries, horse_pos, budget
    global grid_offset_x, visited_tiles, is_escaped, current_score, current_level_idx
    global tile_size, grid_offset_y
    global prev_walls, prev_visited, prev_escaped, prev_walls_used, prev_score
    
    current_level_idx = idx
    lvl = LEVELS[idx]
    budget = lvl['budget']
    
    lines = lvl['map'].strip().split('\n')
    grid_rows = len(lines)
    grid_cols = len(lines[0])
    
    total = grid_rows * grid_cols
    terrain = [0] * total
    walls = [False] * total
    cherries = [False] * total
    
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            i = r * grid_cols + c
            if char == '~': terrain[i] = 1
            elif char == 'H': horse_pos = i
            elif char == 'C': cherries[i] = True
            
    max_w = DWIDTH - 10 
    max_h = DHEIGHT - 80
    w_fit = max_w // grid_cols
    h_fit = max_h // grid_rows
    tile_size = min(16, min(w_fit, h_fit))
    
    gw = grid_cols * tile_size
    grid_offset_x = (DWIDTH - gw) // 2
    grid_offset_y = 35 
    
    visited_tiles = set()
    is_escaped = True
    current_score = 0
    
    # Reset History to force redraw on first frame
    prev_walls = [] 
    prev_visited = set()
    prev_escaped = not is_escaped 
    prev_walls_used = -1
    prev_score = -1
    
    solve_path()

def solve_path():
    global visited_tiles, is_escaped, current_score, walls_used
    
    walls_used = sum(1 for w in walls if w)
    
    queue = [horse_pos]
    visited = {horse_pos}
    escaped = False
    
    head = 0
    while head < len(queue):
        curr = queue[head]; head += 1
        cx, cy = curr % grid_cols, curr // grid_cols
        
        if cx == 0 or cx == grid_cols-1 or cy == 0 or cy == grid_rows-1:
            escaped = True
        
        for dx, dy in [(0,-1), (0,1), (-1,0), (1,0)]:
            nx, ny = cx+dx, cy+dy
            if 0<=nx<grid_cols and 0<=ny<grid_rows:
                ni = ny*grid_cols + nx
                if not walls[ni] and terrain[ni] == 0 and ni not in visited:
                    visited.add(ni)
                    queue.append(ni)
                    
    visited_tiles = visited
    is_escaped = escaped
    
    if escaped:
        current_score = 0
    else:
        score = len(visited)
        for i in visited:
            if cherries[i]: score += 3
        current_score = score

# 6. Drawing Helpers

def pseudo_rand(seed, min_v, max_v):
    val = (seed * 1103515245 + 12345) & 0x7FFFFFFF
    return min_v + (val % (max_v - min_v + 1))

def draw_dashed_h(x1, x2, y, col, s_min, s_max, g_min, g_max, seed):
    curr = x1
    p_seed = seed
    while curr <= x2:
        seg = pseudo_rand(p_seed, s_min, s_max)
        p_seed += 1
        gap = pseudo_rand(p_seed, g_min, g_max)
        p_seed += 1
        end = min(curr + seg, x2 + 1)
        if end > curr: dline(curr, y, end-1, y, col)
        curr += seg + gap

def draw_dashed_v(x, y1, y2, col, s_min, s_max, g_min, g_max, seed):
    curr = y1
    p_seed = seed
    while curr <= y2:
        seg = pseudo_rand(p_seed, s_min, s_max)
        p_seed += 1
        gap = pseudo_rand(p_seed, g_min, g_max)
        p_seed += 1
        end = min(curr + seg, y2 + 1)
        if end > curr: dline(x, curr, x, end-1, col)
        curr += seg + gap

def draw_horse_shape(px, py, ts):
    col = COL_HORSE
    drect(px+3, py+(ts//2), px+ts-3, py+ts-3, col)
    drect(px+ts-6, py+3, px+ts-3, py+(ts//2), col)
    dline(px+3, py+ts-3, px+3, py+ts-1, col)
    dline(px+5, py+ts-3, px+5, py+ts-1, col)
    dline(px+ts-5, py+ts-3, px+ts-5, py+ts-1, col)
    dline(px+ts-3, py+ts-3, px+ts-3, py+ts-1, col)
    dpixel(px+ts-4, py+4, C_BLACK)

def is_water(c, r):
    if 0 <= c < grid_cols and 0 <= r < grid_rows:
        return terrain[r * grid_cols + c] == 1
    return False

# 7. Main Draw Functions

def draw_water_tile(i, c, r, px, py, ts, cell_seed):
    """Draws complex water tile. Only called when force=True."""
    O1, O2 = 2, 4
    border = COL_WATER_BORDER
    
    drect(px, py, px+ts-1, py+ts-1, COL_WATER)
    
    u = is_water(c, r-1)
    d = is_water(c, r+1)
    l = is_water(c-1, r)
    ri = is_water(c+1, r)
    
    ul, ur = is_water(c-1, r-1), is_water(c+1, r-1)
    dl, dr = is_water(c-1, r+1), is_water(c+1, r+1)
    
    if not u:
        sx = px if l else px + O1
        ex = px + ts - 1 if ri else px + ts - 1 - O1
        draw_dashed_h(sx, ex, py + O1, border, 4, 7, 1, 3, cell_seed)
        sx = px if l else px + O2
        ex = px + ts - 1 if ri else px + ts - 1 - O2
        draw_dashed_h(sx, ex, py + O2, border, 3, 5, 1, 2, cell_seed+10)

    if not d:
        y_out = py + ts - 1 - O1
        sx = px if l else px + O1
        ex = px + ts - 1 if ri else px + ts - 1 - O1
        draw_dashed_h(sx, ex, y_out, border, 4, 7, 1, 3, cell_seed+20)
        y_in = py + ts - 1 - O2
        sx = px if l else px + O2
        ex = px + ts - 1 if ri else px + ts - 1 - O2
        draw_dashed_h(sx, ex, y_in, border, 3, 5, 1, 2, cell_seed+30)

    if not l:
        sy = py if u else py + O1
        ey = py + ts - 1 if d else py + ts - 1 - O1
        draw_dashed_v(px + O1, sy, ey, border, 4, 7, 1, 3, cell_seed+40)
        sy = py if u else py + O2
        ey = py + ts - 1 if d else py + ts - 1 - O2
        draw_dashed_v(px + O2, sy, ey, border, 3, 5, 1, 2, cell_seed+50)

    if not ri:
        x_out = px + ts - 1 - O1
        sy = py if u else py + O1
        ey = py + ts - 1 if d else py + ts - 1 - O1
        draw_dashed_v(x_out, sy, ey, border, 4, 7, 1, 3, cell_seed+60)
        x_in = px + ts - 1 - O2
        sy = py if u else py + O2
        ey = py + ts - 1 if d else py + ts - 1 - O2
        draw_dashed_v(x_in, sy, ey, border, 3, 5, 1, 2, cell_seed+70)

    if u and l and not ul:
        dline(px, py+O1, px+O1, py+O1, border)
        dline(px+O1, py, px+O1, py+O1, border)
        dline(px, py+O2, px+O2, py+O2, border)
        dline(px+O2, py, px+O2, py+O2, border)

    if u and ri and not ur:
        xo, xi = px + ts - 1 - O1, px + ts - 1 - O2
        dline(xo, py+O1, px+ts-1, py+O1, border)
        dline(xo, py, xo, py+O1, border)
        dline(xi, py+O2, px+ts-1, py+O2, border)
        dline(xi, py, xi, py+O2, border)

    if d and l and not dl:
        yo, yi = py + ts - 1 - O1, py + ts - 1 - O2
        dline(px, yo, px+O1, yo, border)
        dline(px+O1, yo, px+O1, py+ts-1, border)
        dline(px, yi, px+O2, yi, border)
        dline(px+O2, yi, px+O2, py+ts-1, border)

    if d and ri and not dr:
        xo, xi = px + ts - 1 - O1, px + ts - 1 - O2
        yo, yi = py + ts - 1 - O1, py + ts - 1 - O2
        dline(xo, yo, px+ts-1, yo, border)
        dline(xo, yo, xo, py+ts-1, border)
        dline(xi, yi, px+ts-1, yi, border)
        dline(xi, yi, xi, py+ts-1, border)

    if u and d and l and ri and ul and ur and dl and dr:
        cx = px + ts // 2
        cy = py + ts // 2
        dpixel(cx-2, cy+1, border)
        dpixel(cx-1, cy, border)
        dpixel(cx, cy+1, border)
        dpixel(cx+1, cy, border)
        dpixel(cx+2, cy+1, border)

def draw_dynamic_tile(i, px, py, ts, cell_seed):
    """Draws Grass, Walls, Horse, Cherry. Fast."""
    color = COL_GRASS
    if walls[i]: color = COL_WALL
    elif not is_escaped and i in visited_tiles: color = COL_ENCLOSED
    
    drect(px, py, px+ts-1, py+ts-1, color)
    
    # Detail
    if terrain[i] == 0 and not walls[i] and not cherries[i] and i != horse_pos:
        if (cell_seed % 12) == 0:
            cx = px + ts // 2
            cy = py + ts // 2
            dpixel(cx-2, cy+2, COL_GRASS_DETAIL)
            dpixel(cx-1, cy+1, COL_GRASS_DETAIL)
            dpixel(cx,   cy,   COL_GRASS_DETAIL)
            dpixel(cx+2, cy+2, COL_GRASS_DETAIL)
            dpixel(cx+3, cy+1, COL_GRASS_DETAIL)
            dpixel(cx+4, cy,   COL_GRASS_DETAIL)
    
    if i == horse_pos:
        draw_horse_shape(px, py, ts)
    elif cherries[i]:
        drect(px+5, py+5, px+ts-5, py+ts-5, COL_ALERT)

def draw_grid_optimized(force=False):
    global prev_walls, prev_visited, prev_escaped
    
    ts = tile_size
    
    # Check if a massive state change occurred (escape toggle)
    # If escaped status changed, ALL visited tiles need redraw (Gold <-> Green)
    escape_changed = (is_escaped != prev_escaped)
    
    # Init history if empty (first run)
    if not prev_walls:
        prev_walls = [False] * (grid_cols * grid_rows)
        force = True

    for r in range(grid_rows):
        for c in range(grid_cols):
            i = r * grid_cols + c
            px = grid_offset_x + c * ts
            py = grid_offset_y + r * ts
            cell_seed = (c * 13 + r * 57 + current_level_idx * 101) & 0xFFFFFF
            
            # Water: Draw ONLY on force=True
            if terrain[i] == 1:
                if force:
                    draw_water_tile(i, c, r, px, py, ts, cell_seed)
                continue
            
            # Grass/Wall: Check if redraw needed
            should_draw = force
            
            if not force:
                # 1. Wall toggled here?
                if walls[i] != prev_walls[i]:
                    should_draw = True
                # 2. Visited status changed? (Green <-> Visited Green/Gold)
                elif (i in visited_tiles) != (i in prev_visited):
                    should_draw = True
                # 3. Escape status changed AND this is a visited tile? (Green <-> Gold)
                elif escape_changed and (i in visited_tiles):
                    should_draw = True
            
            if should_draw:
                draw_dynamic_tile(i, px, py, ts, cell_seed)

    # Update history for next frame
    prev_walls = list(walls)
    prev_visited = set(visited_tiles)
    prev_escaped = is_escaped

def draw_ui_dynamic():
    global prev_walls_used, prev_score
    
    footer_y = DHEIGHT - 45
    
    # Update Walls Text only if changed
    if walls_used != prev_walls_used:
        # Clear specific rect
        drect(10, footer_y, 150, footer_y+14, COL_BACKGROUND)
        wc = COL_TEXT if walls_used <= budget else COL_ALERT
        dtext(10, footer_y, wc, f"Walls: {walls_used}/{budget}")
        prev_walls_used = walls_used
        
    # Update Score Text only if changed
    if current_score != prev_score:
        # Clear specific rect
        drect(DWIDTH - 120, footer_y - 15, DWIDTH, footer_y, COL_BACKGROUND)
        sc_txt = str(current_score) if not is_escaped else "N/A"
        sw, _ = dsize(f"Score: {sc_txt}", None)
        dtext(DWIDTH - sw - 10, footer_y - 15, COL_TEXT, f"Score: {sc_txt}")
        prev_score = current_score

def draw_static_interface():
    """Draws parts of UI that never change during a level play"""
    dclear(COL_BACKGROUND)
    draw_top_bar()
    draw_save_btn()
    
    # Best Score doesn't change during gameplay
    footer_y = DHEIGHT - 45
    lid = LEVELS[current_level_idx]['id']
    best = saves_data.get(lid, 0)
    bc = C_RGB(20,20,20)
    if best > 0: # Note: Logic for coloring best score dynamically is tricky with static, keeping simple grey
        pass 
    dtext(10, footer_y + 15, bc, f"Best: {best}")

def draw_top_bar():
    drect(0, 0, DWIDTH, 30, COL_UI_BG)
    drect(5, 5, 35, 25, COL_BTN_BG)
    dtext(15, 8, COL_TEXT, "?")
    day_str = f"Day {LEVELS[current_level_idx]['day']}"
    tw, _ = dsize(day_str, None)
    dtext((DWIDTH - tw)//2, 8, COL_ENCLOSED, day_str)
    drect(DWIDTH-35, 5, DWIDTH-5, 25, COL_BTN_BG)
    dtext(DWIDTH-25, 8, COL_TEXT, ">")

def draw_save_btn():
    by = DHEIGHT - 45
    bx = DWIDTH - 60
    drect(bx, by, bx+50, by+20, COL_BTN_BG)
    dtext(bx+10, by+4, COL_TEXT, "Save")

def draw_modal():
    if not current_modal: return
    mx, my, mw, mh = 40, 100, DWIDTH-40, 200
    drect(mx, my, mw, mh + my, COL_MODAL_BG)
    drect_border(mx, my, mw, mh + my, COL_MODAL_BG, 2, C_BLACK)
    if current_modal == "HELP":
        lvl = LEVELS[current_level_idx]
        dtext(mx+10, my+10, COL_MODAL_TEXT, "HOW TO PLAY")
        dtext(mx+10, my+30, COL_MODAL_TEXT, "Enclose the horse!")
        dtext(mx+10, my+45, COL_MODAL_TEXT, "Use limited walls.")
        dtext(mx+10, my+60, COL_MODAL_TEXT, "Cherries = +3 pts")
        dtext(mx+10, my+90, COL_ENCLOSED, f"Optimal Score: {lvl['opt']}")
        drect(mx+80, my+150, mx+160, my+180, COL_BTN_BG)
        dtext(mx+105, my+158, COL_TEXT, "OK")
    elif current_modal == "SAVE":
        dtext(mx+10, my+20, COL_MODAL_TEXT, "Save High Score?")
        score_txt = str(current_score) if not is_escaped else "0"
        dtext(mx+10, my+50, COL_ENCLOSED, f"Current: {score_txt}")
        drect(mx+20, my+100, mx+100, my+140, COL_BTN_BG)
        dtext(mx+45, my+112, COL_TEXT, "YES")
        drect(mx+140, my+100, mx+220, my+140, COL_ALERT)
        dtext(mx+170, my+112, COL_TEXT, "NO")

# 7. Main Loop

def main():
    global current_modal, saves_data
    global prev_walls_used, prev_score
    
    load_saves()
    load_level(0)
    
    # First draw: Everything
    draw_static_interface()
    draw_grid_optimized(force=True)
    draw_ui_dynamic()
    dupdate()
    
    # State flags
    full_redraw_needed = False
    
    while True:
        ev = pollevent()
        input_processed = False
        
        while ev.type != KEYEV_NONE:
            if ev.type == KEYEV_DOWN:
                if ev.key == KEY_EXIT: return
                if ev.key == KEY_SHIFT and not current_modal:
                    for i in range(len(walls)): walls[i] = False
                    input_processed = True
            
            elif ev.type == KEYEV_TOUCH_DOWN:
                tx, ty = ev.x, ev.y
                
                if current_modal:
                    mx, my = 40, 100
                    if current_modal == "HELP":
                        if mx+80 <= tx <= mx+160 and my+150 <= ty <= my+180:
                            current_modal = None
                            full_redraw_needed = True # Modal closed, need full redraw
                    elif current_modal == "SAVE":
                        if mx+20 <= tx <= mx+100 and my+100 <= ty <= my+140: 
                            if not is_escaped:
                                lid = LEVELS[current_level_idx]['id']
                                old_best = saves_data.get(lid, 0)
                                if current_score > old_best:
                                    saves_data[lid] = current_score
                                    save_game_to_disk()
                            current_modal = None
                            full_redraw_needed = True
                        elif mx+140 <= tx <= mx+220 and my+100 <= ty <= my+140:
                            current_modal = None
                            full_redraw_needed = True
                else:
                    if ty < 30:
                        if 5 <= tx <= 35: 
                            current_modal = "HELP"
                        elif DWIDTH-35 <= tx <= DWIDTH-5: 
                            next_idx = (current_level_idx + 1) % len(LEVELS)
                            load_level(next_idx)
                            # Force reset UI history to ensure redraw
                            prev_walls_used = -1
                            prev_score = -1
                            full_redraw_needed = True
                    
                    elif tx >= DWIDTH - 60 and ty >= DHEIGHT - 45:
                        current_modal = "SAVE"
                        
                    elif grid_offset_y <= ty < grid_offset_y + (grid_rows*tile_size):
                        gx = tx - grid_offset_x
                        gy = ty - grid_offset_y
                        if 0 <= gx < grid_cols*tile_size:
                            c, r = gx//tile_size, gy//tile_size
                            idx = r * grid_cols + c
                            if terrain[idx] == 0 and idx != horse_pos and not cherries[idx]:
                                if not walls[idx] and walls_used >= budget: pass
                                else:
                                    walls[idx] = not walls[idx]
                                    input_processed = True

            ev = pollevent()
            
        if input_processed:
            solve_path()
            
        # Rendering Logic
        if current_modal:
            draw_modal()
            dupdate()
        elif full_redraw_needed:
            draw_static_interface()
            draw_grid_optimized(force=True)
            draw_ui_dynamic()
            dupdate()
            full_redraw_needed = False
        elif input_processed:
            # Optimized partial redraw
            draw_grid_optimized(force=False)
            draw_ui_dynamic()
            dupdate()


main()

