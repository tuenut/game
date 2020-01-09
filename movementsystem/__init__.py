class Cell:
    def __init__(self, down=None, left=None, right=None, up=None):
        self.down = down
        self.left = left
        self.right = right
        self.up = up

    @property
    def exits(self):
        return self.down, self.left, self.right, self.up


class SimplePositioningDataBase:
    directions = ('left', 'right', 'up', 'down')

    def __init__(self, y_max=10, x_max=10):
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

                cell = Cell(down, left, right, up)

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


class MovementSystemInterface:
    def __init__(self, movement_system_repository):
        raise NotImplementedError
        self.repo = movement_system_repository()

    def move(self, direction):
        raise NotImplementedError

    def get_location(self):
        raise NotImplementedError


if __name__ == "__main__":
    world_map = SimplePositioningDataBase()

    directions_text = ''.join(sorted([word[0] for word in world_map.directions])) + ' '
    print(directions_text * len(world_map.x_range))

    for x_row in world_map.grid:
        row = ''
        for location in x_row:
            col = ''.join(str(int(location[key])) for key in sorted(location.keys()))
            row += col + ' '
        print(row)
