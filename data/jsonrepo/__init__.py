"""
Этот модуль нужен для тестовой разработки в абстрактном смысле. Надо выработать общие правила и на их основе описать
 класс-адаптер, который будет использовать один из доступных интерфейсов.
"""

import json

from data import ABCWorldRepository
from data.jsonrepo.locations import LocationRepository


class WorldRepository(ABCWorldRepository):
    """Класс для хранения состояния мира.
    todo В данном сучае это тестовый вариант. Как организовать хорошо и правильно пока не понятно.
    todo задумка такая (WorldState) <- (WorldInterface) <- (data source)
    todo есть один класс, который предоставляет API наружу, он использует одну из реализаций интерфейса для конкретного
            источника данных

    """

    directions = ('left', 'right', 'up', 'down')

    def __init__(self, json_file):
        self.__file_path = json_file

        with open(self.__file_path, 'r') as f:
            self.__raw_data = json.load(f)

        self.__load_data()

    def __load_data(self):
        self.__world = {}
        for coordinates, location_data in self.__raw_data.items():
            coordinates = tuple(int(i) for i in coordinates.split("."))
            location = LocationRepository(coordinates, **location_data)

            self.__world.update({coordinates: location})

    def get_location(self, location_id):
        return self.__world.get(location_id)

    def get_next_location(self, location, direction):
        """

        :param location:
        :param direction:
        :return:
            location : вернет ту же самую локацию, если соседняя не существует.
        """
        x, y = location.coordinates[0], location.coordinates[1]
        pos = (x, y)

        if direction == "down":
            pos = (x, y + 1)
        elif direction == "left":
            pos = (x - 1, y)
        elif direction == "right":
            pos = (x + 1, y)
        elif direction == "up":
            pos = (x, y - 1)

        return self.get_location(pos)

    @property
    def data(self):
        return list(self.__world.values())

    @property
    def locations_ids(self):
        return list(self.__world.keys())
