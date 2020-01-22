import pygame
import random
import logging

from abstractions.data import ABCDataController
from abstractions.gamestate import ABCGameStateController
from abstractions.data import DIRECTIONS
from app.game.state.universe.locations import LocationsManager
from app.game.state.universe.characters import CharactersManager

logger = logging.getLogger(__name__)


class GameStateController(ABCGameStateController):
    """Класс для описания состояния игрового мира."""
    locations = LocationsManager
    characters = CharactersManager
    objects = None

    def __init__(self, *args, **kwargs):
        logger.debug("Init GameState...")

        self.__data = kwargs.get('data')  # type: ABCDataController

        self.locations = LocationsManager(self.__data.locations)
        self.characters = CharactersManager(self.__data.characters)
        # todo: self.objects = ObjectsManager(self.__data.objects)

        for character in self.characters:
            location = self.locations.get_location(character.location)
            self.locations.add_object_on_location(character, location)

        for location in self.locations:
            location.init_characters()

    def move_object(self, target_object, direction, *args, **kwargs):
        logger.debug("Request to moving object <%s> to <%s>.", target_object, direction)

        try:
            origin_location = target_object.location
        except AttributeError:
            logger.exception("Invalid object <target_object> for moving.")
            return

        next_location = origin_location.get_next_location(direction)

        if next_location is None:
            logger.debug("There is no way.")
            return
        if self.locations.remove_object_from_location(target_object) is None:
            return

        self.locations.add_object_on_location(target_object, next_location)

        logger.debug("Object moved successfully.")

    def update(self):
        pass
        # if random.choices([0, 1], [2, 10])[0]:
        #     e = pygame.event.Event(
        #         pygame.USEREVENT,
        #         dict(
        #             character=self.characters.player,
        #             direction=random.choice(DIRECTIONS),
        #             custom_type="move_character"
        #         )
        #     )
        #
        #     pygame.event.post(e)
