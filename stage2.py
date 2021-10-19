import random
import json
import os

from pico2d import *

import MoonLighter_FrameWork
from player import Player

from missile import Missile
from hp import Hp

from enermy import Enermy
import MoonLighter_world

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 800

name = "stage2"

players = None
boss = None
hp = None
font = None


enermy1s = []

missiles = None
image = None


def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    # 벗어나면 False 충돌하면 true
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True
def enter():
    global image
    image = load_image('Stage2.png')

    global players
    players = Player()
    MoonLighter_world.add_object(players, 1)

    global hp
    hp = Hp()
    MoonLighter_world.add_object(hp, 1)

    global enermy1s
    enermy1s = [Enermy()] * 6
    MoonLighter_world.add_objects(enermy1s, 1)


    global missiles
    missiles = Missile()
    MoonLighter_world.add_object(missiles, 1)
    pass

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
        else:
            players.handle_event(event)

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





