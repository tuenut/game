from abc import ABC, abstractmethod


class ABCObject(ABC):
    @property
    @abstractmethod
    def position(self):
        ...

    @property
    @abstractmethod
    def location_id(self):
        ...

    @property
    @abstractmethod
    def data(self):
        ...

    @abstractmethod
    def move(self, *args, **kwargs):
        """return True if can move. Can contain some checks."""
        ...

    @property
    def name(self):
        return self.data.name

    @property
    def type(self):
        return self.data.type
