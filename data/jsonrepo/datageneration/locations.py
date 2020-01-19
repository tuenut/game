import copy
from hashlib import sha3_256


class Location:
    DEFAULT_EXIT = {"location_id": None, "access": None}
    EXITS_PATTERN = {
        "left": copy.deepcopy(DEFAULT_EXIT),
        "right": copy.deepcopy(DEFAULT_EXIT),
        "down": copy.deepcopy(DEFAULT_EXIT),
        "up": copy.deepcopy(DEFAULT_EXIT)
    }
    LOCATION_PATTERN = {
        "exits": copy.deepcopy(EXITS_PATTERN),
        "coordinates": tuple(),
        "characters": [],
        "objects": [],
        "id": None
    }

    def __init__(self, x, y, world_range_x, world_range_y):
        self.x = x
        self.y = y
        self.coordinates = (self.x, self.y)

        self.is_location_on_bottom_edge = (self.y >= max(world_range_y))
        self.is_location_on_left_edge = (self.x <= min(world_range_x))
        self.is_location_on_right_edge = (self.x >= max(world_range_x))
        self.is_location_on_top_edge = (self.y <= min(world_range_y))

        self.data = copy.deepcopy(self.LOCATION_PATTERN)
        self.data["coordinates"] = self.coordinates
        self.data["id"] = self.get_location_id(self.coordinates)
        self.data['exits'] = self.get_exits()

    def get_exits(self):
        exits = {
            "down": self.bottom_exit,
            "left": self.left_exit,
            "right": self.right_exit,
            "up": self.up_exit,
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
    def location_on_left(self):
        return self.get_location_id((self.x - 1, self.y))

    @property
    def location_on_right(self):
        return self.get_location_id((self.x + 1, self.y))

    @property
    def location_on_bottom(self):
        return self.get_location_id((self.x, self.y + 1))

    @property
    def location_on_top(self):
        return self.get_location_id((self.x, self.y - 1))

    @property
    def default_exit(self):
        return copy.deepcopy(self.DEFAULT_EXIT)

    @property
    def bottom_exit(self):
        if not self.is_location_on_bottom_edge:
            return {"location_id": self.location_on_bottom, 'access': True}
        else:
            return self.default_exit

    @property
    def left_exit(self):
        if not self.is_location_on_left_edge:
            return {"location_id": self.location_on_left, 'access': True}
        else:
            return self.default_exit

    @property
    def right_exit(self):
        if not self.is_location_on_right_edge:
            return {"location_id": self.location_on_right, 'access': True}
        else:
            return self.default_exit

    @property
    def up_exit(self):
        if not self.is_location_on_top_edge:
            return {"location_id": self.location_on_top, 'access': True}
        else:
            return self.default_exit