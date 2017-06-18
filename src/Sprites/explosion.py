import pygame
from .sprite import Sprite
from constants import SpriteInfo


class Explosion(Sprite):
    # Constructor. Pass in three images of the plane
    def __init__(self, type, delay):
        # Call the parent class (Sprite) constructor
        _sprite_info = SpriteInfo.TYPES[type]
        Sprite.__init__(self, _sprite_info)

        self.image_index = 0
        self.timer = 0
        self.animation_delay = delay

        self.image = self.images[0]

    def update(self):
        self.timer += 1
        if self.timer > self.animation_delay:
            self.timer = 0
            self.image_index += 1
            if self.image_index < len(self.images):
                self.image = self.images[self.image_index]
