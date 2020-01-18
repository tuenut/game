LOCATION_ID_ONE = "0.0"
LOCATION_ID_TWO = "0.1"

CHARACTER = {
    "type": "test_character",
    "name": "Test Character",
}
CHARACTER_DUMPED = {**CHARACTER, "location_id": LOCATION_ID_ONE}
CHARACTER_MOVED = {**CHARACTER, "location_id": LOCATION_ID_TWO}

LOCATION = {
    "location_id": LOCATION_ID_ONE,
    "exits": {
        "left": False,
        "right": True,
        "up": True,
        "down": False
    },
    "characters": [CHARACTER, ],
    "objects": []
}

LOCATION_DUMPED = {**LOCATION, "characters": [CHARACTER_DUMPED, ]}
