import logging

from app.mainfunctions.logger import pp
from data.abstractions.locations import ABCLocationData, ExitData

logger = logging.getLogger(__name__)

__all__ = ['LocationData']


class LocationData(ABCLocationData):
    __characters = None
    __objects = None

    def __init__(self, **kwargs):
        self.__id = kwargs.get('id')
        self.__coordinates = kwargs.get('coordinates')

        exits = kwargs.get('exits', {})
        self.__location_on_south = ExitData(**exits.get('south'))
        self.__location_on_west = ExitData(**exits.get('west'))
        self.__location_on_east = ExitData(**exits.get('east'))
        self.__location_on_north = ExitData(**exits.get('north'))

        self.__characters = kwargs.get('characters', [])
        self.__objects = kwargs.get('objects', [])

    @property
    def id(self):
        return self.__id

    @property
    def coordinates(self):
        return self.__coordinates

    @property
    def characters(self):
        return self.__characters

    @property
    def objects(self):
        return self.__objects

    @property
    def location_on_south(self):
        return self.__location_on_south

    @property
    def location_on_west(self):
        return self.__location_on_west

    @property
    def location_on_east(self):
        return self.__location_on_east

    @property
    def location_on_north(self):
        return self.__location_on_north

    def dump(self):
        return {
            "id": self.id,
            'exits': {
                "west": self.location_on_west.dump(),
                "east": self.location_on_east.dump(),
                "north": self.location_on_north.dump(),
                "south": self.location_on_south.dump()
            },
            'characters': self.characters,
            'objects': self.objects,
            "coordinates": self.coordinates
        }

    def load(self, data):
        raise NotImplementedError
