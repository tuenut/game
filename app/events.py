import pygame
from abc import ABC, abstractmethod


class ABCEvents(ABC):
    @abstractmethod
    def on_event(self, event):
        ...

    def check(self, events):
        for event in events:
            self.on_event(event)

    def default_callback(self, *args, **kwargs):
        print("Default callback: do nothing.")


class AppEvents(ABCEvents):
    """Класс обработки событий приложения."""

    def __init__(self, *args, **kwargs):
        self.on_exit = kwargs.get('on_exit', self.default_callback)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.on_exit()

        elif event.type == pygame.KEYDOWN:
            self.on_press_key(event)

        return event

    def on_press_key(self, event):
        if event.key in (pygame.K_ESCAPE, pygame.K_q):
            self.on_exit()
