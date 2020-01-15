from state.character.base import Character

__all__ = ['PlayableCharacter', 'NonPlayableCharacter']


class PlayableCharacter(Character):
    DEFAULT_NAME = 'Player'


class NonPlayableCharacter(Character):
    pass
