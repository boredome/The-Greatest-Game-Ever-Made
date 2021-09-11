from app_class import *
from pygame import mixer
#background sound
mixer.music.load('OST.mp3')
mixer.music.play(-1)


if __name__ == '__main__':
    app = App()
    app.run()
