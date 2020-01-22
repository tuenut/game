"""
Этот модуль нужен для тестовой разработки в абстрактном смысле. Надо выработать общие правила и на их основе описать
 класс-адаптер, который будет использовать один из доступных интерфейсов.
"""
import json
import logging

from abstractions.data import ABCDataController
from app.game.data.jsonrepo.locations import LocationData
from app.game.data.jsonrepo.characters import CharacterData
from app.game.data.jsonrepo.objects import ObjectData

logger = logging.getLogger(__name__)


class JSONDataController(ABCDataController):
    def __init__(self, *args, **kwargs):
        self.__file_path = kwargs.get("source")

        logger.debug("Open file <{}>".format(self.__file_path))

        with open(self.__file_path, 'r') as f:
            self.__raw_data = json.load(f)

        self.__locations_list = [LocationData(**location) for location in self.__raw_data['locations']]
        self.__locations_by_id = {location.id: i for i, location in enumerate(self.__locations_list)}

        self.__characters_list = [CharacterData(**character) for character in self.__raw_data['characters']]
        self.__characters_by_id = {character.id: i for i, character in enumerate(self.__characters_list)}

        self.__objects_list = [ObjectData(**obj) for obj in self.__raw_data['objects']]

        self.__world_map = None

    def get_location(self, location_id):
        index = self.__locations_by_id.get(location_id)
        return self.__locations_list[index]

    def get_character(self, character_id):
        index = self.__characters_by_id.get(character_id)
        return self.__characters_list[index]

    def get_object(self, obj_id):
        raise NotImplementedError

    @property
    def locations(self, ):
        return [location.dump() for location in self.__locations_list]

    @property
    def characters(self):
        return [character.dump() for character in self.__characters_list]

    @property
    def objects(self):
        raise NotImplementedError

    def dump(self):
        raise NotImplementedError

    def load(self, data):
        raise NotImplementedError
