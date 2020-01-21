import pygame # type: ignore

from app.events import ABCEvents
from abstractions.data import WEST, EAST, NORTH, SOUTH


class GameEvents(ABCEvents):
    """Класс обработки событий в процессе игры."""

    def __init__(self, *args, **kwargs):
        on_player_move = kwargs.get('on_player_move')
        if on_player_move:
            self.on_player_move = on_player_move.get('callback', self.default_callback)
            self.on_player_move_args = on_player_move.get('args', [])
            self.on_player_move_kwargs = on_player_move.get('kwargs', {})



    def check(self, events):
        for event in events:
            self.on_event(event)

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.on_press_key(event)

    def on_press_key(self, event):
        if event.key == pygame.K_LEFT:
            self.on_player_move(*self.on_player_move_args, WEST, **self.on_player_move_kwargs)
        elif event.key == pygame.K_RIGHT:
            self.on_player_move(*self.on_player_move_args, EAST, **self.on_player_move_kwargs)
        elif event.key == pygame.K_UP:
            self.on_player_move(*self.on_player_move_args, NORTH, **self.on_player_move_kwargs)
        elif event.key == pygame.K_DOWN:
            self.on_player_move(*self.on_player_move_args, SOUTH, **self.on_player_move_kwargs)
