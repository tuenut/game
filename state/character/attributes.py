class BaseStatModifier:
    """
    Модификатор используется для влияния на характеристики.
    value - числовое значение int или float
    source - источник модификатора(например, расовая особенность)
    description - описание
    id - уникальный идентификатор, передаваемый при инициализации
    """

    def __init__(self, value, increment_id, source=None, description=None):
        self.value = value
        self.source = source
        self.description = description
        self.id = increment_id

    def __radd__(self, other):
        """для работы sum() со списком модификаторов"""
        return self.value + other


class ResourceStatModifier(BaseStatModifier):
    pass


class BaseStat:
    """
    Характеристика может быть установлена только при инициализации,
    может быть получено ее значение, значение может быть изменено только
    через соответствующие методы.
    """
    DEFAULT_CAP = 999
    DEFAULT_POINTS = 1

    def __init__(self, points=None, cap=None):
        self.__points = points if points else self.DEFAULT_POINTS
        self.__current_points = points if points else self.DEFAULT_POINTS
        self.__CAP = cap if cap else self.DEFAULT_CAP

    @property
    def points(self):
        return self.__points

    @property
    def current(self):
        return self.__current_points

    def increase_stat(self, value=None):
        if (self.points + value) > self.__CAP or (self.points + 1) > self.__CAP:
            return False
        else:
            self.__points += value if value else 1
            return self.points

    def decrease_stat(self, value=None):
        if (self.points - value) <= 0 or (self.points - 1) <= 0:
            return False
        else:
            self.__points -= value if value else 1
            return self.points


class ResourceStat(BaseStat):
    """
    Ресурсная характеристика имеет максимальный зампас, текущее значение.
    Может быть потрачено текущее значение до тех пор, пока оно не равно 0.
    Текущее значение может быть восстановлено до максимального.
    Максимальное значение может быть увеличено с учетом модификаторов на
    постоянной основе, может быть временно увеличено за счет бонуса.
    """
    DEFAULT_POINTS = 10

    __BASE_MULT = 10.0

    __multipliers = []  # list of ResourceStatModifier
    __multipliers_indices = {}  # {modifier_id: index_in_list}
    __increments = []
    __increments_indices = {}

    __bonus_mult = []
    __bonus_mult_indices = {}
    __bonus_add = []
    __bonus_add_indices = {}

    @property
    def total_points(self):
        return self.points + self.bonus_add + (self.points * self.bonus_mult)

    @property
    def bonus_add(self):
        return sum(self.__bonus_add)

    @property
    def bonus_mult(self):
        return sum(self.__bonus_mult)

    @property
    def multiplier_mod(self):
        return sum(self.__multipliers)

    @property
    def increment_mod(self):
        return sum(self.__increments)

    def increase_stat(self, value=None):
        increment = self.increment_mod + (value * self.multiplier_mod)\
            if value else self.increment_mod
        if (self.points + increment) > self.__CAP:
            return False
        else:
            self.__points += increment
            return self.points

    def reducing(self, value=None):
        self.__current_points -= value
        if self.__current_points < 0:
            self.__current_points = 0
            return False
        else:
            return True

    def restoring(self, value=None):
        self.__current_points += value
        if self.__current_points > self.points:
            self.__current_points = self.points


class BaseAttributes:
    """
    strength  - physical damage, items and some interaction requirements
    agility   - evading, accuracy, physical critical rate, items and some interaction requirements
    vitality  - health, stamina, health regen, physical effects resist, physical critical resist, some interaction requirements
    wisdom    - mana, items and some interaction requirements
    willpower - mana regen, magical resist, magical crit rate, magical crit resist
    intellect - magical damage, magical evading, magical accuracy, items and some interaction requirements
    """

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

    def __init__(self, strength=None, agility=None, vitality=None, wisdom=None,
                 willpower=None, intellect=None, attribute_cap=None,
                 health=None, stamina=None, mana=None, resource_cap=None):
        self.__strength = BaseStat(points=strength, cap=attribute_cap)
        self.__agility = BaseStat(points=agility, cap=attribute_cap)
        self.__vitality = BaseStat(points=vitality, cap=attribute_cap)
        self.__wisdom = BaseStat(points=wisdom, cap=attribute_cap)
        self.__willpower = BaseStat(points=willpower, cap=attribute_cap)
        self.__intellect = BaseStat(points=intellect, cap=attribute_cap)

        self.health = ResourceStat(points=health, cap=resource_cap)
        self.stamina = ResourceStat(points=stamina, cap=resource_cap)
        self.mana = ResourceStat(points=mana, cap=resource_cap)

    def level_up(self, *args, strength=0, agility=0, vitality=0, wisdom=0,
                 willpower=0, intellect=0, **kwargs):
        self.strength.increase_stat(strength)
        self.agility.increase_stat(agility)
        self.vitality.increase_stat(vitality)
        self.wisdom.increase_stat(wisdom)
        self.willpower.increase_stat(willpower)
        self.intellect.increase_stat(intellect)

        self.health.increase_stat(self.vitality.points)
        self.stamina.increase_stat(self.vitality.points)
        self.mana.increase_stat(self.wisdom.points)

