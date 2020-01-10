import pygame

from app.view.cell import LocationCell


class View:
    """Класс "представления" для всего, что касается как минимум графики игры.
    Отрисовка состояния игрового поля и объектов на нем.

    """
    background = (0, 0, 0)

    def __init__(self, world_map, width=640, height=640, fps=30, ):
        self.world_map = world_map

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)

        self.surface = pygame.Surface(self.screen.get_size()).convert()
        self.surface.fill(self.background)

        self.draw_cells()

    def draw_cells(self):
        x = 5
        y = 5

        cell_size = LocationCell.cell_size

        for x_row in self.world_map.grid:
            for location in x_row:
                location_cell = LocationCell(exits=location.exits, x=x, y=y)
                location_cell.blit(self.surface)
                y += cell_size+1

            x += cell_size+1
            y = 5


    def loop(self):
        pygame.display.flip()
        self.screen.blit(self.surface, (0, 0))