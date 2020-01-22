import logging
import pygame

from render.config import CELL_SIZE, CELL_BORDER, MAP_MARGIN_X, MAP_MARGIN_Y, EXIT_WIDTH, EXIT_HEIGHT
from render.locations.exitsobject import LocationExitsRender
from state.universe.locations.locationobject import LocationState

logger = logging.getLogger(__name__)


class LocationRender:
    BACKGROUND = (100, 100, 100)

    def __init__(self, parent_surface, location: LocationState, x_cell=0, y_cell=0, ):
        self.parent_surface = parent_surface

        self.__x_cell = x_cell
        self.__y_cell = y_cell

        self.__x_pos = self.__x_cell * (CELL_SIZE + CELL_BORDER) + MAP_MARGIN_X
        self.__y_pos = self.__y_cell * (CELL_SIZE + CELL_BORDER) + MAP_MARGIN_Y

        self.__location_state = location

        self.__player_state = None
        self.player = None

        if self.__location_state.characters:
            logger.debug("Characters on location {}: {}".format(location.coordinates, self.__location_state.characters))

        self.draw()
        # self.draw_characters()

    def blit(self, ):
        """blit the Ball on the background"""
        self.parent_surface.blit(self.surface, (self.__x_pos, self.__y_pos))

    def draw(self):
        self.surface = pygame.Surface((CELL_SIZE, CELL_SIZE)).convert()
        self.surface.fill(self.BACKGROUND)
        self.exits = LocationExitsRender(
            self.surface, self.__location_state.exits, CELL_SIZE, EXIT_WIDTH, EXIT_HEIGHT
        )

    def update(self):
        self.blit()