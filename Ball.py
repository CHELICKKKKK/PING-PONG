from GameSprite import GameSprite
from pygame import *

class Ball(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

