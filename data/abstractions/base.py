from abc import ABC, ABCMeta, abstractmethod

__all__ = ['ABCDataObject']


class ABCDataObject(ABC):
    @property
    @abstractmethod
    def data_fields(self):
        """Significant fields for data object dump()/load() methods."""
        return []

    @abstractmethod
    def load(self, data):
        """Save data to store(disk, db, etc)."""
        ...

    def dump(self):
        """Serialize data object to dict and other simple types."""
        return {field: getattr(self, field) for field in self.data_fields}
