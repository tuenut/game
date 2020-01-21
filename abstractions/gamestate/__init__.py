from __future__ import annotations

from typing import List, Optional, Union, Tuple
from abc import ABC, abstractmethod, ABCMeta

__all__ = ["ABCGameStateLocation"]


class ABCGameState(ABC):
    @abstractmethod
    def update(self):
        ...


class ABCGameStateController(ABCGameState, metaclass=ABCMeta):
    @abstractmethod
    def move_object(self, target_object: ABCGameStateObject, direction: str, *args, **kwargs):
        ...


class ABCGameStateLocationsManager(ABCGameState, metaclass=ABCMeta):
    @abstractmethod
    def __iter__(self) -> ABCGameStateLocation:
        ...

    @abstractmethod
    def get_location(self, location: Union[str, ABCGameStateLocation]) -> Optional[ABCGameStateLocation]:
        ...

    @abstractmethod
    def add_object_on_location(
            self, obj: ABCGameStateObject, location: ABCGameStateLocation
    ) -> Optional[ABCGameStateObject]:
        ...

    @abstractmethod
    def remove_object_from_location(self, obj: ABCGameStateObject) -> Optional[ABCGameStateObject]:
        ...


class ABCGameStateEntity(ABCGameState, metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    @abstractmethod
    def type(self) -> str:
        ...

    @property
    @abstractmethod
    def id(self) -> Optional[str]:
        ...


class ABCGameStateLocation(ABCGameStateEntity, metaclass=ABCMeta):
    @property
    @abstractmethod
    def coordinates(self) -> Tuple[int, int]:
        ...

    @property
    @abstractmethod
    def characters(self) -> List[ABCGameStateLocation]:
        ...

    @property
    @abstractmethod
    def objects(self) -> List[ABCGameStateLocation]:
        ...

    @property
    @abstractmethod
    def exits(self) -> ABCGameStateLocationExitsManager:
        ...

    @abstractmethod
    def get_next_location(self, direction: str) -> Optional[ABCGameStateLocation]:
        ...

    @abstractmethod
    def add_object(self, character: ABCGameStateObject) -> Optional[ABCGameStateObject]:
        ...

    @abstractmethod
    def remove_object(self, character: ABCGameStateObject) -> Optional[ABCGameStateObject]:
        ...

    @abstractmethod
    def move_object_to_next_location(self, obj: ABCGameStateObject, direction: str):
        ...


class ABCGameStateLocationExitsManager(ABCGameState, metaclass=ABCMeta):
    @property
    @abstractmethod
    def north(self) -> ABCGameStateLocationExit:
        ...

    @property
    @abstractmethod
    def south(self) -> ABCGameStateLocationExit:
        ...

    @property
    @abstractmethod
    def west(self) -> ABCGameStateLocationExit:
        ...

    @property
    @abstractmethod
    def east(self) -> ABCGameStateLocationExit:
        ...


class ABCGameStateObject(ABCGameStateEntity, metaclass=ABCMeta):
    @property
    @abstractmethod
    def location(self) -> Optional[ABCGameStateLocation]:
        ...


class ABCGameStateLocationExit(ABCGameStateObject, metaclass=ABCMeta):
    @property
    @abstractmethod
    def next_location(self) -> Optional[ABCGameStateLocation]:
        ...

    @property
    @abstractmethod
    def access(self) -> bool:
        ...


class ABCGameStateCharacter(ABCGameStateObject, metaclass=ABCMeta):
    ...
