from pico2d import *

import MoonLighter_FrameWork
import MoonLighter_world

import random

class Enermy:
    image = None
    hpimage1 = None
    hpimage3 = None
    hp = 0
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


    def get_bb(self):
        # fill here
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25


    def draw(self):
        self.image.draw(self.x, self.y)
        if Enermy.hp == 0:
            Enermy.hpimage1.draw(self.x, self.y + 50)
        elif Enermy.hp == 1:
            Enermy.hpimage3.draw(self.x, self.y + 50)

        #self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        #draw_rectangle(*self.get_bb())

    def remove(self):
        Enermy.run = True

    def col(self):
        Enermy.hp += 1

    def update(self):
        if self.By < 0:
            Enermy.__init__(self)
            Enermy.draw(self)
            Enermy.update(self)
        if Enermy.run:
            MoonLighter_world.remove_object(self)


class Enermy2:
    image = None
    hpimage1 = None
    hpimage3 = None
    hp = 0
    run = False

    def __init__(self):
        if Enermy2.image == None:
            Enermy2.image = load_image('enermy1.PNG')

        if Enermy2.hpimage1 == None:
            Enermy2.hpimage1 = load_image('hp100.png')

        if Enermy2.hpimage3 == None:
            Enermy2.hpimage3 = load_image('hp50.png')

        self.x, self.y = 900, 300

        self.Bx, self.By = self.x, self.y
        self.speed = 100
        self.font = load_font('ENCR10B.TTF', 16)
        self.Hp = 100

    def get_bb(self):
        # fill here
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def draw(self):
        self.image.draw(self.x, self.y)
        if Enermy2.hp == 0:
            Enermy2.hpimage1.draw(self.x, self.y + 50)
        elif Enermy.hp == 1:
            Enermy2.hpimage3.draw(self.x, self.y + 50)

        # self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        #draw_rectangle(*self.get_bb())

    def remove(self):
        Enermy2.run = True

    def col(self):
        Enermy2.hp += 1

    def update(self):
        if self.By < 0:
            Enermy2.__init__(self)
            Enermy2.draw(self)
            Enermy2.update(self)
        if Enermy2.run:
            MoonLighter_world.remove_object(self)


class Enermy3:
    image = None
    hpimage1 = None
    hpimage3 = None
    hp = 0
    run = False

    def __init__(self):
        if Enermy3.image == None:
            Enermy3.image = load_image('enermy1.PNG')

        if Enermy3.hpimage1 == None:
            Enermy3.hpimage1 = load_image('hp100.png')

        if Enermy3.hpimage3 == None:
            Enermy3.hpimage3 = load_image('hp50.png')

        self.x, self.y = 700, 200

        self.Bx, self.By = self.x, self.y
        self.speed = 100
        self.font = load_font('ENCR10B.TTF', 16)
        self.Hp = 100

    def get_bb(self):
        # fill here
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def draw(self):
        self.image.draw(self.x, self.y)
        if Enermy3.hp == 0:
            Enermy.hpimage1.draw(self.x, self.y + 50)
        elif Enermy3.hp == 1:
            Enermy3.hpimage3.draw(self.x, self.y + 50)

        # self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        #draw_rectangle(*self.get_bb())

    def remove(self):
        Enermy3.run = True

    def col(self):
        Enermy3.hp += 1

    def update(self):
        if self.By < 0:
            Enermy3.__init__(self)
            Enermy3.draw(self)
            Enermy3.update(self)
        if Enermy3.run:
            MoonLighter_world.remove_object(self)


class Enermy4:
    image = None
    hpimage1 = None
    hpimage3 = None
    hp = 0
    run = False

    def __init__(self):
        if Enermy4.image == None:
            Enermy4.image = load_image('enermy1.PNG')

        if Enermy4.hpimage1 == None:
            Enermy4.hpimage1 = load_image('hp100.png')

        if Enermy4.hpimage3 == None:
            Enermy4.hpimage3 = load_image('hp50.png')

        self.x, self.y = 800, 700

        self.Bx, self.By = self.x, self.y
        self.speed = 100
        self.font = load_font('ENCR10B.TTF', 16)
        self.Hp = 100

    def get_bb(self):
        # fill here
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def draw(self):
        self.image.draw(self.x, self.y)
        if Enermy4.hp == 0:
            Enermy4.hpimage1.draw(self.x, self.y + 50)
        elif Enermy4.hp == 1:
            Enermy4.hpimage3.draw(self.x, self.y + 50)

        # self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        #draw_rectangle(*self.get_bb())

    def remove(self):
        Enermy4.run = True

    def col(self):
        Enermy4.hp += 1

    def update(self):
        if self.By < 0:
            Enermy4.__init__(self)
            Enermy4.draw(self)
            Enermy4.update(self)
        if Enermy4.run:
            MoonLighter_world.remove_object(self)


class Enermy5:
    image = None
    hpimage1 = None
    hpimage3 = None
    hp = 0
    run = False

    def __init__(self):
        if Enermy5.image == None:
            Enermy5.image = load_image('enermy1.PNG')

        if Enermy5.hpimage1 == None:
            Enermy5.hpimage1 = load_image('hp100.png')

        if Enermy5.hpimage3 == None:
            Enermy5.hpimage3 = load_image('hp50.png')

        self.x, self.y = 1000, 500

        self.Bx, self.By = self.x, self.y
        self.speed = 100
        self.font = load_font('ENCR10B.TTF', 16)
        self.Hp = 100

    def get_bb(self):
        # fill here
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def draw(self):
        self.image.draw(self.x, self.y)
        if Enermy5.hp == 0:
            Enermy5.hpimage1.draw(self.x, self.y + 50)
        elif Enermy5.hp == 1:
            Enermy5.hpimage3.draw(self.x, self.y + 50)

        # self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        #draw_rectangle(*self.get_bb())

    def remove(self):
        Enermy5.run = True

    def col(self):
        Enermy5.hp += 1

    def update(self):
        if self.By < 0:
            Enermy5.__init__(self)
            Enermy5.draw(self)
            Enermy5.update(self)
        if Enermy5.run:
            MoonLighter_world.remove_object(self)


class Enermy6:
    image = None
    hpimage1 = None
    hpimage3 = None
    hp = 0
    run = False

    def __init__(self):
        if Enermy6.image == None:
            Enermy6.image = load_image('enermy1.PNG')

        if Enermy6.hpimage1 == None:
            Enermy6.hpimage1 = load_image('hp100.png')

        if Enermy6.hpimage3 == None:
            Enermy6.hpimage3 = load_image('hp50.png')

        self.x, self.y = 700, 400

        self.Bx, self.By = self.x, self.y
        self.speed = 100
        self.font = load_font('ENCR10B.TTF', 16)
        self.Hp = 100

    def get_bb(self):
        # fill here
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def draw(self):
        self.image.draw(self.x, self.y)
        if Enermy6.hp == 0:
            Enermy6.hpimage1.draw(self.x, self.y + 50)
        elif Enermy6.hp == 1:
            Enermy6.hpimage3.draw(self.x, self.y + 50)

        # self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        #draw_rectangle(*self.get_bb())

    def remove(self):
        Enermy6.run = True

    def col(self):
        Enermy6.hp += 1

    def update(self):
        if self.By < 0:
            Enermy6.__init__(self)
            Enermy6.draw(self)
            Enermy6.update(self)
        if Enermy6.run:
            MoonLighter_world.remove_object(self)