import logging

from app.render.fogofwar import FogOfWar
from app.render.locations import LocationsRenderManager
from app.render.characters import CharactersRenderManager


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


