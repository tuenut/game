from __future__ import annotations

from typing import List, Optional, Union, Tuple
from abc import ABC, abstractmethod, ABCMeta

__all__ = [
    "ABCGameState", "ABCGameStateController", "ABCGameStateLocationsManager", "ABCGameStateEntity",
    "ABCGameStateLocation", "ABCGameStateLocationExitsManager", "ABCGameStateObject", "ABCGameStateLocationExit",
    "ABCGameStateCharacter", "ABCGameStateCharactersManager"
]


class ABCGameState(ABC):
    """Базовый класс для всех объектов игры(игрового состояния)."""

    @abstractmethod
    def update(self):
        """Метод для обновления состояния объекта.

        Содержит инструкции для обновления своего собственного состояния, либо вызовы обновления вложенных объектов.
        Вызывается каждую итерацию mainloop.
        """
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
    def __iter__(self) -> ABCGameStateLocation:
        ...

    @abstractmethod
    def get_location(self, location: Union[str, ABCGameStateLocation]) -> Optional[ABCGameStateLocation]:
        """Получаем локацию по id или объекту локации.

        Вернет объект локации или None, если локации нет в списке локаций.
        """
        ...

    @abstractmethod
    def add_object_on_location(
            self, obj: ABCGameStateObject, location: ABCGameStateLocation
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


class ABCGameStateEntity(ABCGameState, metaclass=ABCMeta):
    """Базовый класс для всех видов игровых сущнрстей, которые могут быть размещены в мире или на локации."""
    @property
    @abstractmethod
    def name(self) -> str:
        """Имя игрового объекта."""
        ...

    @property
    @abstractmethod
    def type(self) -> str:
        """Тип игрового объекта."""
        ...

    @property
    @abstractmethod
    def id(self) -> Optional[str]:
        """УНИКАЛЬНЫЙ идентификатор игрового объекта."""
        ...

    @property
    @abstractmethod
    def size(self) -> Tuple[int, int]:
        """Размер игрового объекта."""
        ...

    @property
    @abstractmethod
    def position(self) -> Tuple[int, int]:
        """Позиция игрового объекта.

        Объекты, размещаемые на локациях используют параметр, как относительную позицию на локации.
        Объекты, размещаемые в мире (локации), используют позицию как абсолютное размещение в мире.

        todo: Возможно, это придется учитывать при отрисовке локаций и объектов.
        todo: А так же выборе методов отображения этого всего.
        """
        ...


class ABCGameStateLocation(ABCGameStateEntity, metaclass=ABCMeta):
    """Класс состояния локации.

    Локация может содержать в себе персонажей(игроков и npc) и объекты(предметы, объекты окружения).
    """
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
        """Переходы на соседнюю локацию.

        todo: переделать в объекты на локации, чтобы задавать им позицию.
        """
        ...

    @abstractmethod
    def get_next_location(self, direction: str) -> Optional[ABCGameStateLocation]:
        """
        todo deprecated: убрать, потому что перемещение с локации на локацию будет зависить от конфигурации
        todo объекта перехода(выхода), а не ка ксейчас.

        """
        ...

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

    @abstractmethod
    def move_object_to_next_location(self, obj: ABCGameStateObject, direction: str):
        """todo DEPRECATED: использовался как шорткат для удаления объекта с одной локации и добавления на другую."""
        ...


class ABCGameStateLocationExitsManager(ABCGameState, metaclass=ABCMeta):
    """todo DEPRECATED: Менеджер выходов. Убрать, т.к. выходы должны быть приравнены к объектам на локации."""
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


class ABCGameStateObject(ABCGameStateEntity, metaclass=ABCMeta):
    @property
    @abstractmethod
    def location(self) -> Optional[ABCGameStateLocation]:
        ...

    @location.setter
    @abstractmethod
    def location(self, value) -> Optional[ABCGameStateLocation]:
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
