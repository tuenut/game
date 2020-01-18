from data.abstractions.objects import ABCCharacterData


class CharacterData(ABCCharacterData):
    def __init__(self, location_id, **kwargs):
        self.__location_id = location_id
        self.__name = kwargs.get('name')
        self.__type = kwargs.get('type')

    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__type

    @property
    def location_id(self):
        return self.__location_id

    @location_id.setter
    def location_id(self, value):
        self.__location_id = value

