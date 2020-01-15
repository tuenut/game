from data.abstractions.objects import ABCCharacterData


class CharacterData(ABCCharacterData):
    def __init__(self, location, **kwargs):
        self.__location = location
        self.__name = kwargs.get('name')
        self.__type = kwargs.get('type')

    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__type

    @property
    def location(self):
        return self.__location