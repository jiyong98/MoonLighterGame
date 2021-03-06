import random
import json
import os

from pico2d import *

import MoonLighter_FrameWork
from player import Player

from eBall import Eball, Eball2, Eball3, Eball4
from boss import Boss
from missile import Missile
from hp import Hp
import gameover
from enermy1 import Enermy2
import MoonLighter_world
import start_state
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 800
import clear
name = "stage3"


boss = None
hp = None
font = None
eBalls = []
eBalls2 = []


#enermy1s = None
enermy2s = None
missiles = None
image = None
clearc = None

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
    image = load_image('Stage1.png')

    global clearc
    clearc = load_image('stageClear.png')

    global attack
    attack = load_music('eballattack.mp3')
    attack.set_volume(30)

    global die
    die = load_music('die.mp3')
    die.set_volume(64)
    global stageC
    stageC = load_music('stageC.mp3')
    stageC.set_volume(64)
    global boss
    boss = Boss()
    MoonLighter_world.add_object(boss, 1)
    global players
    players = Player()
    MoonLighter_world.add_object(players, 1)

    global hp
    hp = Hp()
    MoonLighter_world.add_object(hp, 1)

    global eBalls
    eBalls = [Eball() for i in range(1)]
    MoonLighter_world.add_objects(eBalls, 1)

    global eBalls2
    eBalls2 = [Eball2() for i in range(1)]
    MoonLighter_world.add_objects(eBalls2, 1)

    global eBalls3
    eBalls3 = [Eball3() for i in range(1)]
    MoonLighter_world.add_objects(eBalls3, 1)

    global eBalls4
    eBalls4 = [Eball4() for i in range(1)]
    MoonLighter_world.add_objects(eBalls4, 1)


    #global enermy1s
    #enermy1s = Enermy()
    #MoonLighter_world.add_object(enermy1s, 1)

    global enermy2s
    enermy2s = Enermy2()
    MoonLighter_world.add_object(enermy2s, 1)

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
        #stageC.play()
    pass


def update():
    for MoonLighter_object in MoonLighter_world.all_objects():
        MoonLighter_object.update()

    for ball in eBalls:
        if collide(players, ball):
            eBalls.remove(ball)
            MoonLighter_world.remove_object(ball)
            Hp.count += 1
            attack.play()
            print("충돌")

    for ball2 in eBalls2:
        if collide(players, ball2):
            eBalls2.remove(ball2)
            MoonLighter_world.remove_object(ball2)
            Hp.count += 1
            attack.play()
            print("충돌")
    for ball3 in eBalls3:
        if collide(players, ball3):
            eBalls3.remove(ball3)
            MoonLighter_world.remove_object(ball3)
            attack.play()
            Hp.count += 1
            print("충돌")
    for ball4 in eBalls4:
        if collide(players, ball4):
            eBalls4.remove(ball4)
            MoonLighter_world.remove_object(ball4)
            Hp.count += 1
            attack.play()
            print("충돌")
    if Hp.count >= 3:
        die.play()
        MoonLighter_FrameWork.change_state(gameover)




    pass



def draw():
    clear_canvas()
    image.draw(1280//2, 400)
    global time
    #if Boss.Hp >= 4 and Player.x >= 1200:
        #clearc.draw(1280 // 2, 400)

    if Boss.Hp >= 4 and Player.x >= 1200:
        stageC.play()
        MoonLighter_FrameWork.change_state(clear)

    for MoonLighter_object in MoonLighter_world.all_objects():
        MoonLighter_object.draw()
    update_canvas()
    pass





