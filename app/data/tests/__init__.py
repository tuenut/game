import unittest
from app.utils.logger import configure_logger
from app.data.models.bases import database
from app.data.models import GameEntity, Location, Character
from config import PLAYABLE_CHARACTER_TYPE, NON_PLAYABLE_CHARACTER_TYPE


class TestDataBase(unittest.TestCase):
    logger = configure_logger()

    def test_create_tables(self):
        database.drop_tables([Location, GameEntity, Character])
        database.create_tables([Location, GameEntity, Character])

    def test_create_locations(self):
        locations = [
            {
                'position_x': 0,
                'position_y': 0,
                'ingame_type': "location"
            },
            {
                'position_x': 1,
                'position_y': 1,
                'ingame_type': "location"
            },
        ]

        for location in locations:
            Location.create(**location)

    def test_create_characters(self):
        characters = [
            {
                'ingame_type': PLAYABLE_CHARACTER_TYPE,
                'ingame_name': 'test_player',
            },
            {
                'ingame_type': NON_PLAYABLE_CHARACTER_TYPE,
                'ingame_name': 'test_npc',
            },
        ]

        for character in characters:
            Character.create(**character)
