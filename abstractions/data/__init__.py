from __future__ import annotations

from typing import List, Tuple, Optional, Union
from abc import ABCMeta, abstractmethod, ABC

PLAYABLE_CHARACTER = "player"
NON_PLAYABLE_CHARACTER = "npc"
CHARACTER_TYPES = (PLAYABLE_CHARACTER, NON_PLAYABLE_CHARACTER)
WEST = 'west'
EAST = 'east'
NORTH = 'north'
SOUTH = 'south'
DIRECTIONS = [WEST, EAST, NORTH, SOUTH]


class ABCData(ABC):
    @property
    @abstractmethod
    def data_fields(self):
        """Fields for data object dump()/load() methods."""
        return []

    @abstractmethod
    def load(self, data):
        """Load data to self."""
        ...

    def dump(self):
        """Serialize data from self to jsonable dict."""
        return {field: getattr(self, field) for field in self.data_fields}


class ABCDataController(ABCData, metaclass=ABCMeta):
    """Get data from source and create objects data instances to build data structure.

    Notes
    -----
    Uses only for get data from some sort of repositiry (`__init__`), provide it to next app layer (`dump`),
     and save it to repository when its needed, aka (`load`).
    """

    @property
    def data_fields(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def locations(self) -> List[ABCDataLocation]:
        ...

    @property
    @abstractmethod
    def objects(self) -> List[ABCDataObject]:
        ...

    @property
    @abstractmethod
    def characters(self) -> List[ABCDataCharacter]:
        ...

    @abstractmethod
    def get_location(self, location_id: str) -> ABCDataLocation:
        ...

    @abstractmethod
    def get_character(self, character_id: str) -> ABCDataCharacter:
        ...

    @abstractmethod
    def get_object(self, obj_id: str) -> ABCDataObject:
        ...

    @abstractmethod
    def dump(self) -> dict:
        ...

    @abstractmethod
    def load(self, data: dict):
        ...


class ABCDataEntity(ABCData, metaclass=ABCMeta):
    @property
    @abstractmethod
    def id(self) -> str:
        ...

    @property
    @abstractmethod
    def name(self):
        ...

    @property
    @abstractmethod
    def type(self):
        ...


class ABCDataLocation(ABCDataEntity, metaclass=ABCMeta):
    @property
    def data_fields(self):
        """Fields for data object dump()/load() methods."""
        return ["id", "objects", "characters", "position", "exits"]

    @property
    @abstractmethod
    def position(self) -> Tuple[int]:
        ...

    @property
    @abstractmethod
    def characters(self) -> list:
        ...

    @property
    @abstractmethod
    def objects(self) -> list:
        ...

    @property
    @abstractmethod
    def exit_on_south(self) -> ABCDataExit:
        ...

    @property
    @abstractmethod
    def exit_on_west(self) -> ABCDataExit:
        ...

    @property
    @abstractmethod
    def exit_on_east(self) -> ABCDataExit:
        ...

    @property
    @abstractmethod
    def exit_on_north(self) -> ABCDataExit:
        ...


class ABCDataExit(ABCDataEntity, metaclass=ABCMeta):
    @property
    @abstractmethod
    def next_location(self):
        ...

    @property
    @abstractmethod
    def accessible(self):
        ...


class ABCDataObject(ABCDataEntity, metaclass=ABCMeta):
    @property
    def data_fields(self):
        """Fields for data object dump()/load() methods."""
        return ["name", "type", "location", "id"]

    @property
    @abstractmethod
    def location(self) -> Optional[ABCDataLocation]:
        ...


class ABCDataCharacter(ABCDataObject, metaclass=ABCMeta):
    @property
    def data_fields(self):
        return ["name", "type", "location", "id"]
