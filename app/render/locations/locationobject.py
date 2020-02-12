import logging
import pygame

from config import MAP_MARGIN_X, MAP_MARGIN_Y, COLOR_RENDER_BG, COLOR_LOCATION_BG
from abstractions.gamestate import ABCLocationGameState

logger = logging.getLogger(__name__)


class LocationRender:
    def __init__(self, parent_surface, location: ABCLocationGameState):
        self.parent_surface = parent_surface

        self.__location = location

        self.__player_state = None
        self.player = None

        if self.__location.characters:
            logger.debug("Characters on location {}: {}".format(location.position, self.__location.characters))

        self.draw()

    @property
    def x(self):
        return self.__location.position[0] * self.size_x + MAP_MARGIN_X

    @property
    def y(self):
        return self.__location.position[1] * self.size_y + MAP_MARGIN_Y

    @property
    def size_x(self):
        return self.__location.size[0]

    @property
    def size_y(self):
        return self.__location.size[1]

    def blit(self, ):
        """blit the Ball on the background"""
        self.parent_surface.blit(self.surface, (self.x, self.y))

    def draw(self):
        self.surface = pygame.Surface((self.size_x, self.size_y)).convert()
        self.surface.fill(COLOR_RENDER_BG)
        pygame.draw.rect(self.surface, COLOR_LOCATION_BG, (1, 1, self.size_x, self.size_y))
        # self.exits = LocationExitsRender(self.surface, self.__location.exits)

    def update(self):
        self.blit()
