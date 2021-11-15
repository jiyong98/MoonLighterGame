from pico2d import *

import MoonLighter_FrameWork
import MoonLighter_world

from player2 import Player

import random


class Boss:
    image = None
    run = False
    isplayer = True
    playerLife = 0
    Hp = 0
    hpimage1 = None
    hpimage2 = None
    hpimage3 = None
    hpimage4 = None
    hpimage5 = None
    def __init__(self):
        if Boss.image == None:
            Boss.image = load_image('bossC.png')
        if Boss.hpimage1 == None:
            Boss.hpimage1 = load_image('bossHp1.png')
        if Boss.hpimage2 == None:
            Boss.hpimage2 = load_image('bossHp2.png')
        if Boss.hpimage3 == None:
            Boss.hpimage3 = load_image('bossHp3.png')
        if Boss.hpimage4 == None:
            Boss.hpimage4 = load_image('bossHp4.png')
        if Boss.hpimage5 == None:
            Boss.hpimage5 = load_image('bossHp5.png')
        self.x, self.y = 900, 400
        self.font = load_font('ENCR10B.TTF', 16)

    def get_bb(self):
        return self.x - 100, self.y - 120, self.x + 100, self.y + 120
    def draw(self):
        self.image.draw(self.x, self.y)
        if Boss.Hp == 0:
            Boss.hpimage1.draw(self.x, self.y + 150)
        elif Boss.Hp == 1:
            Boss.hpimage2.draw(self.x, self.y + 150)
        elif Boss.Hp == 2:
            Boss.hpimage3.draw(self.x, self.y + 150)
        elif Boss.Hp == 3:
            Boss.hpimage4.draw(self.x, self.y + 150)
        elif Boss.Hp == 4:
            Boss.hpimage5.draw(self.x, self.y + 150)
        #draw_rectangle(*self.get_bb())

    def col(self):
        Boss.Hp += 1

    def update(self):
        if Boss.run:
            MoonLighter_world.remove_object(self)
        pass


    def remove(self):
        Boss.run = True




