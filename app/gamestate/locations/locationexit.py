from __future__ import annotations

from abstractions.gamestate import ABCGameStateLocationExit
from config import WEST, EAST, NORTH, SOUTH


class LocationExitsManager:
    def __init__(self, location_exits: dict):
        self.__exit_on_north = LocationExitState(self, **location_exits[NORTH])
        self.__exit_on_south = LocationExitState(self, **location_exits[SOUTH])
        self.__exit_on_west = LocationExitState(self, **location_exits[WEST])
        self.__exit_on_east = LocationExitState(self, **location_exits[EAST])

    @property
    def north(self):
        # todo; проверить, что в последней версии pycharm тоже не резолвится как сабкласс
        return self.__exit_on_north

    @property
    def south(self):
        return self.__exit_on_south

    @property
    def west(self):
        return self.__exit_on_west

    @property
    def east(self):
        return self.__exit_on_east

    def update(self):
        raise NotImplementedError


class LocationExitState(ABCGameStateLocationExit):
    def __init__(self, parent, next_location, access: bool, *args, **kwargs):
        self.__parent = parent
        self.__next_location = next_location
        self.__access = access

    @property
    def next_location(self):
        return self.__next_location if self.access else None

    @property
    def access(self) -> bool:
        return self.__access

    @property
    def location(self):
        return self.__parent

    @property
    def size(self):
        raise NotImplementedError

    @property
    def name(self) -> str:
        raise NotImplementedError

    @property
    def type(self) -> str:
        raise NotImplementedError

    @property
    def id(self) -> str:
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def position(self):
        raise NotImplementedError

    def __repr__(self):
        return "<ExitState from {parent} to {next_location}, accessible is {access} >".format(
            parent=self.location,
            next_location=self.next_location,
            access=self.access
        )

    __str__ = __repr__
