from os.path import sep
import pygame
from .sprite import Sprite
from constants import SpriteInfo


class Bullet(Sprite):
    # Constructor. Pass in three images of the plane
    def __init__(self, type, speed, direction):
        # Call the parent class (Sprite) constructor
        _sprite_info = SpriteInfo.TYPES[type]
        self._sprite = Sprite.__init__(self, _sprite_info)

        self.width = _sprite_info['width']
        self.height = _sprite_info['height']
        self.speed = speed
        self.direction = direction

        self.image = self.images[0]

    def update(self):
        self.rect.y += self.speed * self.direction
