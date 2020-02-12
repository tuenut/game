import logging
import pygame  # type: ignore

from config import CELL_SIZE, EXIT_HEIGHT, EXIT_WIDTH, COLOR_EXIT_ACCESSIBLE, COLOR_EXIT_INACCESSIBLE


class LocationExitsRender:
    logger = logging.getLogger(__name__)

    def __init__(self, parent_surface, exits):
        self.parent_surface = parent_surface

        self.__exits = exits

        self.south = self.draw_exit(self.__south_exit)
        self.west = self.draw_exit(self.__west_exit)
        self.east = self.draw_exit(self.__east_exit)
        self.north = self.draw_exit(self.__north_exit)

    def draw_exit(self, params):
        try:
            return pygame.draw.rect(self.parent_surface, *params)
        except:
            self.logger.exception("Exception while render exits.")

    @property
    def __south_exit(self):
        x = int((CELL_SIZE - EXIT_WIDTH) / 2)
        y = CELL_SIZE - EXIT_HEIGHT / 2
        width = EXIT_WIDTH
        height = EXIT_HEIGHT
        color = COLOR_EXIT_ACCESSIBLE if self.__exits.south.access else COLOR_EXIT_INACCESSIBLE

        return color, (x, y, width, height)

    @property
    def __west_exit(self):
        x = -EXIT_HEIGHT / 2
        y = int((CELL_SIZE - EXIT_WIDTH) / 2)
        width = EXIT_HEIGHT
        height = EXIT_WIDTH
        color = COLOR_EXIT_ACCESSIBLE if self.__exits.west.access else COLOR_EXIT_INACCESSIBLE

        return color, (x, y, width, height,)

    @property
    def __east_exit(self):
        x = CELL_SIZE - EXIT_HEIGHT / 2
        y = int((CELL_SIZE - EXIT_WIDTH) / 2)
        width = EXIT_HEIGHT
        height = EXIT_WIDTH
        color = COLOR_EXIT_ACCESSIBLE if self.__exits.east.access else COLOR_EXIT_INACCESSIBLE

        return color, (x, y, width, height,)

    @property
    def __north_exit(self):
        x = int((CELL_SIZE - EXIT_WIDTH) / 2)
        y = -EXIT_HEIGHT / 2
        width = EXIT_WIDTH
        height = EXIT_HEIGHT
        color = COLOR_EXIT_ACCESSIBLE if self.__exits.north.access else COLOR_EXIT_INACCESSIBLE

        return color, (x, y, width, height,)
