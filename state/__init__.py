import logging

from data.abstractions import ABCData, PLAYABLE_CHARACTER
from state.abstractions import ABCGameStateObject, ABCGameState
from state.characters import PlayableCharacterState
from state.locations import LocationState
from app.mainfunctions.logger import pp

logger = logging.getLogger(__name__)


class GameState(ABCGameState):
    """Класс для описания состояния игрового мира."""

    def __init__(self, *args, **kwargs):
        logger.debug("Init GameState...")

        self.__locations = {}  # type: {str: LocationState}
        self.__characters = {}  # type: {str: PlayableCharacterState}
        self.__objects = []

        self.player = None

        self.__data = kwargs.get('data')  # type: ABCData

        if self.__data is not None:
            for location_id in self.__data.get_all_locations():
                self.create_location(location_id)

            for character_id in self.__data.get_all_characters():
                self.create_character(character_id)

            for location in self.__locations.values():
                location.init_exits()
                location.init_characters()

    def create_location(self, location_id: str):
        # todo сделать как create_character()
        location = LocationState(self.__data.get_location(location_id), self.get_location, self.get_character)
        self.__locations.update({location.id: location})

    def create_character(self, character_id: str):
        character_data = self.__data.get_character(character_id)

        if character_data.type == PLAYABLE_CHARACTER and self.player is None:
            character = PlayableCharacterState(**character_data.dump())
            self.player = character.id
            self.__characters.update({character.id: character})

    def get_character(self, character_id: str):
        return self.__characters.get(character_id)

    def get_location(self, location_id: str):
        """

        Parameters
        ----------
        location_id

        Returns
        -------
            location : LocationState
        """
        return self.__locations.get(location_id)

    def get_all_locations(self):
        return list(self.__locations.keys())

    def add_object_on_location(self, obj: str, location: str):
        raise NotImplementedError

    def remove_object_from_location(self, obj: str):
        raise NotImplementedError

    def move_object(self, obj_id: str, direction: str):
        character = self.get_character(obj_id) # type:PlayableCharacterState or None

        # todo: obj = self.get_object(obj_id)
        obj = None

        target_object = character or obj

        if target_object is None:
            return
        else:
            origin_location = self.get_location(target_object.location)
            next_location = origin_location.get_next_location(direction)

            logger.debug("try move <{}> to <{}> from {}".
                         format(target_object.name, direction, origin_location.coordinates))

            if next_location is not None:
                logger.debug(
                    "<{}> can move to <{}> on location {}".
                        format(target_object.name, direction, next_location.coordinates)
                )

                if origin_location.remove_character(character.id):
                    next_location.add_character(character.id)
                    character.location = next_location
                else:
                    raise Exception("Can't move character.")
            else:
                logger.debug("There is no way!")

    def update(self):
        pass
