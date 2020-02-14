from __future__ import annotations

from abc import ABC, abstractmethod, ABCMeta
from typing import List, Tuple, Optional

from abstractions.bases import ABCNonPlayableCharacter, ABCPlayableCharacter, ABCLocation, ABCObject, \
    ABCLocationJunction, ABCEntity, ABCCharacter

__all__ = [
    'ABCData', 'ABCNonPlayableCharacterData', 'ABCPlayableCharacterData', 'ABCInGameObjectData', 'ABCLocationData',
    'ABCLocationJunctionData', 'ABCDataController', 'ABCEntityData', 'ABCCharacterData'
]


class ABCData(ABC):
    @abstractmethod
    def load(self, data: dict):
        """Load data to self."""
        ...

    @abstractmethod
    def dump(self) -> dict:
        """Serialize data from self to jsonable dict."""
        ...


class ABCEntityData(ABCEntity, ABCData, metaclass=ABCMeta):
    @property
    @abstractmethod
    def uuid(self) -> str:
        ...

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    @abstractmethod
    def type(self) -> str:
        ...

    @abstractmethod
    def load(self, data: dict):
        ...

    @abstractmethod
    def dump(self) -> dict:
        ...


class ABCCharacterData(ABCCharacter, ABCEntityData, metaclass=ABCMeta):
    @property
    @abstractmethod
    def location(self) -> Optional[ABCLocation]:
        ...

    @property
    @abstractmethod
    def position(self) -> Tuple[int, int]:
        ...

    @property
    @abstractmethod
    def size(self) -> Tuple[int, int]:
        ...

    @property
    @abstractmethod
    def uuid(self) -> str:
        ...

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    @abstractmethod
    def type(self) -> str:
        ...

    @abstractmethod
    def load(self, data: dict):
        ...

    @abstractmethod
    def dump(self) -> dict:
        ...


class ABCNonPlayableCharacterData(ABCNonPlayableCharacter, ABCCharacterData, metaclass=ABCMeta):
    ...


class ABCPlayableCharacterData(ABCPlayableCharacter, ABCCharacterData, metaclass=ABCMeta):
    ...


class ABCInGameObjectData(ABCObject, ABCEntityData, metaclass=ABCMeta):
    @property
    @abstractmethod
    def location(self) -> Optional[ABCLocation]:
        ...

    @property
    @abstractmethod
    def position(self) -> Tuple[int, int]:
        ...

    @property
    @abstractmethod
    def size(self) -> Tuple[int, int]:
        ...

    @property
    @abstractmethod
    def uuid(self) -> str:
        ...

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    @abstractmethod
    def type(self) -> str:
        ...

    @abstractmethod
    def load(self, data: dict):
        ...

    @abstractmethod
    def dump(self) -> dict:
        ...


class ABCLocationJunctionData(ABCLocationJunction, ABCInGameObjectData, metaclass=ABCMeta):
    @property
    @abstractmethod
    def next_location(self) -> Optional[ABCObject]:
        ...


class ABCLocationData(ABCLocation, ABCEntityData, metaclass=ABCMeta):
    @property
    @abstractmethod
    def size(self) -> Tuple[int, int]:
        ...

    @property
    @abstractmethod
    def objects(self) -> List[ABCObject]:
        ...

    @property
    @abstractmethod
    def characters(self) -> List[ABCCharacter]:
        ...

    @property
    @abstractmethod
    def uuid(self) -> str:
        ...

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    @abstractmethod
    def type(self) -> str:
        ...

    @abstractmethod
    def load(self, data: dict):
        ...

    @abstractmethod
    def dump(self) -> dict:
        ...


class ABCDataController(ABCData, metaclass=ABCMeta):
    """Get data from source and create objects data instances to build data structure.

    Notes
    -----
    Uses only for get data from some sort of repositiry (`__init__`), provide it to next app layer (`dump`),
     and save it to repository back when its needed, aka (`load`).
    """

    @property
    @abstractmethod
    def locations(self) -> List[ABCLocationData]:
        ...

    @property
    @abstractmethod
    def objects(self) -> List[ABCInGameObjectData]:
        ...

    @property
    @abstractmethod
    def characters(self) -> List[ABCCharacterData]:
        ...
