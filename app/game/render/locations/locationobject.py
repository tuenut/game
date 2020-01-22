import logging
import pygame

from app.game.render.config import CELL_SIZE, CELL_BORDER, MAP_MARGIN_X, MAP_MARGIN_Y, EXIT_WIDTH, EXIT_HEIGHT
from app.game.render.locations.exitsobject import LocationExitsRender
from abstractions.gamestate import ABCGameStateLocation

logger = logging.getLogger(__name__)


class LocationRender:
    BACKGROUND = (100, 100, 100)

    def __init__(self, parent_surface, location: ABCGameStateLocation):
        self.parent_surface = parent_surface

        self.__location = location

        self.__player_state = None
        self.player = None

        if self.__location.characters:
            logger.debug("Characters on location {}: {}".format(location.coordinates, self.__location.characters))

        self.draw()

    @property
    def x(self):
        return self.__location.coordinates[0] * (CELL_SIZE + CELL_BORDER) + MAP_MARGIN_X

    @property
    def y(self):
        return self.__location.coordinates[1] * (CELL_SIZE + CELL_BORDER) + MAP_MARGIN_Y


    def blit(self, ):
        """blit the Ball on the background"""
        self.parent_surface.blit(self.surface, (self.x, self.y))

    def draw(self):
        self.surface = pygame.Surface((CELL_SIZE, CELL_SIZE)).convert()
        self.surface.fill(self.BACKGROUND)
        self.exits = LocationExitsRender(
            self.surface, self.__location.exits, CELL_SIZE, EXIT_WIDTH, EXIT_HEIGHT
        )

    def update(self):
        self.blit()