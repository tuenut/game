import pygame

from app.view import View
from app.events import Events
from app.state import State


class App:
    def __init__(self, world_map):
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")

        self.world_map = world_map

        self.state = State(True)
        self.events = Events(on_exit=self.end_mainloop)
        self.view = View(self.world_map)

    def mainloop(self):
        while self.state.run:
            self.events.check()
            self.view.loop()

        self.exit()

    def end_mainloop(self):
        self.state.run = False

    def exit(self):
        pygame.quit()