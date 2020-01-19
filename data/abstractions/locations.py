from abc import ABC, ABCMeta, abstractmethod
from .base import ABCDataObject

__all__ = ["ABCLocationData", ]


class ABCLocationData(ABCDataObject, metaclass=ABCMeta):
    @property
    def data_fields(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def id(self):
        ...

    @property
    @abstractmethod
    def coordinates(self):
        ...

    @property
    @abstractmethod
    def characters(self):
        ...

    @property
    @abstractmethod
    def objects(self):
        ...

    @property
    @abstractmethod
    def location_on_bottom(self):
        ...

    @property
    @abstractmethod
    def location_on_left(self):
        ...

    @property
    @abstractmethod
    def location_on_right(self):
        ...

    @property
    @abstractmethod
    def location_on_top(self):
        ...
