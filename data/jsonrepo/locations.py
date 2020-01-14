import json

from data.abstractions.location import ABCLocationRepository, ABCExitsRepository
from data.jsonrepo.character import CharacterRepository
from data.jsonrepo.objects import ObjectRepository

__all__ = ['LocationRepository']


class LocationRepository(ABCLocationRepository):
    __exits = None
    __characters = None
    __objects = None

    def __init__(self, coordinates, **kwargs):
        self.__exits = ExitsRepository(kwargs.get('exits'))
        self.__characters = [CharacterRepository(self, **character) for character in kwargs.get('characters', [])]
        self.__objects = kwargs.get('objects', [])
        self.__coordinates = coordinates

    def add_character(self, character):
        if isinstance(character, CharacterRepository):
            self.characters.append(character)

    def add_object(self, obj):
        if isinstance(obj, ObjectRepository):
            self.objects.append(obj)

    def remove_character(self, character):
        self.characters.remove(character)

    def remove_object(self, obj):
        self.objects.remove(obj)

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
    def exits(self):
        return self.__exits

    # @exits.setter
    # def exits(self, value):
    #     if isinstance(value, dict) and {'left', 'right', 'up', 'down'} == set(value.keys()):
    #         self.__exits = value

    def json(self):
        return json.loads(json.dumps({'exits': self.exits, 'characters': self.characters, 'objects': self.objects}))


class ExitsRepository(ABCExitsRepository):
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

    def __init__(self, exits):
        self.__left = exits.get("left", False)
        self.__right = exits.get("right", False)
        self.__down = exits.get("down", False)
        self.__up = exits.get("up", False)
