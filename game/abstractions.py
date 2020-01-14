from abc import ABC, abstractmethod


class ABCGameObject(ABC):
    @abstractmethod
    def update(self):
        ...