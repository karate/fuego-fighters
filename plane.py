import pygame

class Plane(pygame.sprite.Sprite):
  # Constructor. Pass in the color of the block,
  # and its x and y position
  speed_h = 5
  speed_v = 4
  hit_points = 100

  def __init__(self, image_top, image_left, image_right):
    # Call the parent class (Sprite) constructor
    pygame.sprite.Sprite.__init__(self)

    # Load sprites for the plane
    self.image_top = image_top
    self.image_right = image_right
    self.image_left = image_left

    # Set initial sprite
    self.image = self.image_top

    # Fetch the rectangle object that has the dimensions of the image
    # Update the position of this object by setting the values of rect.x and rect.y
    self.rect = self.image.get_rect()

  # Basinc movement
  def key_up(self):
    self.image = self.image_top

  def move_left(self):
    self.image = self.image_left
    self.rect.x -= self.speed_h
    if self.rect.x < 0:
      self.rect.x = 0

  def move_right(self):
    self.image = self.image_right
    screen_width = pygame.display.get_surface().get_width()
    sprite_width = self.image.get_width()
    self.rect.x += self.speed_h
    if self.rect.x > screen_width - sprite_width:
      self.rect.x = screen_width - sprite_width

  def move_up(self):
    self.rect.y -= self.speed_v
    if self.rect.y < 0:
      self.rect.y = 0
  
  def move_down(self):
    screen_height = pygame.display.get_surface().get_height()
    sprite_height = self.image.get_height()
    self.rect.y += self.speed_v
    if self.rect.y > screen_height - sprite_height:
      self.rect.y = screen_height - sprite_height