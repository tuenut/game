import copy
import random
from hashlib import sha3_256
from .config import DEFAULT_LOCATION_SIZE


class Location:
    DEFAULT_EXIT = {"location_id": None, "access": None}
    EXITS_PATTERN = {
        "west": copy.deepcopy(DEFAULT_EXIT),
        "east": copy.deepcopy(DEFAULT_EXIT),
        "south": copy.deepcopy(DEFAULT_EXIT),
        "north": copy.deepcopy(DEFAULT_EXIT)
    }
    LOCATION_PATTERN = {
        "exits": copy.deepcopy(EXITS_PATTERN),
        "coordinates": tuple(),
        "characters": [],
        "objects": [],
        "id": None,
        "size": (0, 0)  # (x, y)
    }

    def __init__(self, x, y, world_range_x, world_range_y, location_size=DEFAULT_LOCATION_SIZE):
        self.x = x
        self.y = y
        self.coordinates = (self.x, self.y)
        self.size = location_size

        self.is_location_on_south_edge = (self.y >= max(world_range_y))
        self.is_location_on_west_edge = (self.x <= min(world_range_x))
        self.is_location_on_east_edge = (self.x >= max(world_range_x))
        self.is_location_on_north_edge = (self.y <= min(world_range_y))

        self.data = copy.deepcopy(self.LOCATION_PATTERN)
        self.data["coordinates"] = self.coordinates
        self.data["id"] = self.get_location_id(self.coordinates)
        self.data['exits'] = self.get_exits()
        self.data['size'] = self.size

    def get_exits(self):
        exits = {
            "south": self.south_exit,
            "west": self.west_exit,
            "east": self.east_exit,
            "north": self.north_exit,
        }

        return exits

    @staticmethod
    def get_location_id(coordinates):
        if (
                isinstance(coordinates, tuple) and
                len(coordinates) == 2 and
                all(isinstance(coord, int) for coord in coordinates)
        ):
            return sha3_256(str(coordinates).encode()).hexdigest()
        else:
            return None

    @property
    def location_on_west(self):
        return self.get_location_id((self.x - 1, self.y))

    @property
    def location_on_east(self):
        return self.get_location_id((self.x + 1, self.y))

    @property
    def location_on_south(self):
        return self.get_location_id((self.x, self.y + 1))

    @property
    def location_on_north(self):
        return self.get_location_id((self.x, self.y - 1))

    @property
    def default_exit(self):
        return copy.deepcopy(self.DEFAULT_EXIT)

    @property
    def south_exit(self):
        if not self.is_location_on_south_edge:
            return {"location_id": self.location_on_south, 'access': True}
        else:
            return self.default_exit

    @property
    def west_exit(self):
        if not self.is_location_on_west_edge:
            return {"location_id": self.location_on_west, 'access': True}
        else:
            return self.default_exit

    @property
    def east_exit(self):
        if not self.is_location_on_east_edge:
            return {"location_id": self.location_on_east, 'access': True}
        else:
            return self.default_exit

    @property
    def north_exit(self):
        if not self.is_location_on_north_edge:
            return {"location_id": self.location_on_north, 'access': True}
        else:
            return self.default_exit
