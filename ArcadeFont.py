import pygame


class ArcadeFont(pygame.font.Font):
    def __init__(self, font_size):
        # Select the font to use, size, bold, italics
        # font = pygame.font.SysFont('Calibri', 40, False, False)
        # wpm_font = pygame.font.SysFont('Calibri', 15, False, False)

        pygame.font.Font.__init__(
            self, 'resources/Arcade Classic.ttf', font_size
        )

    def get_text(self, text, color):
        return self.render(text, False, color)
