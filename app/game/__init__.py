from app.game.events import GameEvents
from data import get_data_object
from state import GameStateController
from render import Render

import logging

logger = logging.getLogger(__name__)

__all__ = ['Game']


class Game:
    """Класс игры.
    Описывает все поведение игры и управляет взаимодействием сущностей игры.
    """

    def __init__(self, *args, **kwargs):
        logger.debug("Init Game...")

        self.data = get_data_object()
        self.state = GameStateController(data=self.data)
        self.render = Render(game_state=self.state)

        self.__configure_events()

    def __configure_events(self):
        self.events = GameEvents(
            on_player_move={
                'callback': self.state.move_object,
                'args': [self.state.characters.player, ],
                'kwargs': {}
            }
        )

    def update(self, events):
        self.events.check(events)
        # todo: self.state.update()
        self.render.update()
