from app.render import Render
from app.game.events import GameEvents
from state import GameState



import logging
logger = logging.getLogger(__name__)


__all__ = ['Game']


class Game:
    """Класс игры.
    Описывает все поведение игры и управляет взаимодействием сущностей игры.
    """

    def __init__(self, *args, **kwargs):
        logger.debug("Init Game...")

        self.state = GameState()
        self.render = Render()

        self.__configure_events()

    def __configure_events(self):
        self.events = GameEvents(
            on_down=lambda: print("Down"),
            on_left=lambda: print("Left"),
            on_right=lambda: print("Right"),
            on_up=lambda: print("Up"),
        )

    def update(self, events):
        self.events.check(events)
        # todo self.world.update()
        self.render.update(self.state.locations)

