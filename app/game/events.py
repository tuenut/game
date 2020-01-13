import pygame

from app.events import ABCEvents


class GameEvents(ABCEvents):
    """Класс обработки событий в процессе игры."""

    def __init__(self, *args, **kwargs):
        self.on_left = kwargs.get('on_left', self.default_callback)
        self.on_right = kwargs.get('on_right', self.default_callback)
        self.on_up = kwargs.get('on_up', self.default_callback)
        self.on_down = kwargs.get('on_down', self.default_callback)

    def check(self, events):
        for event in events:
            self.on_event(event)

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.on_press_key(event)

    def on_press_key(self, event):
        if event.key == pygame.K_LEFT:
            self.on_left()
        elif event.key == pygame.K_RIGHT:
            self.on_right()
        elif event.key == pygame.K_UP:
            self.on_up()
        elif event.key == pygame.K_DOWN:
            self.on_down()
