from abstractions.gamestate import ABCGameStatePlayableCharacter
from app.gamestate.characters.basecharacter import Character


class PlayableCharacterState(ABCGameStatePlayableCharacter, Character):
    DEFAULT_NAME = 'Player'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update(self):
        pass