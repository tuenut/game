import logging
import pygame # type: ignore

from app.game import Game
from app.events import AppEvents
from app.state import State

logger = logging.getLogger(__name__)


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

    FPS = 30
    _playtime = 0.0

    _HINT_IN_TITLE = "Press ESC to quit"

    def __init__(self):
        logger.debug("Init App...")

        self.title = self._HINT_IN_TITLE

        self.state = State()
        self.state.run()

        self._init_pygame()
        self.events = AppEvents(
            on_exit=self.state.stop,
        )

        self.game = Game()

    def run(self):
        self.__mainloop()
        self.exit()

    def __mainloop(self):
        while self.state.runned:
            current_events = pygame.event.get()

            self._fps_update()

            self.events.check(current_events)

            self.game.update(current_events)

    def exit(self):
        pygame.quit()

    def _init_pygame(self):
        pygame.display.init()  # pygame.init() has 100% CPU usage
        self._clock = pygame.time.Clock()
        pygame.display.set_caption(self.title)

    def _fps_update(self):
        milliseconds = self._clock.tick(self.FPS)
        self._playtime += milliseconds / 1000.0

        fps = "FPS: {0:.2f}   Playtime: {1:.2f}".format(self._clock.get_fps(), self._playtime)
        self.title = "{title}. {fps}".format(title=self._HINT_IN_TITLE, fps=fps)

        pygame.display.set_caption(self.title)
