"""
Map module that creates hordes of airplanes
"""
import random
from constants import Constants
from src.exceptions import LevelFinished
from src.Sprites.horde import Horde


class Map:
    """Map class

    """
    def __init__(self, renderables):
        """It creates map object that contains hordes of airplanes

        :param renderables:
        """
        self.active = False
        self.horde_list = []
        for _ in range(20):
            self.horde_list.append(
                Horde(renderables, random.choice(
                    list(Constants.FORMATIONS.keys()))
                     )
            )
        self.hordes = iter(self.horde_list)

    def start(self):
        """Start the map

        :return:
        """
        self.active = True

    def pause(self):
        """Pauses the generation of hordes

        :return:
        """
        self.active = False

    def next_horde(self):
        """Return the next horde in map

        :return:
        """
        try:
            return self.hordes.__next__()
        except StopIteration:
            raise LevelFinished
