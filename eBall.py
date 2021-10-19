import random
from pico2d import *
import MoonLighter_world

from player2 import Player

player2 = None
global count
count = 0

def collide(self, b):
    # fill here
    left_a, bottom_a, right_a, top_a = self.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    # 벗어나면 False 충돌하면 true
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True
class Eball:
    image = None
    isEnermy1 = True

    count = 0
    count2 = 0
    def __init__(self, x = 0, y = 0, velocity = 1):
        if Eball.image == None:
            Eball.image = load_image('eBall2.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.font = load_font('ENCR10B.TTF', 16)

        global player2
        player2 = Player()



    def get_bb(self):
        # fill here
        return self.x - 5, self.y - 15, self.x + 5, self.y + 15

    def draw(self):
        self.image.draw(self.x, self.y)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        # fill here
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y += self.velocity

        if Eball.isEnermy1:
            if collide(self, player2):
                Eball.count = Eball.count + 1
                MoonLighter_world.remove_object(self)
            if Eball.count >= 4:
                Eball.remove(player2)
                Eball.isEnermy1 = False



        if self.y < 25 or self.y > 1000 - 25:
            MoonLighter_world.remove_object(self)

