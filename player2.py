from pico2d import *
import MoonLighter_world
import MoonLighter_FrameWork
#from missile import Missile

PIXEL_PER_METER = (10.0 / 1.0) # 10픽셀 30센치
RUN_SPEED_KMPH = 20.0 # km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8
def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()


    # 벗어나면 False 충돌하면 true
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP = range(4)
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP
}


class Player:
    Left = False
    Right = False
    Up = False
    Down = False
    hpimage1 = None
    hpimage2 = None
    hpimage3 = None
    hpimage4 = None
    run2 = False
    count = 0
    count2 = 0
    count3 = 0
    count4 = 0
    def __init__(self):
        self.x, self.y = 90, 800//2
        self.image = load_image('charecter_anim.png')
        self.dx, self.dy = 0, 0
        self.frame = 0
        self.dir = 1
        self.radi = 700
        self.font = load_font('ENCR10B.TTF', 16)

        if Player.hpimage1 == None:
            Player.hpimage1 = load_image('hp100.png')

        if Player.hpimage2 == None:
            Player.hpimage2 = load_image('hp75.png')

        if Player.hpimage3 == None:
            Player.hpimage3 = load_image('hp50.png')

        if Player.hpimage4 == None:
            Player.hpimage4 = load_image('hp25.png')

    def get_bb(self):
        # fill here
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def remove2(self):
        Player.run2 = True

    #def fire_Missile(self):
        #missile = Missile(self.x, self.y, self.dir * 3)
        #MoonLighter_world.add_object(missile, 1)

    def update(self):
        self.x += self.dx
        self.y += self.dy
        #self.frame = (self.frame + 1) % 4
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * MoonLighter_FrameWork.frame_time) % 4
        if self.x > 1265 or self.x < 50 or self.y > 875 or self.y < 50:
            self.x -= self.dx
            self.y -= self.dy
        if Player.run2:
            MoonLighter_world.remove_object(self)

    def draw(self):
        self.image.clip_draw(100, self.radi * 1, 100, 100, self.x, self.y)
        if Player.Right:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        elif Player.Up:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif Player.Down:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        elif Player.Left:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)

        #self.font.draw(self.x - 50, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))

        #draw_rectangle(*self.get_bb())


    def handle_event(self, event):
        if event.type == SDL_QUIT:
            MoonLighter_FrameWork.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_c:
                Player.__init__(self)
            if event.key == SDLK_RIGHT:
                self.dx += RUN_SPEED_PPS
                self.radi = 700
                Player.Right = True
            elif event.key == SDLK_LEFT:
                self.dx -= RUN_SPEED_PPS
                self.radi = 400
                Player.Left = True
            elif event.key == SDLK_UP:
                self.dy += RUN_SPEED_PPS
                self.radi = 500
                Player.Up = True
            elif event.key == SDLK_DOWN:
                self.dy -= RUN_SPEED_PPS
                self.radi = 600
                Player.Down = True
            #elif event.key == SDLK_a:
                #self.fire_Missile()
            elif event.key == SDLK_ESCAPE:
                MoonLighter_FrameWork.quit()
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                self.dx -= RUN_SPEED_PPS
                self.radi = 700
                Player.Right = False
            elif event.key == SDLK_LEFT:
                self.dx += RUN_SPEED_PPS
                self.radi = 400
                Player.Left = False
            elif event.key == SDLK_UP:
                self.dy -= RUN_SPEED_PPS
                self.radi = 500
                Player.Up = False
            elif event.key == SDLK_DOWN:
                self.dy += RUN_SPEED_PPS
                self.radi = 600
                Player.Down = False




