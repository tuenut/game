import pygame

from app.game import Game
from app.events import Events
from app.state import State


class App:
    """
    Класс приложения.
    Отвечает за обработку состояния приложения, событий и прочего, что связано с самым верхним уровнем.
    Запускает Игру.
    Предполагается, что будет какое-то меню, и в режиме меню Игра не выполняется.
    """
    state = None
    events = None
    game = None
    menu = None

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")

        self.state = State(True)
        self.game = Game()
        self.events = Events(
            on_exit=self.end_mainloop,
        )

    def mainloop(self):
        while self.state.run:
            self.events.check()
            self.game.run()

        self.exit()

    def end_mainloop(self):
        self.state.run = False

    def exit(self):
        pygame.quit()

