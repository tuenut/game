import logging

import pygame

from abstractions.data import PLAYABLE_CHARACTER, NON_PLAYABLE_CHARACTER
from app.game.render.characters import PlayerRenderObject
from app.game.render.config import CELL_SIZE, FOG_OF_WAR


class FogOfWar:
    FOG_WIDTHS = {
        PLAYABLE_CHARACTER: int(CELL_SIZE * 2),
        NON_PLAYABLE_CHARACTER: int(CELL_SIZE / 3),
    }
    BACKGROUND = (0, 0, 0)
    ALPHA_COLOR = (255, 0, 255)

    logger = logging.getLogger(__name__)

    def __init__(self, parent_surface, characters):
        if not FOG_OF_WAR:
            self.ALPHA_COLOR = self.BACKGROUND

        self.__characters = characters
        self.parent_surface = parent_surface

        self.draw()

    def draw(self):
        self.surface = pygame.Surface(self.parent_surface.get_size()).convert()
        self.surface.fill(self.BACKGROUND)

        for character in self.__characters:
            center_postition = self.__get_center(character.location.coordinates)
            radius = self.FOG_WIDTHS[character.type]

            pygame.draw.circle(self.surface, self.ALPHA_COLOR, center_postition, radius)

        self.surface.set_colorkey(self.ALPHA_COLOR)
        self.surface = self.surface.convert_alpha()

    @staticmethod
    def __get_center(character_location_coordinates):
        character_position = PlayerRenderObject.get_coordinates(*character_location_coordinates)

        return tuple(map(lambda x: x + int(CELL_SIZE / 2), character_position))

    def blit(self):
        self.parent_surface.blit(self.surface, (0, 0))

    def update(self):
        self.blit()
        self.draw()
