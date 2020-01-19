from abc import ABC, ABCMeta, abstractmethod

__all__ = ['ABCDataObject']


class ABCDataObject(ABC):
    @property
    @abstractmethod
    def object_properties(self):
        return []

    @abstractmethod
    def dump(self):
        """Serialize data object to dict and other simple types."""
        ...

    def load(self, *args, **kwargs):
        for key, value in kwargs.items():
            if key in self.object_properties:
                try:
                    setattr(self, key, value)
                except AttributeError:
                    pass
