import pygame  # type: ignore

from render.locations.locationobject import LocationRender
from render.world import WorldRender
from state import GameStateController

import logging

logger = logging.getLogger(__name__)


class Render:
    BACKGROUND = (0, 0, 0)

    def __init__(self, game_state: GameStateController, width=640, height=640, fps=30, ):
        logger.debug("Init Render...")

        self.__game_state = game_state

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)

        self.surface = pygame.Surface(self.screen.get_size()).convert()
        self.surface.fill(self.BACKGROUND)

        self.world = WorldRender(self.surface, self.__game_state.locations, self.__game_state.characters)

    def update(self):
        pygame.display.flip()
        self.surface.fill(self.BACKGROUND)
        self.world.update()
        self.screen.blit(self.surface, (0, 0))


