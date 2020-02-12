from app.game.state.characters.rpgsystem.atributes.bases.stats import BaseAttribute
from app.game.state.characters.rpgsystem.atributes.resourcestat.stats import HealthPoints, StaminaPoints, ManaPoints


class Attributes:
    """
    strength  - physical damage, items and some interaction requirements
    agility   - evading, accuracy, physical critical rate, items and some interaction requirements
    vitality  - health, stamina, health regen, physical effects resist, physical critical resist, some interaction
     requirements
    wisdom    - mana, items and some interaction requirements
    willpower - mana regen, magical resist, magical crit rate, magical crit resist
    intellect - magical damage, magical evading, magical accuracy, items and some interaction requirements
    """

    def __init__(
            self, strength=None, agility=None, vitality=None, wisdom=None, willpower=None, intellect=None,
            health=None, stamina=None, mana=None
    ):
        self.__strength = BaseAttribute(points=strength)
        self.__agility = BaseAttribute(points=agility)
        self.__vitality = BaseAttribute(points=vitality)
        self.__wisdom = BaseAttribute(points=wisdom)
        self.__willpower = BaseAttribute(points=willpower)
        self.__intellect = BaseAttribute(points=intellect)

        self.__health = HealthPoints(points=health)
        self.__stamina = StaminaPoints(points=stamina)
        self.__mana = ManaPoints(points=mana)

    @property
    def strength(self):
        return self.__strength

    @property
    def agility(self):
        return self.__agility

    @property
    def vitality(self):
        return self.__vitality

    @property
    def wisdom(self):
        return self.__wisdom

    @property
    def willpower(self):
        return self.__willpower

    @property
    def intellect(self):
        return self.__intellect

    @property
    def health(self):
        return self.__health

    @property
    def stamina(self):
        return self.__stamina

    @property
    def mana(self):
        return self.__mana