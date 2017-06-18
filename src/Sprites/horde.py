"""
Class responsible for generation of horde of airplanes in formations.
"""
import random
import pygame
from constants import Constants
from constants import Layer
from src.exceptions import FormationEnd
from .enemy import Enemy


class Horde:
    """
    Horde of airplanes
    """
    def __init__(self, renderables, formation, interval=450):
        """It creates hordes of enemies

        :param renderables:
        :param formation:
        :param interval:
        """
        self.interval = interval
        self.active = None
        self.current_line = None
        self.renderables = renderables
        self.formation = formation
        self.columns = len(Constants.FORMATIONS[self.formation][0])
        self.rows = len(Constants.FORMATIONS[self.formation])
        self.column_size = pygame.display.get_surface().get_width() / \
            self.columns

    def activate(self):
        """Activate horde generation mode

        :return: None
        """
        self.active = True
        self.current_line = self.rows - 1

    def deactivate(self):
        """De-activate horde generation

        :return: None
        """
        self.active = False
        self.current_line = self.rows - 1

    def render_line(self):
        """Render each line of the chosen formation

        :return:
        """
        try:
            map_line = Constants.FORMATIONS[self.formation][self.current_line]
            for pos, plane in enumerate(map_line):
                if plane:
                    # Enemy(width, height, rows, columns, speed_h, speed_v,
                    #       cooldown, hit_points, x=0, y=0)
                    enemy = Enemy(0, 2, 10, 20)
                    enemy.rect.x = self.column_size * pos + \
                        (enemy.rect.width / 2)
                    enemy.rect.y = 0
                    pygame.time.set_timer(pygame.USEREVENT + self.current_line,
                                          random.randint(1000, 3000))
                    self.renderables.add(enemy, layer=Layer.ENEMIES)
            self.current_line -= 1
            if self.current_line < 0:
                raise IndexError
        except IndexError:
            raise FormationEnd

    # Create boss
    # Enemy(spritesheet_filename, width, height, rows,
    #       columns, speed_h, speed_v, cooldown, hit_points)
    # boss_plane = Boss('boss.png', 157, 135, 1, 1, 1, .3, 0, 500)
    # boss_plane.rect.x = pygame.display.get_surface().get_width() / 2
    # boss_plane.rect.y = 200
    # pygame.time.set_timer(pygame.USEREVENT + 5, 5000)
    # # Add enemy plane to sprite list
    # renderables.add(boss_plane, layer=Layer.ENEMIES)
