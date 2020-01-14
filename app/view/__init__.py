import pygame

from app.view.locationcell import LocationCell

from app.logger import make_logger, LOG_LEVEL
logger = make_logger(__name__, LOG_LEVEL)


class View:
    """Класс "представления" для всего, что касается как минимум графики игры.
    Отрисовка состояния игрового поля и объектов на нем.

    """
    background = (0, 0, 0)
    margin_left = 5
    margin_right = 5

    def __init__(self, world_map, width=640, height=640, fps=30, ):
        self.world_map = world_map

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)

        self.surface = pygame.Surface(self.screen.get_size()).convert()
        self.surface.fill(self.background)

    def draw_cells(self):
        cell_size = LocationCell.cell_size

        for location in self.world_map.locations:
            x = location.coordinates[0] * (cell_size+1) + self.margin_left
            y = location.coordinates[1] * (cell_size+1) + self.margin_right

            location_cell = LocationCell(location, x_pos=x, y_pos=y)
            location_cell.blit(self.surface)

    def update(self):
        self.draw_cells()

        pygame.display.flip()
        self.screen.blit(self.surface, (0, 0))
