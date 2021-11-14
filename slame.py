from pico2d import *

import MoonLighter_FrameWork
import MoonLighter_world
from missile import Missile
import random

class Enermy:
    image = None
    isLife = True
    hpimage1 = None

    hpimage3 = None

    run = False
    def __init__(self):
        if Enermy.image == None:
            Enermy.image = load_image('enermy1.PNG')

        if Enermy.hpimage1 == None:
            Enermy.hpimage1 = load_image('hp100.png')

        if Enermy.hpimage3 == None:
            Enermy.hpimage3 = load_image('hp50.png')

        self.x, self.y = 800, 500

        self.Bx, self.By = self.x, self.y
        self.speed = 100
        self.font = load_font('ENCR10B.TTF', 16)
        self.Hp = 100
        global missile
        missile = Missile()

    def get_bb(self):
        # fill here
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25


    def draw(self):
        self.image.draw(self.x, self.y)


        #self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        draw_rectangle(*self.get_bb())

    def remove(self):
        Enermy.run = True

    def update(self):

        if self.By < 0:
            Enermy.__init__(self)
            Enermy.draw(self)
            Enermy.update(self)

        if Enermy.run:
            MoonLighter_world.remove_object(self)
