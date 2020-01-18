import unittest

from data.abstractions.locations import ABCLocationData
from data.jsonrepo.locations import LocationData
from data.jsonrepo.tests.data import LOCATION, LOCATION_DUMPED


class TestLocationDataObject(unittest.TestCase):
    @staticmethod
    def create_location():
        return LocationData(**LOCATION)

    def test_init(self):
        location = self.create_location()
        self.assertIsInstance(location, ABCLocationData)

    def test_dump_data(self):
        location = self.create_location()
        self.assertEqual(location.dump(), LOCATION_DUMPED)

    def test_load_data(self):
        location = self.create_location()
        # todo
