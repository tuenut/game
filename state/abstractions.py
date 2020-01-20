from abc import ABC, ABCMeta, abstractmethod


class ABCGameState(ABC):
    @abstractmethod
    def update(self):
        ...


class ABCGameStateObject(ABCGameState, metaclass=ABCMeta):
    @property
    @abstractmethod
    def location(self):
        ...

    @property
    @abstractmethod
    def name(self):
        ...

    @property
    @abstractmethod
    def type(self):
        ...
