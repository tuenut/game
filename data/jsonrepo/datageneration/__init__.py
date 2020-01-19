import json
import copy

from data.jsonrepo.datageneration.characters import Character
from data.jsonrepo.datageneration.locations import Location
from data.jsonrepo.datageneration.config import *


def generate_locations():
    _locations = []

    for y in RANGE_Y:
        for x in RANGE_X:
            location = Location(x, y, RANGE_X, RANGE_Y)
            _locations.append(location.data)

    return _locations


def generate_characters():
    characters_list = []

    player = Character(**PLAYER_CHARACTER)
    characters_list.append(player.data)

    return characters_list


def place_characters_on_locations(data):
    for character in data['characters']:
        target_location_id = character.get("location")

        if target_location_id:
            for i, location in enumerate(data["locations"]):

                if location['id'] == target_location_id:
                    location['characters'].append(character['id'])


def generate_json_repo(repo_path):
    repository = copy.deepcopy(DATA_PATTERN)

    repository['locations'] = generate_locations()
    repository['characters'] = generate_characters()

    place_characters_on_locations(repository)

    with open(repo_path, 'w') as f:
        json.dump(repository, f, indent=4)
