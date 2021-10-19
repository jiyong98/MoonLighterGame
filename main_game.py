import MoonLighter_FrameWork
import pico2d

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 800

import start_state

pico2d.open_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)
MoonLighter_FrameWork.run(start_state)
pico2d.close_canvas()