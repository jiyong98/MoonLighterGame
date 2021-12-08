from pico2d import *

import MoonLighter_FrameWork
import MoonLighter_world

import random

class Enermy:
    image = None
    hpimage1 = None
    hpimage3 = None
    efimage = None
    hp = 0
    x = 0
    y = 0
    run = False
    ef = False
    def __init__(self):
        if Enermy.image == None:
            Enermy.image = load_image('slameAni.PNG')

        if Enermy.efimage == None:
            Enermy.efimage = load_image('effect.png')

        if Enermy.hpimage1 == None:
            Enermy.hpimage1 = load_image('hp100.png')

        if Enermy.hpimage3 == None:
            Enermy.hpimage3 = load_image('hp50.png')

        self.x, self.y = 800, 500
        self.frame = 0
        self.Bx, self.By = self.x, self.y
        self.speed = 100
        self.font = load_font('ENCR10B.TTF', 16)
        self.Hp = 100
        self.s = 0.15
        self.Mx = 0.2


    def get_bb(self):
        # fill here
        return Enermy.x - 25, self.y - 25, Enermy.x + 25, self.y + 25


    def draw(self):
        Enermy.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
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
        self.y += self.s
        self.x -= self.Mx
        Enermy.x = self.x
        Enermy.y = self.y
        if self.y >= 510:
            self.s *= -1
        if self.y <= 490:
            self.s *= -1
        self.frame = (self.frame + 1) % 5
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
    x = 0
    run = False

    def __init__(self):
        if Enermy2.image == None:
            Enermy2.image = load_image('slameAni.png')


        if Enermy2.hpimage1 == None:
            Enermy2.hpimage1 = load_image('hp100.png')

        if Enermy2.hpimage3 == None:
            Enermy2.hpimage3 = load_image('hp50.png')
        self.x, self.y = 900, 300
        self.frame = 0
        self.Bx, self.By = self.x, self.y
        self.speed = 100
        self.s = 0.2
        self.font = load_font('ENCR10B.TTF', 16)
        self.Hp = 100
        self.Mx = 0.1

    def get_bb(self):
        # fill here
        return Enermy2.x - 25, self.y - 25, Enermy2.x + 25, self.y + 25

    def draw(self):
        ##self.image.draw(self.x, self.y)
        Enermy2.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        if Enermy2.hp == 0:
            Enermy2.hpimage1.draw(self.x, self.y + 50)
        elif Enermy2.hp == 1:
            Enermy2.hpimage3.draw(self.x, self.y + 50)


        # self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))


    def remove(self):
        Enermy2.run = True

    def col(self):
        Enermy2.hp += 1

    def update(self):
        self.y += self.s
        self.x -= self.Mx
        Enermy2.x = self.x
        if self.y >= 310:
            self.s *= -1
        if self.y <= 290:
            self.s *= -1
        self.frame = (self.frame + 1) % 5

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
    x = 0

    def __init__(self):
        if Enermy3.image == None:
            Enermy3.image = load_image('slameAni.png')

        if Enermy3.hpimage1 == None:
            Enermy3.hpimage1 = load_image('hp100.png')

        if Enermy3.hpimage3 == None:
            Enermy3.hpimage3 = load_image('hp50.png')
        self.x, self.y = 600, 200
        self.frame = 0
        self.Bx, self.By = self.x, self.y
        self.speed = 100
        self.s = 0.2
        self.font = load_font('ENCR10B.TTF', 16)
        self.Hp = 100
        self.Mx = 0.2

    def get_bb(self):
        # fill here
        return Enermy3.x - 25, self.y - 25, Enermy3.x + 25, self.y + 25

    def draw(self):
        ##self.image.draw(self.x, self.y)
        Enermy3.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        if Enermy3.hp == 0:
            Enermy3.hpimage1.draw(self.x, self.y + 50)
        elif Enermy3.hp == 1:
            Enermy3.hpimage3.draw(self.x, self.y + 50)

        # self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        #draw_rectangle(*self.get_bb())

    def remove(self):
        Enermy3.run = True

    def col(self):
        Enermy3.hp += 1

    def update(self):
        self.y += self.s
        self.x -= self.Mx
        Enermy3.x = self.x
        if self.y >= 210:
            self.s *= -1
        if self.y <= 190:
            self.s *= -1
        self.frame = (self.frame + 1) % 5
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
    x = 0

    def __init__(self):
        if Enermy4.image == None:
            Enermy4.image = load_image('slameAni.png')

        if Enermy4.hpimage1 == None:
            Enermy4.hpimage1 = load_image('hp100.png')

        if Enermy4.hpimage3 == None:
            Enermy4.hpimage3 = load_image('hp50.png')
        self.x, self.y = 800, 200
        self.frame = 0
        self.Bx, self.By = self.x, self.y
        self.speed = 100
        self.font = load_font('ENCR10B.TTF', 16)
        self.Hp = 100
        self.s = 0.25
        self.Mx = 0.33

    def get_bb(self):
        # fill here
        return Enermy4.x - 25, self.y - 25, Enermy4.x + 25, self.y + 25

    def draw(self):
        ##self.image.draw(self.x, self.y)

        Enermy4.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
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
        self.y += self.s
        self.x -= self.Mx
        Enermy4.x = self.x
        if self.y >= 210:
            self.s *= -1
        if self.y <= 190:
            self.s *= -1
        self.frame = (self.frame + 1) % 5

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
    x = 0

    def __init__(self):
        if Enermy5.image == None:
            Enermy5.image = load_image('slameAni.png')

        if Enermy5.hpimage1 == None:
            Enermy5.hpimage1 = load_image('hp100.png')

        if Enermy5.hpimage3 == None:
            Enermy5.hpimage3 = load_image('hp50.png')
        self.x, self.y = 500, 400
        self.frame = 0
        self.Bx, self.By = self.x, self.y
        self.speed = 100
        self.font = load_font('ENCR10B.TTF', 16)
        self.Hp = 100
        self.s = 0.2
        self.Mx = 0.1

    def get_bb(self):
        # fill here
        return Enermy5.x - 25, self.y - 25, Enermy5.x + 25, self.y + 25

    def draw(self):
        ##self.image.draw(self.x, self.y)
        Enermy5.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
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
        self.y += self.s
        self.x -= self.Mx
        Enermy5.x = self.x
        if self.y >= 410:
            self.s *= -1
        if self.y <= 390:
            self.s *= -1
        self.frame = (self.frame + 1) % 5
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
    x = 0

    def __init__(self):
        if Enermy6.image == None:
            Enermy6.image = load_image('slameAni.png')

        if Enermy6.hpimage1 == None:
            Enermy6.hpimage1 = load_image('hp100.png')

        if Enermy6.hpimage3 == None:
            Enermy6.hpimage3 = load_image('hp50.png')
        self.x, self.y = 700, 600
        self.frame = 0
        self.Bx, self.By = self.x, self.y
        self.speed = 100
        self.font = load_font('ENCR10B.TTF', 16)
        self.Hp = 100
        self.s = 0.2
        self.Mx = 0.2

    def get_bb(self):
        # fill here

        return Enermy6.x - 25, self.y - 25, Enermy6.x + 25, self.y + 25

    def draw(self):
        ##self.image.draw(self.x, self.y)
        Enermy6.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
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
        self.y += self.s
        self.x -= self.Mx
        Enermy6.x = self.x
        if self.y >= 610:
            self.s *= -1
        if self.y <= 590:
            self.s *= -1
        self.frame = (self.frame + 1) % 5
        if self.By < 0:
            Enermy6.__init__(self)
            Enermy6.draw(self)
            Enermy6.update(self)
        if Enermy6.run:
            MoonLighter_world.remove_object(self)