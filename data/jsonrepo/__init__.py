"""
Этот модуль нужен для тестовой разработки в абстрактном смысле. Надо выработать общие правила и на их основе описать
 класс-адаптер, который будет использовать один из доступных интерфейсов.
"""
import json

from data.abstractions import ABCData
from data.jsonrepo.locations import LocationData
from data.jsonrepo.characters import CharacterData
from data.jsonrepo.objects import ObjectData

from app.mainfunctions.logger import pp

import logging

logger = logging.getLogger(__name__)


class JSONData(ABCData):
    def __init__(self, *args, **kwargs):
        self.__file_path = kwargs.get("source")

        with open(self.__file_path, 'r') as f:
            self.__raw_data = json.load(f)

        self.__locations_list = [LocationData(**location) for location in self.__raw_data['locations']]
        self.__locations_by_id = {location.id: i for i, location in enumerate(self.__locations_list)}

        self.__characters_list = [CharacterData(**character) for character in self.__raw_data['characters']]
        # self.__characters_by_id = {character.location_id: i for i, character in enumerate(self.__characters_list)}

        self.__objects_list = [ObjectData(**obj) for obj in self.__raw_data['objects']]

        self.__world_map = None

        logger.debug(pp.pformat([c.dump() for c in self.__characters_list]))
        logger.debug(pp.pformat([l.dump() for l in self.__locations_list][0]))

    def get_location(self, location_id):
        return self.__locations_list[self.__locations_by_id.get(location_id)]

    def get_character(self, character_id):
        return self.__characters_list

    def get_object(self, obj_id):
        raise NotImplementedError

    def dump(self):
        raise NotImplementedError

    def load(self, data):
        raise NotImplementedError
