from pico2d import *

import MoonLighter_FrameWork
import MoonLighter_world
from player import Player


import random
player = None

class Eball:
    image = None
    isEnermy1 = True
    eBall2image2 = None
    eBall2image3 = None
    run2 = False
    isplayer = True
    FirstEball = True
    count = 0
    count2 = 0
    def __init__(self):
        if Eball.eBall2image2 == None:
            Eball.eBall2image2 = load_image('eBall2.png')
        if Eball.eBall2image3 == None:
            Eball.eBall2image3 = load_image('eBall2Up.png')
        self.font = load_font('ENCR10B.TTF', 16)

        self.x2, self.y2 = 320, 750

        self.speed = 500
        self.font = load_font('ENCR10B.TTF', 16)
        self.Hp = 100

    def get_bb(self):
        return self.x2 - 20, self.y2 - 30, self.x2 + 20, self.y2 + 30




    def draw(self):
        self.eBall2image2.draw(self.x2, self.y2)


        self.font.draw(self.x2 - 10, self.y2 + 50, '(Time: %3.2f)' % get_time(), (255, 0, 255))


        draw_rectangle(*self.get_bb())


    def update(self):
        self.y2 -= self.speed * MoonLighter_FrameWork.frame_time



        if self.y2 < 0:
            Eball.__init__(self)
            Eball.draw(self)
            Eball.update(self)
class Eball2:
    image = None
    isEnermy1 = True
    eBall2image2 = None
    eBall2image3 = None
    run2 = False
    isplayer = True
    FirstEball = True
    count = 0
    count2 = 0
    def __init__(self):
        if Eball2.eBall2image2 == None:
            Eball2.eBall2image2 = load_image('eBall2.png')

        self.font = load_font('ENCR10B.TTF', 16)

        self.x3, self.y3 = 960, 750

        self.speed = 500
        self.font = load_font('ENCR10B.TTF', 16)
        self.Hp = 100

        global player
        player = Player()

    def get_bb(self):
        return self.x3 - 20, self.y3 - 30, self.x3 + 20, self.y3 + 30


    def draw(self):
        self.eBall2image2.draw(self.x3, self.y3)

        self.font.draw(self.x3 - 10, self.y3 + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))


        draw_rectangle(*self.get_bb())


    def update(self):
        self.y3 -= self.speed * MoonLighter_FrameWork.frame_time
        if self.y3 < 0:
            Eball2.__init__(self)
            Eball2.draw(self)
            Eball2.update(self)
class Eball3:
    image = None
    isEnermy1 = True

    eBall2image3 = None
    run2 = False
    isplayer = True
    FirstEball = True
    count = 0
    count2 = 0
    def __init__(self):
        if Eball3.eBall2image3 == None:
            Eball3.eBall2image3 = load_image('eBall2Up.png')
        self.font = load_font('ENCR10B.TTF', 16)

        self.x4, self.y4 = 320, 90

        self.speed = 500
        self.font = load_font('ENCR10B.TTF', 16)
        self.Hp = 100


    def get_bb(self):
        return self.x4 - 20, self.y4 - 30, self.x4 + 20, self.y4 + 30


    def draw(self):
        self.eBall2image3.draw(self.x4, self.y4)

        self.font.draw(self.x4 - 10, self.y4 + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        draw_rectangle(*self.get_bb())


    def update(self):
        self.y4 += self.speed * MoonLighter_FrameWork.frame_time
        if self.y4 > 900:
            Eball3.__init__(self)
            Eball3.draw(self)
            Eball3.update(self)
class Eball4:
    image = None
    isEnermy1 = True

    eBall2image3 = None
    run2 = False
    isplayer = True
    FirstEball = True
    count = 0
    count2 = 0
    def __init__(self):
        if Eball4.eBall2image3 == None:
            Eball4.eBall2image3 = load_image('eBall2Up.png')
        self.font = load_font('ENCR10B.TTF', 16)

        self.x5, self.y5 = 960, 90

        self.speed = 500
        self.font = load_font('ENCR10B.TTF', 16)
        self.Hp = 100


    def get_bb(self):
        return self.x5 - 20, self.y5 - 30, self.x5 + 20, self.y5 + 30


    def draw(self):
        self.eBall2image3.draw(self.x5, self.y5)

        self.font.draw(self.x5 - 10, self.y5 + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))


        draw_rectangle(*self.get_bb())


    def update(self):
        self.y5 += self.speed * MoonLighter_FrameWork.frame_time
        if self.y5 > 900:
            Eball4.__init__(self)
            Eball4.draw(self)
            Eball4.update(self)