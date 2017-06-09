import pygame
from plane import Plane

class Enemy(Plane):
  def __init__(self, spritesheet_filename, width, height, rows, columns, speed_h, speed_v):
    # Call the parent class (Plane) constructor
    Plane.__init__(self, spritesheet_filename, width, height, rows, columns, speed_h, speed_v)

    self.direction = -1

  def update(self):
    if (self.direction == 1):
      self.move_right()
      screen_width = pygame.display.get_surface().get_width()
      sprite_width = self.image.get_width()
      if self.rect.x >= screen_width - sprite_width:
        self.change_direction()
    elif (self.direction == -1):
      self.move_left()
      if (self.rect.x == 0):
        self.change_direction()

  def change_direction(self):
    self.direction = self.direction * -1