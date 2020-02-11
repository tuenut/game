from __future__ import annotations

from abc import ABC, abstractmethod, ABCMeta
from typing import Optional, Tuple, List

__all__ = [
    'ABCInGameEntity', 'ABCLocation', 'ABCCharacter', 'ABCLocationJunction', 'ABCPlayableCharacter', 'ABCInGameObject',
    'ABCNonPlayableCharacter', 'ABCDoorObject', 'ABCItemObject', 'ABCMoveableObject', 'ABCObstructiveObject'
]


class ABCInGameEntity(ABC):
    @property
    @abstractmethod
    def ingame_id(self) -> str:
        ...

    @property
    @abstractmethod
    def ingame_name(self) -> str:
        ...

    @property
    @abstractmethod
    def ingame_type(self) -> str:
        ...


class ABCLocation(ABCInGameEntity, metaclass=ABCMeta):
    @property
    @abstractmethod
    def size(self) -> Tuple[int, int]:
        ...

    @property
    @abstractmethod
    def objects(self) -> List[ABCInGameObject]:
        ...

    @property
    @abstractmethod
    def characters(self) -> List[ABCCharacter]:
        ...


class ABCInGameObject(ABCInGameEntity, metaclass=ABCMeta):
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


class ABCCharacter(ABCInGameObject, metaclass=ABCMeta):
    """Base class for players, mobs, npc."""
    ...


class ABCPlayableCharacter(ABCCharacter, metaclass=ABCMeta):
    ...


class ABCNonPlayableCharacter(ABCCharacter, metaclass=ABCMeta):
    ...


class ABCLocationJunction(ABCInGameObject, metaclass=ABCMeta):
    """Junction between two locations. Placed on one, transport character to another."""

    @property
    @abstractmethod
    def next_location(self) -> Optional[ABCInGameObject]:
        ...


class ABCObstructiveObject(ABCInGameObject, metaclass=ABCMeta):
    """Some object like a mountains, trees, rocks, wich can't change self position in any way in game."""
    ...


class ABCDoorObject(ABCObstructiveObject, metaclass=ABCMeta):
    ...


class ABCMoveableObject(ABCInGameObject, metaclass=ABCMeta):
    """Some objects wich can be moved by players or in another ways."""
    ...


class ABCItemObject(ABCInGameObject, metaclass=ABCMeta):
    ...
