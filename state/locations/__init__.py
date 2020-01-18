from state.locations.properties import LocationPropertiesMixin
from state.character import PlayableCharacter
from state.abstractions import ABCGameStateObject
from data.abstractions.locations import ABCLocationData


class Location(ABCGameStateObject, LocationPropertiesMixin):
    """Класс для хранения состояния ячейки мира"""

    def __init__(self, location: ABCLocationData):
        self._coordinates = location.location_id
        self._down = location.exits.down
        self._left = location.exits.left
        self._right = location.exits.right
        self._up = location.exits.up

        self._objects_on_location = location.objects
        self.__init_characters(location.characters)

    def __init_characters(self, characters):
        self._characters_on_location = []

        for character in characters:
            if character.type == "player":
                character_object = PlayableCharacter(position=self.coordinates)
            else:
                continue

            self._characters_on_location.append(character_object)

    def update(self, *args, **kwargs):
        raise NotImplementedError

    def __repr__(self):
        return "<loc %s>" % str([int(e) for e in self.exits])

    __str__ = __repr__
