"""
Этот модуль нужен для тестовой разработки в абстрактном смысле. Надо выработать общие правила и на их основе описать
 класс-адаптер, который будет использовать один из доступных интерфейсов.
"""

import json

from data.abstractions.world import ABCWorldData
from data.jsonrepo.locations import LocationData


class JSONWorldData(ABCWorldData):
    """Класс для хранения данных о состояния мира."""

    def dump(self):
        pass

    # todo все передаваемые наружу данные должны быть серриализованы. Не передавать объекты!

    def __init__(self, json_file):
        self.__file_path = json_file

        with open(self.__file_path, 'r') as f:
            self.__raw_data = json.load(f)

        self.__load_data()

    def __load_data(self):
        self.__world = {}
        for coordinates, location_data in self.__raw_data.items():
            coordinates = tuple(int(i) for i in coordinates.split("."))
            location = LocationData(coordinates, **location_data)

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
        x, y = location.location_id[0], location.location_id[1]
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
    def locations(self):
        return list(self.__world.values())

    @property
    def locations_ids(self):
        return list(self.__world.keys())
