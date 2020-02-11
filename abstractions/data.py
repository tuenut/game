from __future__ import annotations

from abc import ABC, abstractmethod, ABCMeta
from typing import List

from abstractions.bases import ABCNonPlayableCharacter, ABCPlayableCharacter, ABCLocation, ABCInGameObject, \
    ABCLocationJunction, ABCInGameEntity

__all__ = [
    'ABCData', 'ABCNonPlayableCharacterData', 'ABCPlayableCharacterData', 'ABCInGameObjectData', 'ABCLocationData',
    'ABCLocationJunctionData', 'ABCDataController', 'ABCInGameEntityData'
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

class ABCInGameEntityData(ABCInGameEntity, ABCData, metaclass=ABCMeta):
    ...


class ABCNonPlayableCharacterData(ABCNonPlayableCharacter, ABCData, metaclass=ABCMeta):
    ...


class ABCPlayableCharacterData(ABCPlayableCharacter, ABCData, metaclass=ABCMeta):
    ...


class ABCInGameObjectData(ABCInGameObject, ABCData, metaclass=ABCMeta):
    ...


class ABCLocationJunctionData(ABCLocationJunction, metaclass=ABCMeta):
    ...


class ABCLocationData(ABCLocation, ABCData, metaclass=ABCMeta):
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
    def objects(self) -> List[ABCInGameObjectData, ABCLocationJunctionData, ...]:
        ...

    @property
    @abstractmethod
    def characters(self) -> List[ABCPlayableCharacterData, ABCNonPlayableCharacterData, ...]:
        ...
