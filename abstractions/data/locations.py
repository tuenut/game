from abc import ABCMeta, abstractmethod
from typing import Tuple

from abstractions.data.bases import ABCDataEntity
from abstractions.data.objects import ABCDataExit


class ABCDataLocation(ABCDataEntity, metaclass=ABCMeta):
    @property
    def sirializing_fields(self):
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