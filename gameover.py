import random
import json
import os

import stage3
from pico2d import *

import MoonLighter_FrameWork
from player import Player

from missile import Missile
from hp import Hp

from slame import Enermy,Enermy2,Enermy3,Enermy4,Enermy5,Enermy6
import MoonLighter_world

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 800

name = "stageC"


boss = None
hp = None
font = None


#enermys = []


image = None


def enter():
    global image
    image = load_image('gameover.png')
    global die
    die = load_music('die.mp3')
    die.set_volume(64)

    die.play(1)


def exit():
    MoonLighter_world.clear()
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            MoonLighter_FrameWork.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            MoonLighter_FrameWork.quit()

    pass


def update():
    for MoonLighter_object in MoonLighter_world.all_objects():
        MoonLighter_object.update()



    pass


def draw():
    clear_canvas()
    image.draw(1280//2, 400)

    for MoonLighter_object in MoonLighter_world.all_objects():
        MoonLighter_object.draw()
    update_canvas()
    pass





