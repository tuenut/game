from universe.repositories.dumb import WorldRepository
from .location import Location

class World:
    """Класс для описания состояния игрового мира.
    Содержит информацию об игровом поле, локациях.
    """

    __locations_list = None

    def __init__(self):
        self.__world_repository = WorldRepository()
        self.__locations = [
            Location(exits=location.exits, coordinates=coordinates, characters=location.characters)
            for coordinates, location in self.__world_repository.data.items()
        ]

    def __generate_locations(self):
        ...

    @property
    def locations(self):
        """
        Нужно для сообщения информации обо всех локациях в мире наружу.
        :return:
        """
        return [location.data for location in self.__locations]

    def move(self, direction):
        raise NotImplementedError

    def add_object_on_location(self, obj, location):
        raise NotImplementedError