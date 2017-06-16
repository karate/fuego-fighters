import pygame
from os.path import sep
from .sprite import Sprite


class Bullet(Sprite):
    # Constructor. Pass in three images of the plane
    def __init__(self, spritesheet_filename, width, height, rows,
                 columns, speed, direction):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Load sprite sheet
        _ = pygame.image.load(
            sep.join(['resources', spritesheet_filename])
        ).convert_alpha()

        self.width = width
        self.height = height
        self.speed = speed
        self.direction = direction

        Sprite.__init__(self, spritesheet_filename, width, height, rows,
                        columns)

        self.image = self.images[0]

    def update(self):
        self.rect.y += self.speed * self.direction
