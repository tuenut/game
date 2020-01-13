from universe.location.properties import LocationPropertiesMixin


class Location(LocationPropertiesMixin):
    """Класс для хранения состояния ячейки мира"""

    def __init__(self, coordinates=None, exits=None, objects=None, characters=None):
        self._coordinates = coordinates
        self._down = exits['down']
        self._left = exits['left']
        self._right = exits['right']
        self._up = exits['up']

        self._objects_on_location = objects if isinstance(objects, list) else []
        self._characters_on_location = characters if isinstance(characters, list) else []

    def add_object(self, obj):
        self._objects_on_location.append(obj)

    def remove_object(self, obj):
        try:
            self._objects_on_location.remove(obj)
        except ValueError:
            return None
        else:
            return obj

    def __repr__(self):
        return "<loc %s>" % str([int(e) for e in self.exits])

    __str__ = __repr__