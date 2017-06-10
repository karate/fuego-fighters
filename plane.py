import pygame
from sprite import Sprite
from bullet import Bullet

class Plane(Sprite):

  hit_points = 100

  # Constructor. Pass in three images of the plane
  def __init__(self, spritesheet_filename, width, height, rows, columns, speed_h, speed_v, cooldown):
    # Call the parent class (Sprite) constructor
    Sprite.__init__(self, spritesheet_filename, width, height, rows, columns)

    # Spritesheet must contain 3 sprites, with the following order
    self.image_left = self.images[0]
    self.image_top = self.images[1]
    self.image_right = self.images[2]
    self.speed_h = speed_h
    self.speed_v = speed_v
    self.last_fire = pygame.time.get_ticks()
    self.cooldown = cooldown
    # This variable get True when the player releases the fire button,
    # so we can reduce the cooldown temporary
    self.keyup = False

    # Set initial sprite
    self.image = self.image_top

    # Fetch the rectangle object that has the dimensions of the image
    # Update the position of this object by setting the values of rect.x and rect.y
    self.rect = self.image.get_rect()

  def fire(self):
    # Calculate the last time the gun fired
    now = pygame.time.get_ticks()
    cd = self.cooldown

    # If meanwhile the player has released the fire button,
    # reduce the cooldown to half.
    if self.keyup:
      cd = cd /2

    # If the cooldown has expired, fire the canons!
    # (aka: create a Bullet object)
    if now - self.last_fire >= cd:
      self.last_fire = now
      self.keyup = False
      bullet = Bullet('single_bullet.png', 8, 13, 1, 1, 6)
      bullet.rect.x = self.rect.x + (self.rect.width / 2)
      bullet.rect.y = self.rect.y - 10
      return bullet

  # Remember that the player has released the fire button,
  # so we can reduce the cooldown
  def reset_weapon_colldown(self):
    self.keyup = True

  # Reset sprite to image_top
  def reset_sprite(self):
    self.image = self.image_top

  # Basic movement
  def move_left(self):
    # Change sprite
    self.image = self.image_left
    # Move left
    self.rect.x -= self.speed_h
    # Don't let it go off the borders
    if self.rect.x < 0:
      self.rect.x = 0
      # Return false if the plane has reached the border
      return False
    return True

  def move_right(self):
    # Change sprite
    self.image = self.image_right
    # Move right
    self.rect.x += self.speed_h
    # Don't let it go off the borders
    screen_width = pygame.display.get_surface().get_width()
    sprite_width = self.image.get_width()
    if self.rect.x > screen_width - sprite_width:
      self.rect.x = screen_width - sprite_width
      # Return false if the plane has reached the border
      return False
    return True

  def move_up(self):
    # Move up
    self.rect.y -= self.speed_v
    # Don't let it go off the borders
    if self.rect.y < 0:
      self.rect.y = 0

  def move_down(self):
    # Move down
    self.rect.y += self.speed_v
    # Don't let it go off the borders
    screen_height = pygame.display.get_surface().get_height()
    sprite_height = self.image.get_height()
    if self.rect.y > screen_height - sprite_height:
      self.rect.y = screen_height - sprite_height
