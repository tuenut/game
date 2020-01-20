import logging
from state.abstractions import ABCGameState
from data.abstractions.locations import ABCLocationData
from data.abstractions import WEST, EAST, NORTH, SOUTH

logger = logging.getLogger(__name__)


class ExitState(ABCGameState):
    def __init__(self, parent, to, access: bool):
        self.parent = parent  # type: LocationState
        self.next_location = to  # type: LocationState or None
        self.access = access

    def update(self):
        raise NotImplementedError

    def __repr__(self):
        return "<Exit from {parent} to {next_location}, accessible is {access} >". \
            format(
            parent=self.parent.id if self.parent else self.parent,
            next_location=self.next_location.id if self.next_location else self.next_location,
            access=self.access
        )

    __str__ = __repr__


class LocationState(ABCGameState):
    """Класс для хранения состояния ячейки мира"""
    __exits_created = False

    def __init__(self, location: ABCLocationData, get_location, get_character):
        self.get_location = get_location
        self.get_character = get_character

        self.__location_data = location

        self._coordinates = self.__location_data.coordinates
        self.__id = self.__location_data.id
        self.__characters = self.__location_data.characters  # type: list

        self.__next_location_on_south = None
        self.__next_location_on_west = None
        self.__next_location_on_east = None
        self.__next_location_on_north = None

    def update(self):
        raise NotImplementedError

    def init_exits(self):
        """Call that method after all locations"""
        if not self.__exits_created:
            self.__init_south_exit()
            self.__init_west_exit()
            self.__init_east_exit()
            self.__init_north_exit()

            self.__exits_created = True

    def __init_south_exit(self):
        location = self.get_location(self.__location_data.location_on_south.location)
        access = self.__location_data.location_on_south.accessible
        self.__next_location_on_south = ExitState(self, location, access)

    def __init_west_exit(self):
        location = self.get_location(self.__location_data.location_on_west.location)
        access = self.__location_data.location_on_west.accessible
        self.__next_location_on_west = ExitState(self, location, access)

    def __init_east_exit(self):
        location = self.get_location(self.__location_data.location_on_east.location)
        access = self.__location_data.location_on_east.accessible
        self.__next_location_on_east = ExitState(self, location, access)

    def __init_north_exit(self):
        location = self.get_location(self.__location_data.location_on_north.location)
        access = self.__location_data.location_on_north.accessible
        self.__next_location_on_north = ExitState(self, location, access)

    def init_characters(self):
        characters = []
        for character_id in self.__characters:
            characters.append(self.get_character(character_id))

        self.__characters = characters

    @property
    def id(self):
        return self.__id

    @property
    def coordinates(self):
        return self._coordinates

    @property
    def next_location_on_south(self):
        return self.__next_location_on_south

    @property
    def next_location_on_west(self):
        return self.__next_location_on_west

    @property
    def next_location_on_east(self):
        return self.__next_location_on_east

    @property
    def next_location_on_north(self):
        return self.__next_location_on_north

    @property
    def exits(self):
        return {
            "south": self.next_location_on_south,
            "west": self.next_location_on_west,
            "east": self.next_location_on_east,
            "north": self.next_location_on_north
        }

    @property
    def objects(self):
        raise NotImplementedError

    @property
    def characters(self):
        return self.__characters

    def get_next_location(self, direction):
        """

        Parameters
        ----------
        direction

        Returns
        -------
            location: LocationState or None
        """
        if direction == WEST:
            return self.next_location_on_west.next_location if self.next_location_on_west.access else None
        elif direction == EAST:
            return self.next_location_on_east.next_location if self.next_location_on_east.access else None
        elif direction == NORTH:
            return self.next_location_on_north.next_location if self.next_location_on_north.access else None
        elif direction == SOUTH:
            return self.next_location_on_south.next_location if self.next_location_on_south.access else None
        else:
            return None

    def add_character(self, character_id):
        character = self.get_character(character_id)

        if character not in self.__characters:
            self.__characters.append(character)
            return character
        else:
            return None

    def remove_character(self, character_id):
        character = self.get_character(character_id)

        try:
            self.__characters.remove(character)
        except ValueError:
            return None
        else:
            return character

    def __repr__(self):
        return "<loc %s>" % str([e for e in self.exits])

    __str__ = __repr__
