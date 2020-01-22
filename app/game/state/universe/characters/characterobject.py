from abstractions.gamestate import ABCGameStateCharacter


class Character(ABCGameStateCharacter):
    DEFAULT_NAME = 'Character'

    def __init__(self, *args, **kwargs):
        self.__id = kwargs.get('id')
        self.__name = kwargs.get('name', self.DEFAULT_NAME)
        self.__type = kwargs.get("type")
        self.__location = kwargs.get('location')

    def update(self):
        raise NotImplementedError

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__type

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location

    def __repr__(self):
        return "<Character {type}.{name}, location: {location}>".format(
            type=self.type, name=self.name, location=self.location
        )

    __str__ = __repr__


class PlayableCharacterState(Character):
    DEFAULT_NAME = 'Player'


class NonPlayableCharacter(Character):
    DEFAULT_NAME = 'NPC'
