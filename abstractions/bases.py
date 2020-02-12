from __future__ import annotations

from abc import ABC, abstractmethod, ABCMeta
from typing import Optional, Tuple, List

__all__ = [
    'ABCEntity', 'ABCLocation', 'ABCCharacter', 'ABCLocationJunction', 'ABCPlayableCharacter', 'ABCObject',
    'ABCNonPlayableCharacter', 'ABCDoorObject', 'ABCItemObject', 'ABCMoveableObject', 'ABCObstructiveObject'
]


class ABCEntity(ABC):
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


class ABCLocation(ABCEntity, metaclass=ABCMeta):
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


class ABCObject(ABCEntity, metaclass=ABCMeta):
    """All objects wich can be placed on locations."""

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


class ABCCharacter(ABCObject, metaclass=ABCMeta):
    """Base class for players, mobs, npc."""
    ...


class ABCPlayableCharacter(ABCCharacter, metaclass=ABCMeta):
    ...


class ABCNonPlayableCharacter(ABCCharacter, metaclass=ABCMeta):
    ...


class ABCLocationJunction(ABCObject, metaclass=ABCMeta):
    """Junction between two locations. Placed on one, transport character to another."""

    @property
    @abstractmethod
    def next_location(self) -> Optional[ABCObject]:
        ...


class ABCObstructiveObject(ABCObject, metaclass=ABCMeta):
    """Some object like a mountains, trees, rocks, wich can't change self position in any way in game."""
    ...


class ABCDoorObject(ABCObstructiveObject, metaclass=ABCMeta):
    ...


class ABCMoveableObject(ABCObject, metaclass=ABCMeta):
    """Some objects wich can be moved by players or in another ways."""
    ...


class ABCItemObject(ABCObject, metaclass=ABCMeta):
    ...
