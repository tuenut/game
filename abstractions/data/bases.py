from abc import ABC, abstractmethod, ABCMeta
from typing import Tuple


class ABCData(ABC):
    @property
    @abstractmethod
    def sirializing_fields(self):
        """Fields for data object dump()/load() methods."""
        return []

    @abstractmethod
    def load(self, data):
        """Load data to self."""
        ...

    def dump(self):
        """Serialize data from self to jsonable dict."""
        return {field: getattr(self, field) for field in self.sirializing_fields}


class ABCDataEntity(ABCData, metaclass=ABCMeta):
    @property
    @abstractmethod
    def id(self) -> str:
        ...

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    @abstractmethod
    def type(self) -> str:
        ...

class ABCDataMaterialEntityMixin(ABCDataEntity, metaclass=ABCMeta):
    @property
    @abstractmethod
    def location(self) -> Optional[ABCDataLocation]:
        ...

    @property
    @abstractmethod
    def position(self) -> Tuple(int, int):
        ...