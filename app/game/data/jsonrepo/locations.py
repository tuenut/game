import logging

from abstractions.data import ABCDataLocation
from abstractions.data.objects import ABCDataExit

logger = logging.getLogger(__name__)

__all__ = ['LocationData']


class LocationData(ABCDataLocation):
    __characters = None
    __objects = None

    def __init__(self, **kwargs):
        self.__id = kwargs.get('id')
        self.__coordinates = kwargs.get('coordinates')
        self.__size = kwargs.get('size')

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
    def size(self):
        return self.__size

    @property
    def type(self):
        raise NotImplementedError

    @property
    def name(self):
        raise NotImplementedError

    @property
    def position(self):
        return self.__coordinates

    @property
    def characters(self):
        return self.__characters

    @property
    def objects(self):
        return self.__objects

    @property
    def exit_on_south(self):
        return self.__location_on_south

    @property
    def exit_on_west(self):
        return self.__location_on_west

    @property
    def exit_on_east(self):
        return self.__location_on_east

    @property
    def exit_on_north(self):
        return self.__location_on_north

    def dump(self):
        return {
            "id": self.id,
            'exits': {
                "west": self.exit_on_west.dump(),
                "east": self.exit_on_east.dump(),
                "north": self.exit_on_north.dump(),
                "south": self.exit_on_south.dump()
            },
            'characters': self.characters,
            'objects': self.objects,
            "coordinates": self.position,
            "size": self.size
        }

    def load(self, data):
        raise NotImplementedError


class ExitData(ABCDataExit):
    @property
    def sirializing_fields(self):
        raise NotImplementedError

    def __init__(self, access, location_id):
        self.__access = bool(access)
        self.__location = location_id

    @property
    def id(self):
        raise NotImplementedError

    @property
    def type(self):
        raise NotImplementedError

    @property
    def name(self):
        raise NotImplementedError

    @property
    def next_location(self):
        return self.__location

    @property
    def accessible(self):
        return self.__access

    def dump(self):
        return {
            "location_id": self.next_location,
            "access": self.accessible
        }

    def load(self, data):
        raise NotImplementedError
