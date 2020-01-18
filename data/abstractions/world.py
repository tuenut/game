from abc import ABC, ABCMeta, abstractmethod
from .base import ABCDataObject


class ABCWorldData(ABCDataObject, metaclass=ABCMeta):
    @property
    def object_properties(self):
        pass
    
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

    #  todo пока не ясно, нужно ли отсюда провайдить размеры поля/карты
    #
    # @property
    # @abstractmethod
    # def x_range(self):
    #     ...
    #
    # @property
    # @abstractmethod
    # def y_range(self):
    #     ...

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
