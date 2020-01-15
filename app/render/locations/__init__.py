import pygame

from .doors import LocationExitsRenderObject
from app.render.characters.player import PlayerRenderObject


class LocationRenderObject:
    """Класс отвечает за отрисовку одной ячейки/локации на карте."""
    background = (100, 100, 100)

    cell_size = 62
    door_height = 8
    door_width = cell_size - 2 * door_height

    def __init__(self, location, x_pos=0, y_pos=0, ):
        self.__x_pos = x_pos
        self.__y_pos = y_pos

        self.__exits = location.exits
        self.__characters = location.characters

        self.surface = pygame.Surface((self.cell_size, self.cell_size))
        self.surface = self.surface.convert()
        self.surface.fill(self.background)

        self.exits = LocationExitsRenderObject(self.surface, self.__exits, self.cell_size, self.door_width, self.door_height)

        if self.__characters:
            self.player = PlayerRenderObject(self.surface, self.cell_size, self.door_height)

    def blit(self, background):
        """blit the Ball on the background"""
        background.blit(self.surface, (self.__x_pos, self.__y_pos))
