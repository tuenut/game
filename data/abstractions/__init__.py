# todo пересмотреть методы поиска локации по координатам и по id. Прийти к унифицированному методу.
# т.к. координаты и id по сути являются идентификатором, просто найти способ строить карту локаций
#  не зависимо от типа идентификатора


from abc import ABC, abstractmethod


class ABCWorldData(ABC):
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
