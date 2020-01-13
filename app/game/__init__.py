from app.view import View
from universe import World
from .events import GameEvents


class Game:
    """Класс игры.
    Описывает все поведение игры и управляет взаимодействием сущностей игры.
    """

    def __init__(self):
        self.world = World()
        self.view = View(self.world)
        self.__configure_events()

    def __configure_events(self):
        self.events = GameEvents(
            on_down=lambda : print("Down"),
            on_left=lambda : print("Left"),
            on_right=lambda : print("Right"),
            on_up=lambda : print("Up"),
        )

    def update(self, events):
        self.events.check(events)
        self.view.update()