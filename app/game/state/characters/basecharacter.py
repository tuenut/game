from abstractions.gamestate import ABCGameStateCharacter


class Character(ABCGameStateCharacter):
    DEFAULT_NAME = 'Character'

    def __init__(self, *args, **kwargs):
        self._id = kwargs.get('id')
        self._name = kwargs.get('name', self.DEFAULT_NAME)
        self._type = kwargs.get("type")
        self._location = kwargs.get('location')

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location




