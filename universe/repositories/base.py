from abc import ABC, abstractmethod


class ABCWorldRepository(ABC):
    @property
    @abstractmethod
    def data(self):
        """
        todo 'data' is deprecated.
        Хочу убрать, чтобы был унифицированный интерфейс поиска локации по координатам или id,
         вместо прямого доступа к хранилищу и создания зависимости от реализации хранилища.
        """
        ...

    @property
    @abstractmethod
    def x_range(self):
        ...

    @property
    @abstractmethod
    def y_range(self):
        ...

    @property
    @abstractmethod
    def locations_coordinates(self):
        ...

    @property
    @abstractmethod
    def locations_ids(self):
        ...

    @abstractmethod
    def get_location_by_id(self, location_id):
        ...

    @abstractmethod
    def get_location_by_coordinates(self, x, y):
        ...


class ABCLocationRepository(ABC):
    @property
    @abstractmethod
    def exits(self):
        ...

    @property
    @abstractmethod
    def characters(self):
        ...

    @property
    @abstractmethod
    def objects(self):
        ...