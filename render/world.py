from render.locations import LocationsRenderManager
from render.characters import CharactersRenderManager


class WorldRender:
    def __init__(self, parent_surface, locations, characters):
        self.surface = parent_surface

        self.locations = LocationsRenderManager(self.surface, locations_objects=locations)
        self.characters = CharactersRenderManager(self.surface, character_objects=characters)

    def update(self):
        self.locations.update()
        self.characters.update()