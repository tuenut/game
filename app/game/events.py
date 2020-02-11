import logging
import pygame  # type: ignore

from config import WEST, EAST, NORTH, SOUTH

logger = logging.getLogger(__name__)


class GameEvents:
    """Класс обработки событий в процессе игры."""

    def __init__(self, *args, **kwargs):
        on_player_move = kwargs.get('on_player_move')
        if on_player_move:
            self.on_player_move = on_player_move.get('callback', )
            self.on_player_move_args = on_player_move.get('args', [])
            self.on_player_move_kwargs = on_player_move.get('kwargs', {})

    def check(self, events):
        for event in events:
            self.on_event(event)

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.on_press_key(event)
        elif event.type == pygame.USEREVENT:
            logger.debug(event.type)
            self.on_player_move(event.character, event.direction)

    def on_press_key(self, event):
        if event.key == pygame.K_LEFT:
            self.on_player_move(*self.on_player_move_args, WEST, **self.on_player_move_kwargs)
        elif event.key == pygame.K_RIGHT:
            self.on_player_move(*self.on_player_move_args, EAST, **self.on_player_move_kwargs)
        elif event.key == pygame.K_UP:
            self.on_player_move(*self.on_player_move_args, NORTH, **self.on_player_move_kwargs)
        elif event.key == pygame.K_DOWN:
            self.on_player_move(*self.on_player_move_args, SOUTH, **self.on_player_move_kwargs)

    def default_callback(self, *args, **kwargs):
        print("Default callback: do nothing.")