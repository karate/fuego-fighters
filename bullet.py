import pygame
from sprite import Sprite

class Bullet(Sprite):

  # Constructor. Pass in three images of the plane
  def __init__(self, spritesheet_filename, width, height, rows, columns, speed, ):
    # Call the parent class (Sprite) constructor
    pygame.sprite.Sprite.__init__(self)

    # Load sprite sheet
    sprite_sheet = pygame.image.load('resources/' + spritesheet_filename).convert_alpha()

    self.width = width
    self.height = height
    self.speed = speed

    Sprite.__init__(self, spritesheet_filename, width, height, rows, columns)

    self.image = self.images[0]

  def update(self):
    self.rect.y -= self.speed
