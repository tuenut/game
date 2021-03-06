import logging

import pygame

from app.appstate import AppState
from app.events import EventManager
from app.game import Game


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

    logger = logging.getLogger(__name__)

    def __init__(self):
        self.logger.debug("Init App...")

        self.title = self._HINT_IN_TITLE

        self.state = AppState()

        self.__init_pygame()

        self.events = EventManager()
        self.events.subscribe(event_type=pygame.QUIT, callback=self.state.stop, )
        self.events.subscribe(event_type=pygame.KEYDOWN, callback=self.state.stop, conditions={"key": pygame.K_q})
        self.events.subscribe(event_type=pygame.KEYDOWN, callback=self.state.stop, conditions={"key": pygame.K_ESCAPE})

        self.game = Game()

    def run(self):
        self.state.run()
        self.__mainloop()
        self.exit()

    def exit(self):
        pygame.quit()

    def __mainloop(self):
        while self.state.runned:
            self.__fps_update()

            self.events.check_events()

            self.game.update()

    def __init_pygame(self):
        pygame.display.init()  # pygame.init() make 100% CPU usage
        self._clock = pygame.time.Clock()
        pygame.display.set_caption(self.title)

    def __fps_update(self):
        milliseconds = self._clock.tick(self.FPS)
        self._playtime += milliseconds / 1000.0

        fps = "FPS: {0:.2f}   Playtime: {1:.2f}".format(self._clock.get_fps(), self._playtime)
        self.title = "{title}. {fps}".format(title=self._HINT_IN_TITLE, fps=fps)

        pygame.display.set_caption(self.title)
