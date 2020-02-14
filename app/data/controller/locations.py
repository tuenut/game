from abstractions.data import ABCData

from app.data.models import Location
from app.data.models.bases import database


class LocationsDataController(ABCData):
    def load(self, data: dict):
        raise NotImplementedError

    def dump(self) -> list:
        return [location.dump() for location in self.locations]

    @database.connection_context()
    def __init__(self):
        self.locations = Location.select()
