from config import CELL_SIZE

DATA_PATTERN = {
    "locations": [],
    "characters": [],
    "objects": [],
}

RANGE_X = range(4)
RANGE_Y = range(4)

DEFAULT_LOCATION_SIZE = (CELL_SIZE, CELL_SIZE)

PLAYER_CHARACTER = {
    "type": "player",
    "name": "player",
    "location": (0, 0)
}

NPC_CHARACTER = {
    "type": "npc",
    "name": "npc",
    "location": (9, 0)
}
