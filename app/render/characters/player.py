import pygame


class PlayerRenderObject:
    """Класс отвечает за отрисовку одной двери в ячейке/на локации."""

    color = (200, 200, 0)

    def __init__(self, surface, size, magrin):
        self.surface = surface

        self.size = size
        self.width = int(self.size * 0.1)
        self.margin = magrin * 1.1 + self.width

        self.draw()

    def draw(self):
        start_pos = (self.margin, self.margin)
        end_pos = (self.size - self.margin, self.size - self.margin)
        pygame.draw.line(self.surface, self.color, start_pos, end_pos, self.width)

        start_pos = (self.size - self.margin, self.margin)
        end_pos = (self.margin, self.size - self.margin)
        pygame.draw.line(self.surface, self.color, start_pos, end_pos, self.width)
