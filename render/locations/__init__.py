import logging

from render.locations.locationobject import LocationRender

logger = logging.getLogger(__name__)


class LocationsRenderManager:
    def __init__(self, parent_surface, locations_objects):
        self.parent_surface = parent_surface
        self.__locations_state = locations_objects
        self.locations = []

        self.__init_draw()

    def __init_draw(self):
        for location in self.__locations_state:
            x = location.coordinates[0]
            y = location.coordinates[1]

            location_cell = LocationRender(self.parent_surface, location, x_cell=x, y_cell=y)
            location_cell.blit()

            self.locations.append(location_cell)

    def update(self):
        for location in self.locations:
            location.update()
