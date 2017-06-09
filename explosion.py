import pygame
from sprite import Sprite

class Explosion(Sprite):

  # Constructor. Pass in three images of the plane
  def __init__(self, spritesheet_filename, width, height, rows, columns,  delay):
    # Call the parent class (Sprite) constructor
    pygame.sprite.Sprite.__init__(self)

    # Load sprite sheet
    sprite_sheet = pygame.image.load('resources/' + spritesheet_filename).convert_alpha()

    self.width = width
    self.height = height
    self.image_index = 0
    self.timer = 0
    self.animation_delay = delay

    Sprite.__init__(self, spritesheet_filename, width, height, rows, columns)

    self.image = self.images[0]

  def update(self):
    self.timer += 1
    if self.timer > self.animation_delay:
      self.timer = 0
      self.image_index += 1
      if self.image_index >= len(self.images):
          self.image_index = 0
      self.image = self.images[self.image_index]
