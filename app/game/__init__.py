import pygame
import logging

from app.events import EventManager
from .data import get_data_object
from .state import GameStateController
from .render import Render
from .config import NAVIGATION

__all__ = ['Game']


class Game:
    """Класс игры.
    Описывает все поведение игры и управляет взаимодействием сущностей игры.
    """
    logger = logging.getLogger(__name__)

    def __init__(self, *args, **kwargs):
        self.logger.debug("Init Game...")

        self.data = get_data_object()

        self.state = GameStateController(data=self.data)
        self.render = Render(game_state=self.state)

        self.events = EventManager()
        self.events.subscribe(event_type=pygame.KEYDOWN, callback=self.move_player, kwargs=["key"])

    def move_player(self, key):
        self.state.move_object(self.state.characters.player, NAVIGATION[key])

    def update(self):
        self.state.update()
        self.render.update()
