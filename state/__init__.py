import logging


from data.abstractions.locations import ABCLocationData
from data.abstractions.objects import ABCObjectRepository, ABCCharacterData
from state.abstractions import ABCGameStateObject
from state.locations import Location

logger = logging.getLogger(__name__)


class GameState(ABCGameStateObject):
    """Класс для описания состояния игрового мира."""

    def __init__(self, *args, **kwargs):
        logger.debug("Init GameState...")

        self.__world_data = kwargs.get('data')
        self.__generate_locations()

    def __generate_locations(self):
        self.__locations = [Location(location) for location in self.__world_data.locations]
        self.__locations_by_coordinates = {location.coordinates: location for location in self.__locations}

    def add_object_on_location(self, obj: ABCObjectRepository, location: ABCLocationData):
        raise NotImplementedError

    def remove_object_from_location(self, obj: ABCObjectRepository):
        raise NotImplementedError

    def move_object(self, obj: ABCObjectRepository, direction: str):
        """Изменяет состояние репозитория данных."""
        self.remove_object_from_location(obj)
        self.add_object_on_location(obj, self.__world_data.get_next_location(obj.location_id, direction))

    def update(self):
        """Обновить состояние мира на основе состояния репозитория данных."""
        pass  # todo subj

    def create_player(self, player: ABCCharacterData):
        logger.warning("Method not implemented!")

    @property
    def locations(self):
        # todo реализовать self.data, а это убрать.
        return self.__locations

    @property
    def data(self):
        """
        Должен возвращать серриализованные данные объектов для того, чтобы сообщить о текущем состоянии кому-то снаружи.

        :return:
        """
        raise NotImplementedError