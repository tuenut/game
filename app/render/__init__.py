import pygame

from app.render.locations import LocationRenderObject

import logging

logger = logging.getLogger(__name__)


class Render:
    """Класс "представления" для всего, что касается как минимум графики игры.
    Отрисовка состояния игрового поля и объектов на нем.

    """
    background = (0, 0, 0)
    margin_left = 5
    margin_right = 5

    def __init__(self, width=640, height=640, fps=30, ):
        logger.debug("Init Render...")

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)

        self.surface = pygame.Surface(self.screen.get_size()).convert()
        self.surface.fill(self.background)

    def draw_cells(self, data):
        cell_size = LocationRenderObject.cell_size

        for location in data:
            x = location.coordinates[0] * (cell_size + 1) + self.margin_left
            y = location.coordinates[1] * (cell_size + 1) + self.margin_right

            location_cell = LocationRenderObject(location, x_pos=x, y_pos=y)
            location_cell.blit(self.surface)

    def update(self, data):
        self.draw_cells(data)

        pygame.display.flip()
        self.screen.blit(self.surface, (0, 0))
