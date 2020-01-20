from app.game.events import GameEvents
from data import get_data_object
from state import GameState
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
        self.state = GameState(data=self.data)
        self.render = Render(game_state=self.state)

        self.__configure_events()

    def __configure_events(self):
        self.events = GameEvents(
            self.state.player,
            on_player_move=self.state.move_object,
        )

    def update(self, events):
        self.events.check(events)
        self.state.update()
        self.render.update()
