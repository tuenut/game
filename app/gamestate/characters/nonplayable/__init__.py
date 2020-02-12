from abstractions.gamestate import ABCGameStateNonPlayableCharacter
from app.gamestate.characters.aisystem import NPCMazeAI
from app.gamestate.characters.basecharacter import Character


class NonPlayableCharacter(ABCGameStateNonPlayableCharacter, Character):
    DEFAULT_NAME = 'NPC'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ai = NPCMazeAI(self)

    def update(self):
        self.ai.update()