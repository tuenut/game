import logging
import random
import pygame

from datetime import timedelta as td, datetime as dt

from app.events import EventManager, MOVE_CHARACTER
from abstractions.data import EAST, NORTH, WEST, SOUTH
from abstractions.gamestate import ABCGameState


class NPCMazeAI(ABCGameState):
    DELAY = td(milliseconds=500)
    PREFFERED_DIRECTIONS = [EAST, NORTH]
    OPPOSITE_DIRECTIONS = {
        EAST: WEST,
        WEST: EAST,
        NORTH: SOUTH,
        SOUTH: NORTH
    }

    logger = logging.getLogger(__name__)

    def __init__(self, character_state):
        self.__character = character_state
        self.__knowledge = {"timestamp": dt.now(), "map": {}}

    def choose_direction_of_character_move(self):
        known_map = self.__knowledge.get("map", {})

        current_location_coordinates = self.__character.location.position
        current_location = known_map.get(current_location_coordinates)

        # заподнить знания о локации, если их нет
        if current_location is None:
            current_location = {
                EAST: {
                    "access": bool(self.__character.location.exits.east.access),
                    "increment": (1, 0),  # increment coordinates to ge next location
                    "score": None
                },
                WEST: {
                    "access": bool(self.__character.location.exits.west.access),
                    "increment": (-1, 0),
                    "score": None
                },
                NORTH: {
                    "access": bool(self.__character.location.exits.north.access),
                    "increment": (0, -1),
                    "score": None
                },
                SOUTH: {
                    "access": bool(self.__character.location.exits.south.access),
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
                    # access = 0 todo: seems unnecessary
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

                self.logger.debug("Location <%s> exit <%s> score <%s>", current_location_coordinates, direction,
                                  score)

        weights = [current_location[key]["score"] for key in sorted(list(current_location.keys()))]

        self.__knowledge.update({self.__character.id: known_map})

        return random.choices(sorted(list(current_location.keys())), weights)[0]

    def update(self):
        if dt.now() - self.__knowledge["timestamp"] > self.DELAY:

            direction = self.choose_direction_of_character_move()

            EventManager.dispatch(
                pygame.USEREVENT,
                subtype=MOVE_CHARACTER,
                character=self.__character.id,
                direction=direction
            )

            self.__knowledge.update({"timestamp": dt.now()})