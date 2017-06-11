import pygame
from .plane import Plane
from .bullet import Bullet

class Enemy(Plane):
  def __init__(self, spritesheet_filename, width, height, rows, columns, speed_h, speed_v, cooldown, hit_points):
    # Call the parent class (Plane) constructor
    Plane.__init__(self, spritesheet_filename, width, height, rows, columns, speed_h, speed_v, cooldown, hit_points)

    self.direction = -1

  def update(self):
    # If current direction is right
    if (self.direction == 1):
      # Move right and check if the plane reached the edge
      if not self.move_right():
        # Change direction
        self.change_direction()
    # If current direction is left
    elif (self.direction == -1):
      # Move left and check if the plane reached the edge
      if not self.move_left():
        # Change direction
        self.change_direction()

  def change_direction(self):
    self.direction = self.direction * -1

  def fire(self):
      bullet = Bullet('enemy_bullet.png', 8, 13, 1, 1, 6, 1)
      bullet.rect.x = self.rect.x + (self.rect.width / 2)
      bullet.rect.y = self.rect.y - 10
      return bullet
