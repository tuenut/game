import pygame

from app.events import ABCEvents
from data.abstractions import WEST, EAST, NORTH, SOUTH


class GameEvents(ABCEvents):
    """Класс обработки событий в процессе игры."""

    def __init__(self, *args, **kwargs):
        self.on_player_move = kwargs.get('on_player_move', self.default_callback)
        self.player_id = args[0]

    def check(self, events):
        for event in events:
            self.on_event(event)

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.on_press_key(event)

    def on_press_key(self, event):
        if event.key == pygame.K_LEFT:
            self.on_player_move(self.player_id, WEST)
        elif event.key == pygame.K_RIGHT:
            self.on_player_move(self.player_id, EAST)
        elif event.key == pygame.K_UP:
            self.on_player_move(self.player_id, NORTH)
        elif event.key == pygame.K_DOWN:
            self.on_player_move(self.player_id, SOUTH)
