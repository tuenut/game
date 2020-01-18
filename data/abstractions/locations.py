from abc import ABC, ABCMeta, abstractmethod
from .base import ABCDataObject

__all__ = ["ABCLocationData", "ABCExitsData"]


class ABCLocationData(ABCDataObject, metaclass=ABCMeta):
    @property
    def object_properties(self):
        return []

    @property
    @abstractmethod
    def exits(self):
        """

        :return:
            ABCExits
        """
        ...

    @property
    @abstractmethod
    def location_id(self):
        ...

    @property
    @abstractmethod
    def characters(self):
        ...

    @property
    @abstractmethod
    def objects(self):
        ...

    @abstractmethod
    def add_character(self, character):
        ...

    @abstractmethod
    def add_object(self, obj):
        ...

    @abstractmethod
    def remove_character(self, character):
        ...

    @abstractmethod
    def remove_object(self, obj):
        ...


class ABCExitsData(ABCDataObject, metaclass=ABCMeta):
    @property
    def object_properties(self):
        return []

    @property
    @abstractmethod
    def down(self):
        ...

    @property
    @abstractmethod
    def left(self):
        ...

    @property
    @abstractmethod
    def right(self):
        ...

    @property
    @abstractmethod
    def up(self):
        ...
