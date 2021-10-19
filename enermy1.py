from pico2d import *

import MoonLighter_FrameWork
import MoonLighter_world

from player2 import Player

import random

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


def collide2(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb2()
    left_b, bottom_b, right_b, top_b = b.get_bb2()

    # 벗어나면 False 충돌하면 true
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def collide3(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb3()
    left_b, bottom_b, right_b, top_b = b.get_bb3()

    # 벗어나면 False 충돌하면 true
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def collide4(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb4()
    left_b, bottom_b, right_b, top_b = b.get_bb4()

    # 벗어나면 False 충돌하면 true
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

class Enermy2:
    image2 = None
    eBall2image2 = None
    eBall2image3 = None
    run2 = False
    isplayer = True
    playerLife = 0

    def __init__(self):
        if Enermy2.image2 == None:
            Enermy2.image2 = load_image('enermy2.PNG')
        if Enermy2.eBall2image2 == None:
            Enermy2.eBall2image2 = load_image('eBall2.png')
        if Enermy2.eBall2image3 == None:
            Enermy2.eBall2image3 = load_image('eBall2Up.png')

        self.x2, self.y2 = 320, 750
        self.x3, self.y3 = 960, 750
        self.x4, self.y4 = 320, 50
        self.x5, self.y5 = 960, 50
        self.Bx2, self.By2 = self.x2, self.y2
        self.Bx3, self.By3 = self.x3, self.y3
        self.Bx4, self.By4 = self.x4, self.y4
        self.Bx5, self.By5 = self.x5, self.y5
        self.speed = 500
        #self.font = load_font('ENCR10B.TTF', 16)
        self.Hp = 100

        global playerlife
        playerlife = Player()

    def get_bb(self):
        return self.Bx2 - 25, self.By2 - 50, self.Bx2 + 25, self.By2 + 50

    def get_bb2(self):
        return self.Bx3 - 25, self.By3 - 50, self.Bx3 + 25, self.By3 + 50

    def get_bb3(self):
        return self.Bx4 - 25, self.By4 - 50, self.Bx4 + 25, self.By4 + 50

    def get_bb4(self):
        return self.Bx5 - 25, self.By5 - 50, self.Bx5 + 25, self.By5 + 50

    def draw(self):
        self.eBall2image2.draw(self.Bx2, self.By2)
        self.image2.draw(self.x2, self.y2)
        self.eBall2image2.draw(self.Bx3, self.By3)
        self.image2.draw(self.x3, self.y3)
        self.eBall2image3.draw(self.Bx4, self.By4)
        self.image2.draw(self.x4, self.y4)
        self.eBall2image3.draw(self.Bx5, self.By5)
        self.image2.draw(self.x5, self.y5)


        # self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        # self.font.draw(self.x2 - 60, self.y2 + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))

        #draw_rectangle(*self.get_bb())


    def remove2(self):
        Enermy2.run2 = True

    def update(self):
        self.By2 -= self.speed * MoonLighter_FrameWork.frame_time
        self.By3 -= self.speed * MoonLighter_FrameWork.frame_time
        self.By4 += self.speed * MoonLighter_FrameWork.frame_time
        self.By5 += self.speed * MoonLighter_FrameWork.frame_time
        if Enermy2.isplayer:
            if collide(self, playerlife):
                Enermy2.playerLife = Enermy2.playerLife + 1
                MoonLighter_world.remove_object(self)
            if playerlife.count2 >= 4:
                playerlife.remove2(playerlife)
                Enermy2.isplayer = False

        if self.By2 < 0:
            Enermy2.__init__(self)
            Enermy2.draw(self)
            Enermy2.update(self)

        if Enermy2.run2:
            MoonLighter_world.remove_object(self)





