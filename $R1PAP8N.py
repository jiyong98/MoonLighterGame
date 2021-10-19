from pico2d import *

import MoonLighter_FrameWork
import MoonLighter_world

from player2 import Player
import random

class Hp:
    image1 = None
    image2 = None
    image3 = None
    image4 = None

    def __init__(self, x = 0, y = 0):
        if Hp.image1 == None:
            Hp.image1 = load_image('playerHp.png')

        if Hp.image2 == None:
            Hp.image2 = load_image('hp75.png')

        if Hp.image3 == None:
            Hp.image3 = load_image('hp50.png')

        #self.x, self.y = 250, 400
        self.x2, self.y2 = 150, 700
        self.x3, self.y3 = x, y
        self.x4, self.y4 = x, y
        self.Hp = 100


        global players
        players = Player()

    def draw(self):

        if players.count2 == 0:
            self.image1.draw(self.x2, self.y2 + 40)
        elif players.count2 == 1:
            self.image2.draw(self.x2, self.y2 + 40)
        elif players.count2 == 2:
            self.image3.draw(self.x2, self.y2 + 40)


        # self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))

    def remove(self):
        MoonLighter_world.remove_object(self)

    def update(self):
        pass







