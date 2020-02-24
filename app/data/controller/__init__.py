from abstractions.data import ABCDataController

from app.data.controller.locations import LocationsDataController
from app.data.controller.objects import ObjectsDataController
from app.data.controller.characters import CharactersDataController


class DataController(ABCDataController):
    def __init__(self):
        self.__locations = LocationsDataController()
        self.__objects = ObjectsDataController()
        self.__characters = CharactersDataController()

    @property
    def locations(self):
        return self.__locations.dump()

    @property
    def objects(self):
        return self.__objects.dump()

    @property
    def characters(self):
        return self.__characters.dump()

    def load(self, data: dict):
        pass

    def dump(self) -> dict:
        pass
