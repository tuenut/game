import pygame


class DoorRenderObject:
    """Класс отвечает за отрисовку одной двери в ячейке/на локации."""

    def __init__(self, surface, x, y, width, height, color):
        self.x = x
        self.y = y
        self.surface = surface
        self.height = height
        self.width = width
        self.color = color

        self.draw()

    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.width, self.height))
