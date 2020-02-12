import logging

from app.utils.logger import pp


from app.gamestate.characters.rpgsystem.atributes import Attributes
from app.gamestate.characters.rpgsystem.classes import CharacterClass
from app.gamestate.characters.rpgsystem.races import CharacterRace
from app.gamestate.characters.rpgsystem.actions import CharacterMoving
from app.gamestate.characters.rpgsystem.actions import CharacterAttack
from app.gamestate.characters.rpgsystem.actions import CharacterInterraction

logger = logging.getLogger(__name__)


class Character:
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

