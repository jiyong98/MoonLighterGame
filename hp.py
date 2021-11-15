from pico2d import *

import MoonLighter_FrameWork
import MoonLighter_world
from missile import Missile
import random

class Hp:
    imageFir = None
    imageSec = None
    imageTre = None
    count = 0

    image1 = None
    image2 = None
    image3 = None
    image4 = None

    def __init__(self, x = 0, y = 0):
        if Hp.imageFir == None:
            Hp.imageFir = load_image('playerHp.png')
        if Hp.imageSec == None:
            Hp.imageSec = load_image('playerHp2.png')
        if Hp.imageTre == None:
            Hp.imageTre = load_image('playerHp3.png')
        if Hp.image1 == None:
            Hp.image1 = load_image('hp100.png')

        if Hp.image2 == None:
            Hp.image2 = load_image('hp75.png')

        if Hp.image3 == None:
            Hp.image3 = load_image('hp50.png')

        if Hp.image4 == None:
            Hp.image4 = load_image('hp25.png')
        self.x, self.y = 150, 750
        self.x2, self.y2 = 500, 400
        self.x3, self.y3 = x, y
        self.x4, self.y4 = x, y

        self.Bx, self.By = 500, 800
        self.Hp = 100
        self.font = load_font('ENCR10B.TTF', 16)
        global missile
        missile = Missile()


    def draw(self):
        if Hp.count == 0:
            self.imageFir.draw(self.x, self.y)
        elif Hp.count == 1:
            self.imageSec.draw(self.x, self.y)
        elif Hp.count == 2:
            self.imageTre.draw(self.x, self.y)

        # self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))

    def remove(self):
        MoonLighter_world.remove_object(self)

    def update(self):
        pass







