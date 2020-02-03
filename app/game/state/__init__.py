import logging

from abstractions.data.datacontroller import ABCDataController
from abstractions.gamestate import ABCGameStateController

from app.game.state.locations import LocationsManager
from app.game.state.characters import CharactersManager


class GameStateController(ABCGameStateController):
    """Класс для описания состояния игрового мира."""
    locations = LocationsManager
    characters = CharactersManager
    objects = None

    logger = logging.getLogger(__name__)

    def __init__(self, *args, **kwargs):
        self.logger.debug("Init GameState...")

        self.__data = kwargs.get('data')  # type: ABCDataController

        self.locations = LocationsManager(self.__data.locations)
        self.characters = CharactersManager(self.__data.characters)
        # todo: self.objects = ObjectsManager(self.__data.objects)

        for character in self.characters:
            location = self.locations.get_location(character.location)
            self.locations.add_object_on_location(character, location)

        for location in self.locations:
            location.init_characters()

    def move_character(self, character, direction, *args, **kwargs):
        self.logger.debug("Request to moving object <%s> to <%s>.", character, direction)
        try:
            origin_location = character.location
        except AttributeError:
            character = self.characters.get_character(character)
            origin_location = character.location

        next_location = origin_location.get_next_location(direction)

        if next_location is None:
            self.logger.debug("There is no way.")
            return
        if self.locations.remove_object_from_location(character) is None:
            return

        self.locations.add_object_on_location(character, next_location)

        self.logger.debug("Object moved successfully.")

    def move_object(self, target_object, direction, *args, **kwargs):
        self.logger.debug("Request to moving object <%s> to <%s>.", target_object, direction)

        try:
            origin_location = target_object.location
        except AttributeError:
            self.logger.exception("Invalid object <target_object> for moving.")
            return

        next_location = origin_location.get_next_location(direction)

        if next_location is None:
            self.logger.debug("There is no way.")
            return
        if self.locations.remove_object_from_location(target_object) is None:
            return

        self.locations.add_object_on_location(target_object, next_location)

        self.logger.debug("Object moved successfully.")

    def update(self):
        self.characters.update()
