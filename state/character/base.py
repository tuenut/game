from state import ABCGameStateObject

from state.character.atributes import Attributes
from state.character.classes import CharacterClass
from state.character.races import CharacterRace
from state.character.actions import CharacterMoving
from state.character.actions import CharacterAttack
from state.character.actions import CharacterInterraction


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

        self.name = kwargs.get('name', self.DEFAULT_NAME)
        self.position = kwargs.get('position')

    def update(self):
        raise NotImplementedError
