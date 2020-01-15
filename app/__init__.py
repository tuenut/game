import logging
import pygame

from time import sleep

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
    __playtime = 0.0

    __HINT_IN_TITLE = "Press ESC to quit"

    def __init__(self):
        logger.debug("Init App...")

        self.__title = self.__HINT_IN_TITLE

        self.__init_pygame()
        self.__configure_events()

        self.state = State()

        self.game = Game()

    def __configure_events(self):
        self.events = AppEvents(
            on_exit=self._end_mainloop,
        )

    def __init_pygame(self):
        pygame.display.init()  # pygame.init() has 100% CPU usage

        self.__clock = pygame.time.Clock()

        pygame.display.set_caption(self.__title)

    def run(self):
        self.state.run = True

        # self.__fake_loading()

        self._mainloop()

        self._exit()

    def __fake_loading(self):
        print("Loading imitation...")
        sleep(1)
        print("Still imitate...")
        sleep(1)
        print("Last two seconds... Honestly :)")
        sleep(2)

        print("Let's the Game begin!")

    def _mainloop(self):
        while self.state.run:
            current_events = pygame.event.get()

            self._fps_update()

            self.events.check(current_events)

            self.game.update(current_events)

    def _fps_update(self):
        milliseconds = self.__clock.tick(self.FPS)
        self.__playtime += milliseconds / 1000.0

        fps = "FPS: {0:.2f}   Playtime: {1:.2f}".format(self.__clock.get_fps(), self.__playtime)
        self.__title = "{title}. {fps}".format(title=self.__HINT_IN_TITLE, fps=fps)

        pygame.display.set_caption(self.__title)

    def _end_mainloop(self):
        self.state.run = False

    def _exit(self):
        pygame.quit()
