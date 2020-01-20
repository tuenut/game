# todo пересмотреть методы поиска локации по координатам и по id. Прийти к унифицированному методу.
# т.к. координаты и id по сути являются идентификатором, просто найти способ строить карту локаций
#  не зависимо от типа идентификатора
from abc import ABC, ABCMeta, abstractmethod
from .base import ABCDataObject
from .objects import ABCCharacterData

__all__ = ['ABCData', 'PLAYABLE_CHARACTER', 'CHARACTER_TYPES', 'WEST', 'EAST', 'NORTH', 'SOUTH', 'DIRECTIONS']

PLAYABLE_CHARACTER = "player"
CHARACTER_TYPES = (PLAYABLE_CHARACTER, )
WEST = 'west'
EAST = 'east'
NORTH = 'north'
SOUTH = 'south'
DIRECTIONS = [WEST, EAST, NORTH, SOUTH]


class ABCData(ABCDataObject, metaclass=ABCMeta):
    """Get data from source and create objects data instances to build data structure."""

    @property
    def data_fields(self):
        raise NotImplementedError

    @abstractmethod
    def get_location(self, location_id):
        ...

    @abstractmethod
    def get_all_locations(self,):
        ...

    @abstractmethod
    def get_character(self, character_id):
        """

        Parameters
        ----------
        character_id

        Returns
        -------
            character_data_object : ABCCharacterData
        """
        ...

    @abstractmethod
    def get_all_characters(self):
        ...

    @abstractmethod
    def get_object(self, obj_id):
        ...


