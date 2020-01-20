from abc import abstractmethod, ABCMeta
from .base import ABCDataObject


class ABCObjectRepository(ABCDataObject, metaclass=ABCMeta):
    @property
    @abstractmethod
    def id(self):
        ...

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
    def location(self):
        ...


class ABCCharacterData(ABCObjectRepository, metaclass=ABCMeta):
    @property
    def data_fields(self):
        return ["name", "type", "location", "id"]
