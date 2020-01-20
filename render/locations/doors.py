import logging
import pygame


logger = logging.getLogger(__name__)


class LocationExitsRender:
    color_exit_accesible = (200, 200, 200)
    color_exit_inaccessible = (50, 50, 50)

    def __init__(self, surface, exits, cell_size, door_width, door_height):
        self.surface = surface

        self.__exits = exits
        self.__width = door_width
        self.__height = door_height
        self.__cell_size = cell_size

        self.south = self.draw_exit(self.__south_exit)
        self.west = self.draw_exit(self.__west_exit)
        self.east = self.draw_exit(self.__east_exit)
        self.north = self.draw_exit(self.__north_exit)

    def draw_exit(self, params):
        try:
            return pygame.draw.rect(self.surface, *params)
        except:
            logger.exception("Exception while render exits.")

    @property
    def __south_exit(self):
        x = self.__height
        y = self.__cell_size - self.__height
        width = self.__width
        height = self.__height
        color = self.color_exit_accesible if self.__exits.get("south").access else self.color_exit_inaccessible

        return color, (x, y, width, height)

    @property
    def __west_exit(self):
        x = 0
        y = self.__height
        width = self.__height
        height = self.__width
        color = self.color_exit_accesible if self.__exits.get("west").access else self.color_exit_inaccessible

        return color, (x, y, width, height,)

    @property
    def __east_exit(self):
        x = self.__cell_size - self.__height
        y = self.__height
        width = self.__height
        height = self.__width
        color = self.color_exit_accesible if self.__exits.get("east").access else self.color_exit_inaccessible

        return color, (x, y, width, height,)

    @property
    def __north_exit(self):
        x = self.__height
        y = 0
        width = self.__width
        height = self.__height
        color = self.color_exit_accesible if self.__exits.get("north").access else self.color_exit_inaccessible

        return color, (x, y, width, height,)

