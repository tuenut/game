from abstractions.data import ABCData

from app.data.orm.locations.models import Location


class LocationsDataController(ABCData):
    def load(self, data: dict):
        raise NotImplementedError

    def dump(self) -> list:
        return [location.dump() for location in self.locations]

    def __init__(self):
        self.locations = Location.objects.all()
