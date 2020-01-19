from data.abstractions.locations import ABCLocationData

__all__ = ['LocationData']


class LocationData(ABCLocationData):
    __exits = None
    __characters = None
    __objects = None

    def __init__(self, **kwargs):
        self.__id = kwargs.get('id')
        self.__coordinates = kwargs.get('coordinates')

        exits = kwargs.get('exits', {})
        self.__location_on_bottom = exits.get('down')
        self.__location_on_left = exits.get('left')
        self.__location_on_right = exits.get('right')
        self.__location_on_top = exits.get('up')

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
    def location_on_bottom(self):
        return self.__location_on_bottom

    @property
    def location_on_left(self):
        return self.__location_on_left

    @property
    def location_on_right(self):
        return self.__location_on_right

    @property
    def location_on_top(self):
        return self.__location_on_top

    def dump(self):
        return {
            "location_id": self.id,
            'exits': {
                "left": self.location_on_left,
                "right": self.location_on_right,
                "up": self.location_on_top,
                "down": self.location_on_bottom
            },
            'characters': self.characters,
            'objects': self.objects,
            "coordinates": self.coordinates
        }

    def load(self, data):
        raise NotImplementedError
