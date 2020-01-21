import logging

from abstractions.data import PLAYABLE_CHARACTER
from state.characters import PlayableCharacterState, NonPlayableCharacter
from state.characters.base import Character

logger = logging.getLogger(__name__)


class CharactersManager:
    def __init__(self, characters_data):
        self.__characters_data = characters_data
        self.__characters = {}  # type: {str: Character}
        self.player = None

        if self.__characters_data is not None:
            self.__init_character_objets()

    def __iter__(self):
        for character in self.__characters.values():
            yield character

    def __init_character_objets(self):
        for character_dumped_data in self.__characters_data:
            self.create_character(character_dumped_data)

    def create_character(self, character_dumped_data: dict):
        if character_dumped_data.get('type') == PLAYABLE_CHARACTER and self.player is None:
            character = PlayableCharacterState(**character_dumped_data)

            self.player = character
            self.__characters.update({character.id: character})

            return character
        else:
            return None

    def get_character(self, character):
        """Character getter.

        Parameters
        ----------
        character

        Returns
        -------
            character : PlayableCharacterState or NonPlayableCharacter or None
        """
        if self.__is_valid_character_state_object(character):
            return character
        elif isinstance(character, str):
            return self.__characters.get(character)
        else:
            return None

    def __is_valid_character_state_object(self, character):
        logger.debug("Check is %s a valid character", character)

        is_character = False
        in_characters = False

        try:
            is_character = issubclass(character.__class__, Character)
            in_characters = character.id in self
        except Exception as e:
            result = False
        else:
            result = is_character and in_characters

        logger.debug("Is character: %s. In characters: %s. Result: %s.", is_character, in_characters, result)

        return result

    def update(self):
        raise NotImplementedError