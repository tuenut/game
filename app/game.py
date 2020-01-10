from app.view import View
from universe.interfaces.simplestore import WorldRepository
from universe import World

class Game:
    """Класс игры.
    Описывает все поведение игры и управляет взаимодействием сущностей игры.
    """
    __world = WorldRepository()

    def __init__(self):
        self.world = World(self.__world)

        self.view = View(self.world)


    def run(self):
        self.view.loop()