import pygame



class ArcadeFont(pygame.font.Font):
  # Basic colors
  WHITE = (255, 255, 255)
  BLACK = (0, 0, 0)

  def __init__(self, font_size):
    pygame.font.Font.__init__(self, 'resources/Arcade Classic.ttf', font_size)
    #pygame.font.Font.__init__('resources/Arcade Classic.ttf', 20)

  def get_text(self, text, color):
    return self.render(text, False, color)
