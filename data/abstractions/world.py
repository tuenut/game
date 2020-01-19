from abc import ABC, ABCMeta, abstractmethod
from .base import ABCDataObject


__all__ = ['ABCWorldMapData']


class ABCWorldMapData(ABCDataObject, metaclass=ABCMeta):
    @property
    def object_properties(self):
        return []
    
    @property
    @abstractmethod
    def locations(self):
        """
        todo 'data' is deprecated.
        Хочу убрать, чтобы был унифицированный интерфейс поиска локации по координатам или id,
         вместо прямого доступа к хранилищу и создания зависимости от реализации хранилища.

        :return:
            list
        """
        ...

    @property
    @abstractmethod
    def locations_ids(self):
        ...

    @abstractmethod
    def get_location(self, location_id):
        ...

    @abstractmethod
    def get_next_location(self, location, direction):
        ...
