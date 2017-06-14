import pygame
from .enemy import Enemy
from constants import Constants
from constants import Layer


class Hordes:
    def __init__(self, renderables, formation, interval=300):
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
        self.column_width = len(Constants.FORMATIONS[self.formation][0])
        self.column_height = len(Constants.FORMATIONS[self.formation])
        self.column_size = pygame.display.get_surface().get_width() / (
            self.column_width * 50)

    def activate(self):
        """Activate horde generation mode

        :return: None
        """
        self.active = True
        self.current_line = self.column_height - 1

    def deactivate(self):
        """De-activate horde generation

        :return: None
        """
        self.active = False
        self.current_line = self.column_height - 1

    def render_line(self):
        try:
            map_line = Constants.FORMATIONS[self.formation][self.current_line]
            for pos, plane in enumerate(map_line):
                if plane:
                    # Enemy(width, height, rows, columns, speed_h, speed_v,
                    #       cooldown, hit_points, x, y)
                    x = self.column_size * pos * 50
                    self.renderables.add(Enemy(31, 42, 1, 5, 0, 3, 10, 20,
                                               int(x), 0), layer=Layer.ENEMIES)
            self.current_line -= 1
            if self.current_line < 0:
                raise IndexError
        except IndexError:
            self.deactivate()

    # Create boss
    # Enemy(spritesheet_filename, width, height, rows,
    #       columns, speed_h, speed_v, cooldown, hit_points)
    # boss_plane = Boss('boss.png', 157, 135, 1, 1, 1, .3, 0, 500)
    # boss_plane.rect.x = pygame.display.get_surface().get_width() / 2
    # boss_plane.rect.y = 200
    # pygame.time.set_timer(pygame.USEREVENT + 5, 5000)
    # # Add enemy plane to sprite list
    # renderables.add(boss_plane, layer=Layer.ENEMIES)

