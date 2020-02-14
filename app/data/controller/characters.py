from abstractions.data import ABCData

from app.data.models import Character


class CharactersDataController(ABCData):
    def load(self, data: dict):
        raise NotImplementedError

    def dump(self) -> list:
        return [character.dump() for character in self.characters]

    def __init__(self):
        self.characters = Character.select()
