from pico2d import *

import MoonLighter_FrameWork
import MoonLighter_world

from player2 import Player

import random


class Enermy2:
    image2 = None
    run2 = False
    isplayer = True
    playerLife = 0

    def __init__(self):
        if Enermy2.image2 == None:
            Enermy2.image2 = load_image('enermy2.PNG')

        self.x2, self.y2 = 320, 750
        self.x3, self.y3 = 960, 750
        self.x4, self.y4 = 320, 50
        self.x5, self.y5 = 960, 50

    def draw(self):
        self.image2.draw(self.x2, self.y2)
        self.image2.draw(self.x3, self.y3)
        self.image2.draw(self.x4, self.y4)
        self.image2.draw(self.x5, self.y5)

    def update(self):
        pass




