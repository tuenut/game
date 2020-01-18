from abc import ABC, abstractmethod, ABCMeta
from .base import ABCDataObject


class ABCObjectRepository(ABCDataObject, metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        ...

    @property
    @abstractmethod
    def type(self):
        ...

    @property
    @abstractmethod
    def location_id(self):
        ...


class ABCCharacterData(ABCObjectRepository, metaclass=ABCMeta):
    @property
    def object_properties(self):
        return ["name", "type", "location_id"]

    def dump(self):
        return {
            "location_id": self.location_id,
            "name": self.name,
            "type": self.type
        }
