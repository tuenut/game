import logging

from app.mainfunctions.logger import pp

from state.abstractions import ABCGameStateObject
from state.characters.atributes import Attributes
from state.characters.classes import CharacterClass
from state.characters.races import CharacterRace
from state.characters.actions import CharacterMoving
from state.characters.actions import CharacterAttack
from state.characters.actions import CharacterInterraction

logger = logging.getLogger(__name__)


class Character(ABCGameStateObject):
    """
    Описание методов персонажа.

    Персонаж имеет различные виды параметров: класс, раса, возможно расширение этого списка.
    Эти параметры оказывают влияние на базовые атрибуты персонажа.
    По сути персонаж имеет базовые атрибуты в виде характеристик (сила, ловкость и тд),
     ресурсные характеристики, которые могут быть израсходованы, например, здоровье или мана.
     Любая характеристика имеет базовое значение, которое может быть измененно за счет модификаторов.
     Модификаторы могут быть переданы от класса, расы, либо временных эффектов.

    """

    __klass_cls = CharacterClass
    __race_cls = CharacterRace
    __atributes_cls = Attributes

    __moving_cls = CharacterMoving
    __interraction_cls = CharacterInterraction
    __attack_cls = CharacterAttack

    DEFAULT_NAME = 'Character'

    ATTRIBUTE_CAP = 999
    RESOURCE_CAP = 1000000
    name = None

    def __init__(self, *args, **kwargs):
        self.atributes = self.__atributes_cls(
            strength=kwargs.get('strength'),
            agility=kwargs.get('agility'),
            vitality=kwargs.get('vitality'),
            wisdom=kwargs.get('wisdom'),
            willpower=kwargs.get('willpower'),
            intellect=kwargs.get('intellect'),
        )

        logger.debug("Create character with kwargs: \n{}".format(pp.pformat(kwargs)))

        self.__id = kwargs.get('id')
        self.name = kwargs.get('name', self.DEFAULT_NAME)
        self.__type = kwargs.get("type")
        self.__location = kwargs.get('location')

    def update(self):
        raise NotImplementedError

    @property
    def id(self):
        return self.__id

    @property
    def type(self):
        return self.__type

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        # todo здесь бы какую-то проверку или предусмотреть на другом уровне, что локация может быть только
        # определенного типа
        self.__location = location

    def __repr__(self):
        return "<Character {type}.{name}, location: {location}>".format(
            type=self.type, name=self.name, location=self.location
        )

    __str__ = __repr__