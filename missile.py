import random
from pico2d import *
import MoonLighter_world
from slame import Enermy,Enermy2,Enermy3,Enermy4,Enermy5,Enermy6
from boss import Boss
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
    isEnermy3 = True
    isEnermy4 = True
    isEnermy5 = True
    isEnermy6 = True
    isBoss = True
    BossCount = 0
    count = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    Total = 0
    run = False
    isStage2 = False
    isStage3 = False
    isRad = True
    L, R, U, D = 0, 1, 0, 0
    rad = 0
    def __init__(self, x = 0, y = 0, velocity = 1):
        if Missile.image == None:
            Missile.image = load_image('eBall.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.font = load_font('ENCR10B.TTF', 16)
        global boss
        boss = Boss()
        global slames
        slames = Enermy()
        global slames2
        slames2 = Enermy2()
        global slames3
        slames3 = Enermy3()
        global slames4
        slames4 = Enermy4()
        global slames5
        slames5 = Enermy5()
        global slames6
        slames6 = Enermy6()

    def get_bb(self):
        # fill here
        return self.x - 8, self.y - 8, self.x + 8, self.y + 8

    def draw(self):
        self.image.draw(self.x, self.y)
        #self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))

        # fill here
        #draw_rectangle(*self.get_bb())

    def update(self):

        self.x += self.velocity

        Missile.Total = Missile.count + Missile.count2 + Missile.count3 + \
                        Missile.count4 + Missile.count5 + Missile.count6
        #if Missile.R == 1:
            #self.x += self.velocity
        #elif Missile.L == 1:
            #self.x -= self.velocity
        #elif Missile.U == 1:
         #   self.y += self.velocity
        #elif Missile.D == 1:
         #   self.y -= self.velocity
        if Missile.isStage2:
            if Missile.isEnermy1:
                if collide(self, slames):
                    Missile.count = Missile.count + 1
                    Enermy.col(slames)
                    MoonLighter_world.remove_object(self)
                if Missile.count >= 2:
                    Enermy.remove(slames)
                    Missile.isEnermy1 = False
            if Missile.isEnermy2:
                if collide(self, slames2):
                    Missile.count2 = Missile.count2 + 1
                    Enermy2.col(slames2)
                    MoonLighter_world.remove_object(self)
                if Missile.count2 >= 2:
                    Enermy2.remove(slames2)
                    Missile.isEnermy2 = False

            if Missile.isEnermy3:
                if collide(self, slames3):
                    Missile.count3 = Missile.count3 + 1
                    Enermy3.col(slames3)
                    MoonLighter_world.remove_object(self)
                if Missile.count3 >= 2:
                    Enermy3.remove(slames3)
                    Missile.isEnermy3 = False

            if Missile.isEnermy4:
                if collide(self, slames4):
                    Missile.count4 = Missile.count4 + 1
                    Enermy4.col(slames4)
                    MoonLighter_world.remove_object(self)
                if Missile.count4 >= 2:
                    Enermy4.remove(slames4)
                    Missile.isEnermy4 = False

            if Missile.isEnermy5:
                if collide(self, slames5):
                    Missile.count5 = Missile.count5 + 1
                    Enermy5.col(slames5)
                    MoonLighter_world.remove_object(self)
                if Missile.count5 >= 2:
                    Enermy5.remove(slames5)
                    Missile.isEnermy5 = False

            if Missile.isEnermy6:
                if collide(self, slames6):
                    Missile.count6 = Missile.count6 + 1
                    Enermy6.col(slames6)
                    MoonLighter_world.remove_object(self)
                if Missile.count6 >= 2:
                    Enermy6.remove(slames6)
                    Missile.isEnermy6 = False
        if Missile.isStage3:
            if Missile.isBoss:
                if collide(self, boss):
                    Missile.BossCount = Missile.BossCount + 1
                    Boss.col(boss)
                    MoonLighter_world.remove_object(self)
                if Missile.BossCount >= 5:
                    Boss.remove(boss)
                    Missile.isBoss = False
        if Missile.run:
            MoonLighter_world.remove_object(self)


        if self.y < 25 or self.y > 800 - 25:
            MoonLighter_world.remove_object(self)
        if self.x < 25 or self.x > 1280 - 25:
            MoonLighter_world.remove_object(self)

    def remove(self):
        Missile.run = True