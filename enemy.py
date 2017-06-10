import pygame
from plane import Plane

class Enemy(Plane):
  def __init__(self, spritesheet_filename, width, height, rows, columns, speed_h, speed_v):
    # Call the parent class (Plane) constructor
    Plane.__init__(self, spritesheet_filename, width, height, rows, columns, speed_h, speed_v, 1000)

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