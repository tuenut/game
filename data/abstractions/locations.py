from abc import ABC, ABCMeta, abstractmethod
from .base import ABCDataObject

__all__ = ["ABCLocationData", ]


class ABCLocationData(ABCDataObject, metaclass=ABCMeta):
    @property
    def data_fields(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def id(self):
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

    @property
    @abstractmethod
    def location_on_south(self):
        """

        Returns
        -------
            location_exit: ExitData
        """
        ...

    @property
    @abstractmethod
    def location_on_west(self):
        """

        Returns
        -------
            location_exit: ExitData
        """
        ...

    @property
    @abstractmethod
    def location_on_east(self):
        """

        Returns
        -------
            location_exit: ExitData
        """
        ...

    @property
    @abstractmethod
    def location_on_north(self):
        """

        Returns
        -------
            location_exit: ExitData
        """
        ...


class ExitData(ABCDataObject):
    def __init__(self, access, location_id):
        self.__access = bool(access)
        self.__location = location_id

    @property
    def location(self):
        return self.__location

    @property
    def accessible(self):
        return self.__access

    @property
    def data_fields(self):
        return []

    def dump(self):
        return {
            "location_id": self.location,
            "access": self.accessible
        }

    def load(self, data):
        raise NotImplementedError
