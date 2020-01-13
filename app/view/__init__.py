import pygame

from app.view.locationcell import LocationCell


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

        self.__init_draw_cells()

    def __init_draw_cells(self):
        # todo косяк!!! создание новых объектов в каждом цикле. Хотелось бы работать с тем, что есть.
        cell_size = LocationCell.cell_size

        for content in self.world_map.locations:
            x = content['coordinates'][0] * (cell_size+1) + self.margin_left
            y = content['coordinates'][1] * (cell_size+1) + self.margin_right

            location_cell = LocationCell(content, x_pos=x, y_pos=y)
            location_cell.blit(self.surface)

    def update(self):
        self.rerender_cells_if_nesessary()

        pygame.display.flip()
        self.screen.blit(self.surface, (0, 0))

    def rerender_cells_if_nesessary(self):
        pass