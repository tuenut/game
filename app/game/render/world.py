import logging

from app.game.render.fogofwar import FogOfWar
from app.game.render.locations import LocationsRenderManager
from app.game.render.characters import CharactersRenderManager


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


