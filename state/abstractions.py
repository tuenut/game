from abc import ABC, abstractmethod


class ABCGameStateObject(ABC):
    @abstractmethod
    def update(self):
        ...