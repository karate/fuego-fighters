from src.exceptions import LevelFinished
from .Sprites.horde import Horde


class Map:
    def __init__(self, renderables):
        self.active = False
        self.hordes = iter([Horde(renderables, '/'),
                            Horde(renderables, '/'),
                            Horde(renderables, '\\'),
                            Horde(renderables, 'z'),
                            Horde(renderables, 'v'),
                            Horde(renderables, 'dv'),
                            Horde(renderables, 'v')])

    def start(self):
        self.active = True

    def pause(self):
        self.active = False

    def next_horde(self):
        try:
            return self.hordes.__next__()
        except StopIteration:
            raise LevelFinished

