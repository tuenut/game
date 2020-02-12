class BaseAttribute:
    BASE_VALUE_CAP = 999
    DEFAULT_POINTS = 1

    def __init__(self, points=None, cap=None):
        self.__points = points if points else self.DEFAULT_POINTS
        self.__current_points = self.__points

        self.__CAP = cap if cap else self.BASE_VALUE_CAP

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


