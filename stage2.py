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

name = "stage2"


boss = None
hp = None
font = None


#enermys = []


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

    global enermys
    #enermys = [Enermy() for i in range(6)]
    enermys = Enermy()
    MoonLighter_world.add_object(enermys, 1)
    #MoonLighter_world.add_objects(enermys, 1)
    global enermys2
    # enermys = [Enermy() for i in range(6)]
    enermys2 = Enermy2()
    MoonLighter_world.add_object(enermys2, 1)

    global enermys3
    # enermys = [Enermy() for i in range(6)]
    enermys3 = Enermy3()
    MoonLighter_world.add_object(enermys3, 1)

    global enermys4
    # enermys = [Enermy() for i in range(6)]
    enermys4 = Enermy4()
    MoonLighter_world.add_object(enermys4, 1)

    global enermys5
    # enermys = [Enermy() for i in range(6)]
    enermys5 = Enermy5()
    MoonLighter_world.add_object(enermys5, 1)

    global enermys6
    # enermys = [Enermy() for i in range(6)]
    enermys6 = Enermy6()
    MoonLighter_world.add_object(enermys6, 1)


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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            MoonLighter_FrameWork.change_state(stage3)
        else:
            players.handle_event(event)

    pass


def update():
    for MoonLighter_object in MoonLighter_world.all_objects():
        MoonLighter_object.update()

    if Missile.Total == 12:
        Missile.isStage2 = False
        Missile.isStage3 = True
        MoonLighter_FrameWork.change_state(stage3)


    #for ball in eBalls:
     #   if collide(players, ball):
      #      eBalls.remove(ball)
       #     MoonLighter_world.remove_object(ball)
        #    print("충돌")

    pass


def draw():
    clear_canvas()
    image.draw(1280//2, 400)
    for MoonLighter_object in MoonLighter_world.all_objects():
        MoonLighter_object.draw()
    update_canvas()
    pass





