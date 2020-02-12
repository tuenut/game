from __future__ import annotations
from abc import ABC, abstractmethod, ABCMeta
from typing import Union, Optional, Tuple, List

from .bases import ABCEntity, ABCLocation


class ABCGameState(ABC):
    """Базовый класс для всех объектов игры(игрового состояния)."""

    @abstractmethod
    def update(self):
        """Метод для обновления состояния объекта.

        Содержит инструкции для обновления своего собственного состояния, либо вызовы обновления вложенных объектов.
        Вызывается каждую итерацию mainloop.
        """
        ...


class ABCEntityGameState(ABCEntity, ABCGameState, metaclass=ABCMeta):
    """Базовый класс для всех видов игровых сущнрстей, которые могут быть размещены в мире или на локации."""
    ...


class ABCLocationGameState(ABCLocation, ABCEntityGameState, metaclass=ABCMeta):
    """Класс состояния локации.

    Локация может содержать в себе персонажей(игроков и npc) и объекты(предметы, объекты окружения).
    """

    @abstractmethod
    def add_object(self, character: ABCGameStateObject) -> Optional[ABCGameStateObject]:
        """Добавить объект на текущюю локацию.

        todo: возможно, добавить метод для "размещения" объекта (place_object(obj)), чтобы размещать объект в
        todo определенном месте.
        todo: исправить имя входного аргумента.
        """
        ...

    @abstractmethod
    def remove_object(self, character: ABCGameStateObject) -> Optional[ABCGameStateObject]:
        """Удалить объект с текущей локации."""
        ...


class ABCGameStateObject(ABCEntityGameState, metaclass=ABCMeta):
    @property
    @abstractmethod
    def location(self) -> Optional[ABCLocationGameState]:
        ...

    @location.setter
    @abstractmethod
    def location(self, value) -> Optional[ABCLocationGameState]:
        ...


class ABCGameStateLocationExit(ABCGameStateObject, metaclass=ABCMeta):
    @property
    @abstractmethod
    def next_location(self) -> Optional[ABCLocationGameState]:
        ...

    @property
    @abstractmethod
    def access(self) -> bool:
        ...


class ABCGameStateCharacter(ABCGameStateObject, metaclass=ABCMeta):
    @property
    @abstractmethod
    def DEFAULT_NAME(self):
        ...

    def __repr__(self):
        return "<Character {type}.{name}, location: {location}>".format(
            type=self.type, name=self.name, location=self.location
        )

    __str__ = __repr__


class ABCGameStateNonPlayableCharacter(ABCGameStateCharacter, metaclass=ABCMeta):
    ...


class ABCGameStatePlayableCharacter(ABCGameStateCharacter, metaclass=ABCMeta):
    ...


class ABCGameStateController(ABCGameState, metaclass=ABCMeta):
    """Класс контроллера игрового состояния.

    Управляет отдельными менеджерами игровых сущностей.
    """

    @abstractmethod
    def move_object(self, target_object: ABCGameStateObject, direction: str, *args, **kwargs):
        """Метод-callback для перемещениия объекта по событию."""
        ...


class ABCGameStateLocationsManager(ABCGameState, metaclass=ABCMeta):
    """Менеджер локаций.

    Создает локации при инициализации. Предоставляет API для некоторого управления состоянием имеющихся локаций.
    Может самостоятельно управлять локациями, без предоставления API наружу.
    """

    @abstractmethod
    def __iter__(self) -> ABCLocationGameState:
        ...

    @abstractmethod
    def get_location(self, location: Union[str, ABCLocationGameState]) -> Optional[ABCLocationGameState]:
        """Получаем локацию по id или объекту локации.

        Вернет объект локации или None, если локации нет в списке локаций.
        """
        ...

    @abstractmethod
    def add_object_on_location(
            self, obj: ABCGameStateObject, location: ABCLocationGameState
    ) -> Optional[ABCGameStateObject]:
        """Добавляем объект на локацию.

        Возвращает None, если добавление не удалось. Можно использовать для перемещения объекта с локации на локацию.
        """
        ...

    @abstractmethod
    def remove_object_from_location(self, obj: ABCGameStateObject) -> Optional[ABCGameStateObject]:
        """Удаляем объект с локации.

        Вернет None, если удаление не удачно. Можно использовать для перемещения объекта с локации на локацию.
        """
        ...



class ABCGameStateCharactersManager(ABCGameState, metaclass=ABCMeta):
    @abstractmethod
    def __iter__(self) -> ABCGameStateCharacter:
        ...

    @abstractmethod
    def create_character(self, character_dumped_data: dict) -> ABCGameStateCharacter:
        ...

    @abstractmethod
    def get_character(self, character: Union[str, ABCGameStateCharacter]) -> ABCGameStateCharacter:
        ...
