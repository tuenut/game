"""
Этот модуль нужен для тестовой разработки в абстрактном смысле. Надо выработать общие правила и на их основе описать
 класс-адаптер, который будет использовать один из доступных интерфейсов.
"""

from .base import ABCWorldRepository, ABCLocationRepository

PLAYER = {'type': 'player', 'name': 'player'}


class LocationRepository(ABCLocationRepository):
    __exits = None
    __content = None

    def __init__(self, **kwargs):
        self.exits = kwargs.get('exits')
        self.__content = kwargs.get('characters')

    @property
    def characters(self):
        return self.__content

    @characters.setter
    def characters(self, value):
        pass

    @property
    def objects(self):
        raise NotImplementedError

    @property
    def exits(self):
        return self.__exits

    @exits.setter
    def exits(self, value):
        if isinstance(value, dict) and {'left', 'right', 'up', 'down'} == set(value.keys()):
            self.__exits = value


class WorldRepository(ABCWorldRepository):
    """Класс для хранения состояния мира.
    todo В данном сучае это тестовый вариант. Как организовать хорошо и правильно пока не понятно.
    todo задумка такая (WorldState) <- (WorldInterface) <- (data source)
    todo есть один класс, который предоставляет API наружу, он использует одну из реализаций интерфейса для конкретного
            источника данных

    """

    @property
    def locations_coordinates(self):
        return list(self.__data.keys())

    @property
    def locations_ids(self):
        raise NotImplementedError("Поиск локации по id не заложен")

    directions = ('left', 'right', 'up', 'down')

    def __init__(self, *args, y_max=10, x_max=10, **kwargs):
        self.__data = {}

        self.__x_range = range(x_max)
        self.__y_range = range(y_max)

        self.__fill_grid()

    def __fill_grid(self):
        for x in self.x_range:
            for y in self.y_range:
                cell = {'exits': {}}

                if (x, y) == (0, 0):
                    # todo для персонажей и объектов должен быть свой класс, аналогично локациям
                    player = PLAYER
                    cell.update({"characters": [player, ]})

                if x == min(self.x_range):
                    cell['exits'].update({'left': False, 'right': True, })
                elif x == max(self.x_range):
                    cell['exits'].update({'left': True, 'right': False, })
                else:
                    cell['exits'].update({'left': True, 'right': True, })

                if y == min(self.y_range):
                    cell['exits'].update({'up': False, 'down': True, })
                elif y == max(self.y_range):
                    cell['exits'].update({'up': True, 'down': False, })
                else:
                    cell['exits'].update({'up': True, 'down': True, })

                self.__data.update({(x, y): LocationRepository(**cell)})

    @property
    def data(self):
        return self.__data

    @property
    def x_range(self):
        return self.__x_range

    @property
    def y_range(self):
        return self.__y_range

    def get_location_by_coordinates(self, x, y):
        return self.data.get((x, y))

    def get_location_by_id(self, location_id):
        raise NotImplementedError("Поиск локации по id не заложен")
