import random
from pico2d import *
import MoonLighter_world
from slame import Enermy

from player2 import Player

enermy1 = None
enermy2 = None
players = None
global count
count = 0
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

class Missile:
    image = None
    isEnermy1 = True
    isEnermy2 = True
    count = 0
    count2 = 0
    run = False
    L, R, U, D = 0, 0, 0, 0

    def __init__(self, x = 0, y = 0, velocity = 1):
        if Missile.image == None:
            Missile.image = load_image('eBall.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.font = load_font('ENCR10B.TTF', 16)
        global slames
        slames = Enermy()

    def get_bb(self):
        # fill here
        return self.x - 8, self.y - 8, self.x + 8, self.y + 8

    def draw(self):
        self.image.draw(self.x, self.y)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        # fill here
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.velocity

        #if Missile.R == 1:
            #self.x += self.velocity
        #elif Missile.L == 1:
            #self.x -= self.velocity
        #elif Missile.U == 1:
         #   self.y += self.velocity
        #elif Missile.D == 1:
         #   self.y -= self.velocity

        if Missile.isEnermy1:
            if collide(self, slames):
                Missile.count = Missile.count + 1
                MoonLighter_world.remove_object(self)
            if Missile.count >= 2:
                Enermy.remove(slames)
                Missile.isEnermy1 = False
        if Missile.run:
            MoonLighter_world.remove_object(self)


        if self.y < 25 or self.y > 1000 - 25:
            MoonLighter_world.remove_object(self)

    def remove(self):
        Missile.run = True