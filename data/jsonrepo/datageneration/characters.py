import copy
import json
from hashlib import sha3_256

from data.jsonrepo.datageneration.locations import Location


class Character:
    CHARACTER_PATTERN = {
        "type": None,
        "name": None,
        "location": None,
        "id": None
    }

    def __init__(self, **kwargs):
        self.data = copy.deepcopy(self.CHARACTER_PATTERN)
        self.data['name'] = kwargs.get('name')
        self.data['type'] = kwargs.get('type')
        self.data['location'] = Location.get_location_id(kwargs.get('location'))
        self.data['id'] = self.get_character_id(self.data)

    @staticmethod
    def get_character_id(character_data: dict):
        hashable_data = {
            key: value
            for key, value in character_data.items()
            if key in ("type", "name")
        }
        return sha3_256(json.dumps(hashable_data).encode()).hexdigest()