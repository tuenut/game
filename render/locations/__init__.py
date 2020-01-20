import pygame
import logging

from render.locations.doors import LocationExitsRender
from render.characters.player import PlayerRenderObject
from state.locations import LocationState
from data.abstractions import PLAYABLE_CHARACTER

logger = logging.getLogger(__name__)


class LocationRender:
    background = (100, 100, 100)

    cell_size = 62
    exit_height = 8
    exit_width = cell_size - 2 * exit_height

    def __init__(self, parent, location: LocationState, x_pos=0, y_pos=0, ):
        self.parent = parent

        self.__x_pos = x_pos
        self.__y_pos = y_pos

        self.__location_state = location

        self.__player_state = None
        self.player = None

        if self.__location_state.characters:
            logger.debug("Characters on location {}: {}".format(location.coordinates, self.__location_state.characters))

        self.draw()
        self.draw_characters()

    def blit(self,):
        """blit the Ball on the background"""
        self.parent.blit(self.surface, (self.__x_pos, self.__y_pos))

    def draw(self):
        self.surface = pygame.Surface((self.cell_size, self.cell_size))
        self.surface = self.surface.convert()
        self.surface.fill(self.background)
        self.exits = LocationExitsRender(
            self.surface, self.__location_state.exits, self.cell_size, self.exit_width, self.exit_height
        )

    def draw_characters(self):
        # todo что-то мутное с условиями, могут быть проблемы

        if self.__player_state is not None and self.__player_state not in self.__location_state.characters:
            logger.debug("Redraw location")
            self.__player_state = None
            self.player = None
            self.draw()

        for character in self.__location_state.characters:
            if character.type == PLAYABLE_CHARACTER:
                if self.__player_state != character:
                    logger.debug("Found player")
                    self.__player_state = character

                if not isinstance(self.player, PlayerRenderObject):
                    self.player = PlayerRenderObject(self.surface, self.cell_size, self.exit_height)

    def update(self):
        self.draw_characters()
        self.blit()


