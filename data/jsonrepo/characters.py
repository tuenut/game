from data.abstractions.objects import ABCCharacterData


class CharacterData(ABCCharacterData):
    __location = None

    def __init__(self, **kwargs):
        self.__location = kwargs.get('location')
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

    def load(self, data):
        raise NotImplementedError