import pygame


class Door:
    def __init__(self, surface, x, y, width, height, color):
        self.x = x
        self.y = y
        self.surface = surface
        self.height = height
        self.width = width
        self.color = color

        self.draw_door()

    def draw_door(self):
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.width, self.height))


class Cell:
    color_left = (255, 100, 100)
    color_right = (100, 255, 100)
    color_up = (100, 100, 255)
    color_down = (255, 255, 100)
    color_no_exit = (50, 50, 50)

    background = (100, 100, 100)

    cell_size = 62
    door_height = 8
    door_width = cell_size - 2 * door_height

    def __init__(self, exits=(0, 0, 0, 0), x=0, y=0, ):
        self.x = x
        self.y = y

        self.exits = exits

        self.surface = pygame.Surface((self.cell_size, self.cell_size))
        self.surface = self.surface.convert()
        self.surface.fill(self.background)

        self.down_door = Door(self.surface, *self.__down_door)
        self.left_door = Door(self.surface, *self.__left_door)
        self.right_door = Door(self.surface, *self.__right_door)
        self.up_door = Door(self.surface, *self.__up_door)

    @property
    def __down_door(self):
        x = self.door_height
        y = self.cell_size - self.door_height
        width = self.door_width
        height = self.door_height
        color = self.color_down if self.exits[0] else self.color_no_exit

        return x, y, width, height, color

    @property
    def __left_door(self):
        x = 0
        y = self.door_height
        width = self.door_height
        height = self.door_width
        color = self.color_left if self.exits[1] else self.color_no_exit

        return x, y, width, height, color

    @property
    def __right_door(self):
        x = self.cell_size - self.door_height
        y = self.door_height
        width = self.door_height
        height = self.door_width
        color = self.color_right if self.exits[2] else self.color_no_exit

        return x, y, width, height, color

    @property
    def __up_door(self):
        x = self.door_height
        y = 0
        width = self.door_width
        height = self.door_height
        color = self.color_up if self.exits[3] else self.color_no_exit

        return x, y, width, height, color

    def blit(self, background):
        """blit the Ball on the background"""
        background.blit(self.surface, (self.x, self.y))
