import unittest

from data.abstractions.objects import ABCCharacterData
from data.jsonrepo.characters import CharacterData
from data.jsonrepo.tests.data import CHARACTER, CHARACTER_DUMPED, CHARACTER_MOVED, LOCATION_ID_ONE, LOCATION_ID_TWO


class TestCharacterDataObject(unittest.TestCase):
    @staticmethod
    def create_character():
        return CharacterData(LOCATION_ID_ONE, **CHARACTER)

    def test_init(self):
        character = self.create_character()
        self.assertIsInstance(character, ABCCharacterData)

    def test_dump_data(self):
        character = self.create_character()

        self.assertEqual(character.dump(), CHARACTER_DUMPED)

    def test_load_data(self):
        character = self.create_character()
        character.load(location_id=LOCATION_ID_TWO)

        # because for now i don't planing provide interface to change name or type of character.
        character.load(type="new_type")
        character.load(name="name")

        self.assertEqual(character.dump(), CHARACTER_MOVED)
