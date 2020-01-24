import logging
import random
from datetime import timedelta as td, datetime as dt

import pygame

from abstractions.data import EAST, NORTH, WEST, SOUTH, NON_PLAYABLE_CHARACTER
from app.events import EventManager, MOVE_CHARACTER
from app.game import GameStateController


class AISystem:
    DELAY = td(milliseconds=500)
    PREFFERED_DIRECTIONS = [EAST, NORTH]
    OPPOSITE_DIRECTIONS = {
        EAST: WEST,
        WEST: EAST,
        NORTH: SOUTH,
        SOUTH: NORTH
    }

    logger = logging.getLogger(__name__)

    def __init__(self, game_state: GameStateController):
        self.__characters = game_state.characters
        self.__characters_knowledge = {}

        for character in self.__characters:
            if character.type == NON_PLAYABLE_CHARACTER:
                character_data = {character.id: {"timestamp": dt.now(), "map": {}}}
                self.__characters_knowledge.update(character_data)

    def choose_direction_of_character_move(self, character):
        character_data = self.__characters_knowledge[character.id]
        known_map = character_data.get("map", {})
        current_location_coordinates = character.location.coordinates
        current_location = known_map.get(current_location_coordinates)


        # заподнить знания о локации, если их нет
        if current_location is None:
            current_location = {
                EAST: {
                    "access": bool(character.location.exits.east.access),
                    "increment": (1, 0),  # increment coordinates to ge next location
                    "score": None
                },
                WEST: {
                    "access": bool(character.location.exits.west.access),
                    "increment": (-1, 0),
                    "score": None
                },
                NORTH: {
                    "access": bool(character.location.exits.north.access),
                    "increment": (0, -1),
                    "score": None
                },
                SOUTH: {
                    "access": bool(character.location.exits.south.access),
                    "increment": (0, 1),
                    "score": None
                },
            }
            known_map.update({current_location_coordinates: current_location})

        # считаем веса для выбора направления
        for direction, exit_data in current_location.items():
            if exit_data['score'] is None:
                access = exit_data["access"]

                if not access:
                    # если нет выхода пробуем другой, помечаем как плохой
                    access = 0
                    exit_data['score'] = 0
                    continue

                score = int(access) * 10 if direction in self.PREFFERED_DIRECTIONS else int(access) * 2

                # проверяем, что известно о следующей локации
                next_location = known_map.get(tuple(map(
                    lambda x, y: x + y,
                    current_location_coordinates, exit_data["increment"]
                )))
                if next_location is None:
                    pass
                else:
                    score += next_location[self.OPPOSITE_DIRECTIONS[direction]]["access"] * 2

                exit_data['score'] = score

                self.logger.debug("Location <%s> exit <%s> score <%s>", current_location_coordinates, direction, score)

        weights = [current_location[key]["score"] for key in sorted(list(current_location.keys()))]

        self.__characters_knowledge.update({character.id: known_map})

        return random.choices(sorted(list(current_location.keys())), weights)[0]

    def update(self):
        for character in self.__characters:
            if character.type == NON_PLAYABLE_CHARACTER:
                character_data = self.__characters_knowledge.get(character.id, {})
                if dt.now() - character_data["timestamp"] > self.DELAY:
                    # direction = random.choice(DIRECTIONS)
                    direction = self.choose_direction_of_character_move(character)

                    EventManager.dispatch(
                        pygame.USEREVENT,
                        subtype=MOVE_CHARACTER,
                        character=character.id,
                        direction=direction
                    )

                    self.__characters_knowledge.update({character.id: {"timestamp": dt.now()}})