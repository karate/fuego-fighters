import pygame

class Explosion(pygame.sprite.Sprite):

  # Constructor. Pass in three images of the plane
  def __init__(self):
    # Call the parent class (Sprite) constructor
    pygame.sprite.Sprite.__init__(self)

    # Load sprite sheet
    sprite_sheet = pygame.image.load("resources/explosion.png").convert_alpha()

    self.width = 64
    self.height = 64
    self.image_index = 0
    self.timer = 0
    self.animation_delay = 2

    # extract images
    self.images = []
    for j in range(3):
      for i in range(8):
        # Rect(left, top, width, height)
        print(i*self.width, j*self.height, self.width, self.height)
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
