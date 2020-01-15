from app.render.objects.door import DoorRenderObject


class LocationExitsRenderObject:
    color_left = (255, 100, 100)
    color_right = (100, 255, 100)
    color_up = (100, 100, 255)
    color_down = (255, 255, 100)
    color_no_exit = (50, 50, 50)

    def __init__(self, surface, exits, cell_size, door_width, door_height):
        self.__exits = exits
        self.__width = door_width
        self.__height = door_height
        self.__cell_size = cell_size

        self.down = DoorRenderObject(surface, *self.__down_door)
        self.left = DoorRenderObject(surface, *self.__left_door)
        self.right = DoorRenderObject(surface, *self.__right_door)
        self.up = DoorRenderObject(surface, *self.__up_door)

    @property
    def __down_door(self):
        x = self.__height
        y = self.__cell_size - self.__height
        width = self.__width
        height = self.__height
        color = self.color_down if self.__exits[0] else self.color_no_exit

        return x, y, width, height, color

    @property
    def __left_door(self):
        x = 0
        y = self.__height
        width = self.__height
        height = self.__width
        color = self.color_left if self.__exits[1] else self.color_no_exit

        return x, y, width, height, color

    @property
    def __right_door(self):
        x = self.__cell_size - self.__height
        y = self.__height
        width = self.__height
        height = self.__width
        color = self.color_right if self.__exits[2] else self.color_no_exit

        return x, y, width, height, color

    @property
    def __up_door(self):
        x = self.__height
        y = 0
        width = self.__width
        height = self.__height
        color = self.color_up if self.__exits[3] else self.color_no_exit

        return x, y, width, height, color
