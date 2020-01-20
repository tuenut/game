import logging

from app.mainfunctions.logger import pp

from data.abstractions import WEST, EAST, NORTH, SOUTH
from state import ABCGameState, ABCGameStateObject
from state.characters.base import Character
from .locationexit import ExitState

logger = logging.getLogger(__name__)


class LocationState(ABCGameState):
    """Класс для хранения состояния ячейки мира"""
    __exits_created = False

    def __init__(self, location_data: dict):
        logger.debug("Init location with data:\n%s", pp.pformat(location_data))

        self.__location_data = location_data

        self._coordinates = self.__location_data.get('coordinates')
        self.__id = self.__location_data.get('id')
        self.__characters = self.__location_data.get('characters')  # type: list

        self.__next_location_on_south = None
        self.__next_location_on_west = None
        self.__next_location_on_east = None
        self.__next_location_on_north = None

    def update(self):
        raise NotImplementedError

    def init_exits(self, location_exits):
        """Call that method after all locations"""
        if not self.__exits_created:
            self.__next_location_on_south = ExitState(self, **location_exits[SOUTH])
            self.__next_location_on_west = ExitState(self, **location_exits[WEST])
            self.__next_location_on_east = ExitState(self, **location_exits[EAST])
            self.__next_location_on_north = ExitState(self, **location_exits[NORTH])

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
    def data(self):
        # todo: одно использование для инициализации выходов
        return self.__location_data

    @property
    def coordinates(self):
        return self._coordinates

    @property
    def exits(self):
        return {
            "south": self.__next_location_on_south,
            "west": self.__next_location_on_west,
            "east": self.__next_location_on_east,
            "north": self.__next_location_on_north
        }

    @property
    def objects(self):
        raise NotImplementedError

    @property
    def characters(self):
        return self.__characters

    def get_next_location(self, direction: str):
        """
        Returns
        -------
            location: LocationState or None
        """
        if direction == WEST:
            destination = self.__next_location_on_west.next_location if self.__next_location_on_west.access else None
        elif direction == EAST:
            destination = self.__next_location_on_east.next_location if self.__next_location_on_east.access else None
        elif direction == NORTH:
            destination = self.__next_location_on_north.next_location if self.__next_location_on_north.access else None
        elif direction == SOUTH:
            destination = self.__next_location_on_south.next_location if self.__next_location_on_south.access else None
        else:
            destination = None

        return destination

    def add_character(self, character: ABCGameStateObject):
        if character not in self.__characters:
            self.__characters.append(character)

            logger.debug("Character was added to location.")
            return character
        else:
            logger.debug("Unknown character object.")
            return None

    def remove_character(self, character: ABCGameStateObject):
        try:
            self.__characters.remove(character)
        except ValueError:
            logger.debug("Can't remove character from origin location.")

            return None
        else:
            logger.debug("Character was removed from location.")

            return character

    def move_object_to_next_location(self, obj: ABCGameStateObject, direction: str):
        if self.get_next_location(direction) is not None:
            self.get_next_location(direction).add_character(self.remove_character(obj))

    def __repr__(self):
        return "<LocationState %s>" % self.coordinates

    __str__ = __repr__
