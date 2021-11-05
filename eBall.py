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
        self.x3, self.y3 = 960, 750
        self.x4, self.y4 = 320, 50
        self.x5, self.y5 = 960, 50

        self.speed = 500
        self.font = load_font('ENCR10B.TTF', 16)
        self.Hp = 100

        global player
        player = Player()

    def get_bb(self):
        return self.x2 - 20, self.y2 - 30, self.x2 + 20, self.y2 + 30

    #def get_bb2(self):
        #return self.Bx3 - 20, self.By3 - 30, self.Bx3 + 20, self.By3 + 30

    #def get_bb3(self):
        #return self.Bx4 - 20, self.By4 - 30, self.Bx4 + 20, self.By4 + 30

    #def get_bb4(self):
        #return self.Bx5 - 20, self.By5 - 30, self.Bx5 + 20, self.By5 + 30


    def draw(self):
        self.eBall2image2.draw(self.x2, self.y2)
        #self.eBall2image2.draw(self.Bx3, self.By3)
        #self.eBall2image3.draw(self.Bx4, self.By4)
        #self.eBall2image3.draw(self.Bx5, self.By5)

        self.font.draw(self.x2 - 10, self.y2 + 50, '(Time: %3.2f)' % get_time(), (255, 0, 255))
        #self.font.draw(self.Bx3 - 10, self.By3 + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        #self.font.draw(self.Bx4 - 10, self.By4 + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        #self.font.draw(self.Bx5 - 10, self.By5 + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))

        draw_rectangle(*self.get_bb())
        #draw_rectangle(*self.get_bb2())
        #draw_rectangle(*self.get_bb3())
        #draw_rectangle(*self.get_bb4())

    def update(self):
        self.y2 -= self.speed * MoonLighter_FrameWork.frame_time
        #self.By3 -= self.speed * MoonLighter_FrameWork.frame_time
        #self.By4 += self.speed * MoonLighter_FrameWork.frame_time
        #self.By5 += self.speed * MoonLighter_FrameWork.frame_time

        if Eball.FirstEball:
            if collide(self, player):
                # Enermy2.playerLife = Enermy2.playerLife + 1
                print('충돌')
                MoonLighter_world.remove_object(self)


        if self.y2 < 0:
            Eball.__init__(self)
            Eball.draw(self)
            Eball.update(self)
