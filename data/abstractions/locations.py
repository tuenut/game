from abc import ABC, abstractmethod


class ABCLocationData(ABC):
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


class ABCExitsData(ABC):
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