import pygame

class Plane(pygame.sprite.Sprite):

  speed_h = 5
  speed_v = 4
  hit_points = 100

  # Constructor. Pass in three images of the plane
  def __init__(self, image_top_filename, image_left_filename = None, image_right_filename = None):
    # Call the parent class (Sprite) constructor
    pygame.sprite.Sprite.__init__(self)

    # Load sprites for the plane
    self.image_top = pygame.image.load('resources/' + image_top_filename).convert_alpha()

    # If image_left or image_right was not provided, use image_top instead
    if image_left_filename:
      self.image_left = pygame.image.load('resources/' + image_left_filename).convert_alpha()
    else:
      self.image_left = self.image_top

    if image_right_filename:
      self.image_right = pygame.image.load('resources/' + image_right_filename).convert_alpha()
    else:
      self.image_right = self.image_top

    # Set initial sprite
    self.image = self.image_top

    # Fetch the rectangle object that has the dimensions of the image
    # Update the position of this object by setting the values of rect.x and rect.y
    self.rect = self.image.get_rect()

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
