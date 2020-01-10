"""
Этот модуль нужен для тестовой разработки в абстрактном смысле. Надо выработать общие правила и на их основе описать
 класс-адаптер, который будет использовать один из доступных интерфейсов.
"""


class Location:
    """Класс для хранения состояния ячейки"""
    def __init__(self, down=None, left=None, right=None, up=None, objects=None):
        self.down = down
        self.left = left
        self.right = right
        self.up = up

        self.__objects = objects if isinstance(objects, list) else []

    @property
    def exits(self):
        return self.down, self.left, self.right, self.up

    @property
    def objects(self):
        return self.__objects

    @property
    def contents(self):
        return {
            "exits": self.exits,
            "objects": self.objects
        }

    def add_object(self, obj):
        self.__objects.append(obj)

    def remove_object(self, obj):
        try:
            self.__objects.remove(obj)
        except ValueError:
            return None
        else:
            return obj

    def __repr__(self):
        return "<loc %s>" % str([int(e) for e in self.exits])

    __str__ = __repr__


class WorldRepository:
    """Класс для хранения состояния мира.
    todo В данном сучае это тестовый вариант. Как организовать хорошо и правильно пока не понятно.
    todo задумка такая (WorldState) <- (WorldInterface) <- (data source)
    todo есть один класс, который предоставляет API наружу, он использует одну из реализаций интерфейса для конкретного
            источника данных

    """
    directions = ('left', 'right', 'up', 'down')

    def __init__(self, *args, y_max=10, x_max=10, **kwargs):
        self.__grid = []

        self.__x_range = range(x_max)
        self.__y_range = range(y_max)

        self.__fill_grid()

    def __fill_grid(self):
        for x in self.x_range:
            self.__grid.append([])

            for y in self.y_range:
                if x == min(self.x_range):
                    left = False
                    right = True
                elif x == max(self.x_range):
                    left = True
                    right = False
                else:
                    left = True
                    right = True

                if y == min(self.y_range):
                    up = False
                    down = True
                elif y == max(self.y_range):
                    up = True
                    down = False
                else:
                    up = True
                    down = True

                cell = Location(down, left, right, up)

                self.__grid[x].append(cell)

    @property
    def grid(self):
        return self.__grid

    @property
    def x_range(self):
        return self.__x_range

    @property
    def y_range(self):
        return self.__y_range