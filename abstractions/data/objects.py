from abc import ABCMeta, abstractmethod
from typing import Optional

from abstractions.data import ABCDataLocation
from abstractions.data.bases import ABCDataEntity


class ABCDataObject(ABCDataEntity, metaclass=ABCMeta):
    @property
    def sirializing_fields(self):
        """Fields for data object dump()/load() methods."""
        return ["name", "type", "location", "id"]

    @property
    @abstractmethod
    def location(self) -> Optional[ABCDataLocation]:
        ...


class ABCDataExit(ABCDataObject, metaclass=ABCMeta):
    @property
    @abstractmethod
    def next_location(self):
        ...

    @property
    @abstractmethod
    def accessible(self):
        ...