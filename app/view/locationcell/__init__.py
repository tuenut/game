import pygame

from .doors import Doors
from app.view.characters.player import Player

# todo for development
from universe.repositories.dumb import PLAYER


class LocationCell:
    """Класс отвечает за отрисовку одной ячейки/локации на карте."""
    background = (100, 100, 100)

    cell_size = 62
    door_height = 8
    door_width = cell_size - 2 * door_height

    DEFAULT_EXITS_CONFIGURATION = (0, 0, 0, 0)  # (down, left, right, up)

    def __init__(self, content, x_pos=0, y_pos=0, ):
        self.__x_pos = x_pos
        self.__y_pos = y_pos

        self.__exits = content.get('exits', self.DEFAULT_EXITS_CONFIGURATION)
        self.__characters = content.get('characters')

        self.surface = pygame.Surface((self.cell_size, self.cell_size))
        self.surface = self.surface.convert()
        self.surface.fill(self.background)

        self.doors = Doors(self.surface, self.__exits, self.cell_size, self.door_width, self.door_height)

        if isinstance(self.__characters, (list, tuple)) and PLAYER in self.__characters:
            self.player = Player(self.surface, self.cell_size, self.door_height)

    def blit(self, background):
        """blit the Ball on the background"""
        background.blit(self.surface, (self.__x_pos, self.__y_pos))
