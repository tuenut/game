from __future__ import annotations

import logging

from typing import List, Mapping, Dict, Any, Union, Optional, Tuple

from app.mainfunctions.logger import pp

from abstractions.data import WEST, EAST, NORTH, SOUTH
from abstractions.gamestate import ABCGameStateLocation, ABCGameStateObject
from state.characters.base import Character
from .locationexit import LocationExitsManager

logger = logging.getLogger(__name__)


class LocationState(ABCGameStateLocation):
    """Класс для хранения состояния ячейки мира"""
    __exits_created = False

    def __init__(self, location_data):
        logger.debug("Init location with data:\n%s", pp.pformat(location_data))

        self.__location_data = location_data

        self.__get_id()
        self.__get_coordinates()

        self.__characters = self.__location_data['characters'] # type: list

    def __get_id(self):
        _id = self.__location_data['id']
        if isinstance(_id, str):
            self.__id = _id # type: str

    def __get_coordinates(self):
        coordinates = self.__location_data['coordinates']
        if len(coordinates) != 2 or isinstance(coordinates, (tuple, list)):
            raise TypeError("Wrong coordinates %s for location %s" % (coordinates, self.id))
        else:
            self.__coordinates = tuple(self.__location_data['coordinates']) # type: Tuple[int, int]


    def update(self):
        raise NotImplementedError

    def init_exits(self, location_exits):
        """Call that method after all locations"""
        if not self.__exits_created:
            self.__exits = LocationExitsManager(location_exits)
            self.__exits_created = True

    def init_characters(self):
        self.__characters = [
            character
            for character in self.__characters
            if issubclass(character.__class__, Character)
        ]

    @property
    def id(self):
        return self.__id

    @property
    def type(self):
        raise NotImplementedError

    @property
    def name(self):
        raise NotImplementedError

    @property
    def data(self) -> dict:
        # todo: одно использование для инициализации выходов
        return self.__location_data

    @property
    def coordinates(self):
        return self.__coordinates

    @property
    def exits(self):
        return self.__exits

    @property
    def objects(self):
        raise NotImplementedError

    @property
    def characters(self):
        return self.__characters

    def get_next_location(self, direction):
        if direction == WEST:
            destination = self.exits.west.next_location
        elif direction == EAST:
            destination = self.exits.east.next_location
        elif direction == NORTH:
            destination = self.exits.north.next_location
        elif direction == SOUTH:
            destination = self.exits.south.next_location
        else:
            destination = None

        return destination

    def add_object(self, character):
        if character not in self.__characters:
            self.__characters.append(character)

            logger.debug("Character was added to location.")
            return character
        else:
            logger.debug("Unknown character object.")
            return None

    def remove_object(self, character):
        try:
            self.__characters.remove(character)
        except ValueError:
            logger.debug("Can't remove character from origin location.")

            return None
        else:
            logger.debug("Character was removed from location.")

            return character

    def move_object_to_next_location(self, obj, direction):
        try:
            self.get_next_location(direction).add_object(self.remove_object(obj))
        except AttributeError:
            logger.exception("Next location is None.")

    def __repr__(self):
        return "<LocationState %s>" % self.coordinates

    __str__ = __repr__
