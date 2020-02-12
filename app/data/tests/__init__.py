import unittest

from app.utils.logger import configure_logger
from app.data.models.bases import database
from app.data.models import Entity, Location, Character, InGameObject, LocationJunction, EntityTypes
from config import CELL_SIZE
from app.data.config import PLAYABLE_CHARACTER_TYPE, NON_PLAYABLE_CHARACTER_TYPE, LOCATION_TYPE, OBJECT_TYPE, \
    JUNCTION_OBJECT_TYPE, ENTITY_TYPES

database.init(':memory:')


# TODO sqlite в памяти, похоже, сществует только в пределах запуска одного теста.
# TODO или переделать на файл, или разобраться с контекстом.


class TestDataBase(unittest.TestCase):
    logger = configure_logger()

    @database.connection_context()
    def test_001_create_tables(self):
        database.drop_tables([Location, Entity, Character, InGameObject, LocationJunction, EntityTypes])
        database.create_tables([Location, Entity, Character, InGameObject, LocationJunction, EntityTypes])

    @database.connection_context()
    def test_002_create_types(self):
        for entity_description, entity_type in ENTITY_TYPES.items():
            EntityTypes.create(value=entity_type, description=entity_description)

    @database.connection_context()
    def test_003_create_locations(self):
        locations = [
            {
                'position_x': 0,
                'position_y': 0,
                'type': LOCATION_TYPE,
                'name': 'location_1'
            },
            {
                'position_x': 1,
                'position_y': 1,
                'type': LOCATION_TYPE,
                'name': 'location_2'
            },
        ]

        for location in locations:
            Location.create(**location)

    @database.connection_context()
    def test_004_create_characters(self):
        characters = [
            {
                'type': PLAYABLE_CHARACTER_TYPE,
                'name': 'test_player',
            },
            {
                'type': NON_PLAYABLE_CHARACTER_TYPE,
                'name': 'test_npc',
            },
        ]

        for character in characters:
            Character.create(**character)

    @database.connection_context()
    def test_005_create_objects(self):
        InGameObject.create(
            name='test_object',
            type=OBJECT_TYPE,
            position_x=int(CELL_SIZE / 2),
            position_y=int(CELL_SIZE / 2),
            size_x=int(CELL_SIZE / 10),
            size_y=int(CELL_SIZE / 10),
            location=Location.get_or_none(name='location_1')
        )

    @database.connection_context()
    def test_005_create_location_junctions(self):
        LocationJunction.create(
            name='location_junction',
            type=JUNCTION_OBJECT_TYPE,
            position_x=10,
            position_y=0,
            size_x=int(CELL_SIZE - CELL_SIZE / 10),
            size_y=10,
            location=Location.get_or_none(name='location_1')
        )
