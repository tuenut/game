from abstractions.data import ABCDataCharacter


class CharacterData(ABCDataCharacter):
    __location = None

    def __init__(self, **kwargs):
        self.__id = kwargs.get("id")
        self.__location = kwargs.get('location')
        self.__name = kwargs.get('name')
        self.__type = kwargs.get('type')

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

    def load(self, data):
        raise NotImplementedError