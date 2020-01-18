import json

from data.abstractions.locations import ABCLocationData, ABCExitsData
from data.jsonrepo.character import CharacterData
from data.jsonrepo.objects import ObjectData

__all__ = ['LocationData']


class LocationData(ABCLocationData):
    __exits = None
    __characters = None
    __objects = None

    def __init__(self, location_id, **kwargs):
        self.__coordinates = location_id

        self.__exits = ExitsData(kwargs.get('exits', {}))

        self.__characters = [CharacterData(self.location_id, **character) for character in kwargs.get('characters', [])]
        self.__objects = kwargs.get('objects', [])

    def add_character(self, character):
        if isinstance(character, CharacterData):
            self.characters.append(character)

    def add_object(self, obj):
        if isinstance(obj, ObjectData):
            self.objects.append(obj)

    def remove_character(self, character):
        self.characters.remove(character)

    def remove_object(self, obj):
        self.objects.remove(obj)

    @property
    def location_id(self):
        return self.__coordinates

    @property
    def characters(self):
        return self.__characters

    @property
    def objects(self):
        return self.__objects

    @property
    def exits(self):
        return self.__exits

    # @exits.setter
    # def exits(self, value):
    #     if isinstance(value, dict) and {'left', 'right', 'up', 'down'} == set(value.keys()):
    #         self.__exits = value

    def dump(self):
        return {
            "location_id": self.location_id,
            'exits': self.exits.dump(),
            'characters': [character.dump() for character in self.characters],
            'objects': [obj.dump() for obj in self.objects]
        }

    def load(self):
        pass


class ExitsData(ABCExitsData):
    def __init__(self, exits):
        self.__left = exits.get("left", False)
        self.__right = exits.get("right", False)
        self.__down = exits.get("down", False)
        self.__up = exits.get("up", False)

    @property
    def down(self):
        return self.__down

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right

    @property
    def up(self):
        return self.__up

    def dump(self):
        return {
            "left": self.left,
            "right": self.right,
            "up": self.up,
            "down": self.down
        }
