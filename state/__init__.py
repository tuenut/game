import logging

from data.abstractions import ABCData
from state.abstractions import ABCGameStateObject, ABCGameState
from state.universe.locations import LocationsManager
from state.universe.characters import CharactersManager

logger = logging.getLogger(__name__)


class GameState(ABCGameState):
    """Класс для описания состояния игрового мира."""
    locations = LocationsManager
    characters = CharactersManager
    objects = None

    def __init__(self, *args, **kwargs):
        logger.debug("Init GameState...")

        self.__data = kwargs.get('data')  # type: ABCData

        self.locations = LocationsManager(self.__data.get_all_locations())
        self.characters = CharactersManager(self.__data.get_all_characters())

        for character in self.characters:
            location = self.locations.get_location(character.location)
            self.locations.add_object_on_location(character, location)

        for location in self.locations:
            location.init_characters()

    def move_object(self, target_object: ABCGameStateObject, direction: str, *args, **kwargs):
        logger.debug("Request to moving object <%s> to <%s>.", target_object, direction)

        try:
            origin_location = target_object.location
        except AttributeError:
            logger.exception("Invalid object <target_object> for moving.")
            return None

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
