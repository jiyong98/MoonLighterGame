import MoonLighter_FrameWork
from pico2d import *
import stage1

name = "StartState"
image = None


def enter():
    global image
    image = load_image('Start_Map.png')

    global cl
    cl = load_music('stageM.mp3')
    cl.set_volume(32)

    cl.play(1)

    global start
    start = load_music('start.mp3')
    pass


def exit():
    global image
    del(image)
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            MoonLighter_FrameWork.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            MoonLighter_FrameWork.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            start.play()
            MoonLighter_FrameWork.change_state(stage1)
    pass

def draw():
    clear_canvas()

    image.draw(1280//2, 800//2)
    update_canvas()
    pass



def update():
    pass


def pause():
    pass


def resume():
    pass






