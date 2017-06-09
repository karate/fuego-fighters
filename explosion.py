import pygame

class Explosion(pygame.sprite.Sprite):

  # Constructor. Pass in three images of the plane
  def __init__(self, spritesheet_filename, rows, columns, width, height, delay):
    # Call the parent class (Sprite) constructor
    pygame.sprite.Sprite.__init__(self)

    # Load sprite sheet
    sprite_sheet = pygame.image.load('resources/' + spritesheet_filename).convert_alpha()

    self.width = width
    self.height = height
    self.image_index = 0
    self.timer = 0
    self.animation_delay = delay

    # extract images
    self.images = []
    for j in range(columns):
      for i in range(rows):
        # Rect(left, top, width, height)
        rect = pygame.Rect((i*self.width, j*self.height, self.width, self.height))
        self.image = pygame.Surface(rect.size).convert()
        self.image.set_colorkey(self.image.get_at((0,0)), pygame.RLEACCEL)
        self.image.blit(sprite_sheet, (0, 0), rect)
        self.images.append(self.image)

    self.rect = self.images[0].get_rect()
    self.image = self.images[0]

  def update(self):
    self.timer += 1
    if self.timer > self.animation_delay:
      self.timer = 0
      self.image_index += 1
      if self.image_index >= len(self.images):
          self.image_index = 0
      self.image = self.images[self.image_index]
