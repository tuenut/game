from abc import ABCMeta, abstractmethod
from typing import List

from abstractions.data import ABCDataLocation, ABCDataObject, ABCDataCharacter
from abstractions.data.bases import ABCData


class ABCDataController(ABCData, metaclass=ABCMeta):
    """Get data from source and create objects data instances to build data structure.

    Notes
    -----
    Uses only for get data from some sort of repositiry (`__init__`), provide it to next app layer (`dump`),
     and save it to repository when its needed, aka (`load`).
    """

    @property
    def sirializing_fields(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def locations(self) -> List[ABCDataLocation]:
        ...

    @property
    @abstractmethod
    def objects(self) -> List[ABCDataObject]:
        ...

    @property
    @abstractmethod
    def characters(self) -> List[ABCDataCharacter]:
        ...

    @abstractmethod
    def get_location(self, location_id: str) -> ABCDataLocation:
        ...

    @abstractmethod
    def get_character(self, character_id: str) -> ABCDataCharacter:
        ...

    @abstractmethod
    def get_object(self, obj_id: str) -> ABCDataObject:
        ...

    @abstractmethod
    def dump(self) -> dict:
        ...

    @abstractmethod
    def load(self, data: dict):
        ...