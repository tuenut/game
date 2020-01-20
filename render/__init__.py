import pygame

from render.locations import LocationRender
from state import GameState

import logging

logger = logging.getLogger(__name__)


class Render:
    background = (0, 0, 0)
    margin_left = 5
    margin_right = 5

    def __init__(self, game_state: GameState, width=640, height=640, fps=30, ):
        logger.debug("Init Render...")

        self.__game_state = game_state

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)

        self.surface = pygame.Surface(self.screen.get_size()).convert()
        self.surface.fill(self.background)

        self.locations = []  # type: [LocationRender]

        self.draw_cells()

    def draw_cells(self, ):
        cell_size = LocationRender.cell_size

        for location in self.__game_state.locations:
            x = location.coordinates[0] * (cell_size + 1) + self.margin_left
            y = location.coordinates[1] * (cell_size + 1) + self.margin_right

            location_cell = LocationRender(self.surface, location, x_pos=x, y_pos=y)
            location_cell.blit()

            self.locations.append(location_cell)

    def update(self):
        pygame.display.flip()
        for location in self.locations:
            location.update()
        self.screen.blit(self.surface, (0, 0))
