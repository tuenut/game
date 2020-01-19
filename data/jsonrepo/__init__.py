"""
Этот модуль нужен для тестовой разработки в абстрактном смысле. Надо выработать общие правила и на их основе описать
 класс-адаптер, который будет использовать один из доступных интерфейсов.
"""
import json

from data.abstractions import ABCData
from data.jsonrepo.locations import LocationData


class JSONData(ABCData):
    def __init__(self, json_file):
        self.__file_path = json_file

        with open(self.__file_path, 'r') as f:
            self.__raw_data = json.load(f)

        self.__locations_list = None
        self.__characters_list = None
        self.__objects_list = None

        self.__world_map = None


    def __load_data(self):
        self.__world = {}
        for coordinates, location_data in self.__raw_data.items():
            coordinates = tuple(int(i) for i in coordinates.split("."))
            location = LocationData(coordinates, **location_data)

            self.__world.update({coordinates: location})

    @property
    def locations_list(self):
        return self.__locations_list

    @property
    def characters_list(self):
        return self.__characters_list

    @property
    def objects_list(self):
        return self.__objects_list

    def move_object_to(self, obj, direction):
        pass

    def add_new_object(self, obj_type, obj_props, location=None):
        pass

    def remove_object(self, obj_id):
        pass

    def delete_obj(self, obj_id):
        pass

    def dump(self):
        pass
