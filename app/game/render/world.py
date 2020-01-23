import logging
import pygame

from abstractions.data import PLAYABLE_CHARACTER, NON_PLAYABLE_CHARACTER
from app.game.render.config import CELL_SIZE
from app.game.render.locations import LocationsRenderManager
from app.game.render.characters import CharactersRenderManager, PlayerRenderObject


class WorldRender:
    logger = logging.getLogger(__name__)

    def __init__(self, parent_surface, locations, characters):
        self.surface = parent_surface

        self.locations = LocationsRenderManager(self.surface, locations_objects=locations)
        self.characters = CharactersRenderManager(self.surface, character_objects=characters)
        self.fog = FogOfWar(self.surface, characters)

    def update(self):
        self.locations.update()
        self.characters.update()
        self.fog.update()


class FogOfWar:
    FOG_WIDTHS = {
        PLAYABLE_CHARACTER: int(CELL_SIZE * 2),
        NON_PLAYABLE_CHARACTER: int(CELL_SIZE / 3),
    }

    logger = logging.getLogger(__name__)

    def __init__(self, parent_surface, characters):
        self.__characters = characters
        self.parent_surface = parent_surface

        self.draw()

    def draw(self):
        self.surface = pygame.Surface(self.parent_surface.get_size()).convert()
        self.surface.fill((0, 0, 0))

        for character in self.__characters:
            coords = PlayerRenderObject.get_coordinates(*character.location.coordinates)
            coords = tuple(map(lambda x: x + int(CELL_SIZE / 2), coords))
            radius = self.FOG_WIDTHS[character.type]

            pygame.draw.circle(self.surface, (255, 0, 255), coords, radius)

        self.surface.set_colorkey((255, 0, 255))
        self.surface = self.surface.convert_alpha()

    def blit(self):
        self.parent_surface.blit(self.surface, (0, 0))

    def update(self):
        self.blit()
        self.draw()
