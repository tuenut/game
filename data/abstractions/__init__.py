# todo пересмотреть методы поиска локации по координатам и по id. Прийти к унифицированному методу.
# т.к. координаты и id по сути являются идентификатором, просто найти способ строить карту локаций
#  не зависимо от типа идентификатора
from abc import ABC, ABCMeta, abstractmethod
from .base import ABCDataObject

__all__ = []


class ABCData(ABCDataObject, metaclass=ABCMeta):
    @property
    @abstractmethod
    def locations_list(self):
        ...

    @property
    @abstractmethod
    def characters_list(self):
        ...

    @property
    @abstractmethod
    def objects_list(self):
        ...

    @abstractmethod
    def move_object_to(self, obj, direction):
        ...

    @abstractmethod
    def add_new_object(self, obj_type, obj_props, location=None):
        ...

    @abstractmethod
    def remove_object(self, obj_id):
        """Remove from location."""
        ...

    @abstractmethod
    def delete_obj(self, obj_id):
        """Fully delete object from game."""
        ...

    def load(self, *args, **kwargs):
        raise NotImplementedError