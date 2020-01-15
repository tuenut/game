from abc import ABC, abstractmethod, ABCMeta


class ABCObjectRepository(ABC):
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
    pass
