from state.characters.atributes.bases.stats import BaseAttribute


class ResourceAttribute(BaseAttribute):
    """
    Ресурсная характеристика имеет максимальный зампас, текущее значение.
    Может быть потрачено текущее значение до тех пор, пока оно не равно 0.
    Текущее значение может быть восстановлено до максимального.
    Максимальное значение может быть увеличено с учетом модификаторов на
    постоянной основе, может быть временно увеличено за счет бонуса.
    """
    DEFAULT_POINTS = 100
    BASE_VALUE_CAP = 999999999

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
        increment = self.increment_mod + (value * self.multiplier_mod) if value else self.increment_mod
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


class HealthPoints(ResourceAttribute):
    DEFAULT_POINTS = 100


class StaminaPoints(ResourceAttribute):
    DEFAULT_POINTS = 100


class ManaPoints(ResourceAttribute):
    DEFAULT_POINTS = 100