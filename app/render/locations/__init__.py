import logging

from abstractions.gamestate import ABCGameStateLocationsManager
from app.render.locations.locationobject import LocationRender

logger = logging.getLogger(__name__)


class LocationsRenderManager:
    def __init__(self, parent_surface, locations_objects: ABCGameStateLocationsManager):
        self.parent_surface = parent_surface
        self.__locations_state = locations_objects
        self.locations = []

        self.__init_draw()

    def __init_draw(self):
        for location in self.__locations_state:
            self.locations.append(LocationRender(self.parent_surface, location))

    def update(self):
        for location in self.locations:
            location.update()
