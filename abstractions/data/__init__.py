from __future__ import annotations

from abstractions.data import ABCDataLocation, ABCDataObject, ABCDataCharacter
from abstractions.data.characters import ABCDataCharacter
from abstractions.data.locations import ABCDataLocation
from abstractions.data.objects import ABCDataObject

PLAYABLE_CHARACTER = "player"
NON_PLAYABLE_CHARACTER = "npc"
CHARACTER_TYPES = (PLAYABLE_CHARACTER, NON_PLAYABLE_CHARACTER)
WEST = 'west'
EAST = 'east'
NORTH = 'north'
SOUTH = 'south'
DIRECTIONS = [WEST, EAST, NORTH, SOUTH]


