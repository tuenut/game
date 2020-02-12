import logging

import pygame

from app.data import DataController
from app.events import EventManager, MOVE_CHARACTER
from app.gamestate import GameStateController
from app.render import Render
from config import NAVIGATION


class Game:
    """Класс игры.
    Описывает все поведение игры и управляет взаимодействием сущностей игры.
    """
    logger = logging.getLogger(__name__)

    def __init__(self, *args, **kwargs):
        self.logger.debug("Init Game...")

        self.data = DataController()

        self.state = GameStateController(data=self.data)
        self.render = Render(game_state=self.state)

        self.events = EventManager()
        self.events.subscribe(
            event_type=pygame.KEYDOWN,
            callback=self.move_player,
            conditions={"key": [pygame.K_DOWN, pygame.K_UP, pygame.K_RIGHT, pygame.K_LEFT]},
            kwargs=["key"]
        )

        self.events.subscribe(
            pygame.USEREVENT,
            callback=self.state.move_character,
            subtype=MOVE_CHARACTER,
            kwargs=["direction", "character"]
        )

    def move_player(self, key):
        self.state.move_object(self.state.characters.player, NAVIGATION[key])

    def update(self):
        self.state.update()
        self.render.update()
