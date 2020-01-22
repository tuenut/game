import logging
import pygame  # type: ignore

from app.game.render.config import CELL_SIZE, CELL_BORDER, MAP_MARGIN_Y, MAP_MARGIN_X, EXIT_HEIGHT
from abstractions.gamestate import ABCGameStateCharacter

logger = logging.getLogger(__name__)


class PlayerRenderObject:
    """Класс отвечает за отрисовку одной двери в ячейке/на локации."""

    color = (255, 200, 0)

    def __init__(self, parent_surface, character_state: ABCGameStateCharacter):
        self.parent_surface = parent_surface

        self.surface = pygame.Surface((CELL_SIZE, CELL_SIZE)).convert()
        self.surface.fill((255, 0, 255))
        self.surface.set_colorkey((255, 0, 255))
        self.surface.convert_alpha()

        self.__character = character_state

        self.update()

    @property
    def width(self):
        return EXIT_HEIGHT

    @property
    def margin(self):
        return EXIT_HEIGHT * 2

    @property
    def x(self):
        return self.__character.location.coordinates[0] * CELL_SIZE + MAP_MARGIN_X

    @property
    def y(self):
        return self.__character.location.coordinates[1] * CELL_SIZE + MAP_MARGIN_Y

    def blit(self):
        self.parent_surface.blit(self.surface, (self.x, self.y))

    def draw(self):
        rect = ((CELL_SIZE - self.margin) / 2, (CELL_SIZE - self.margin) / 2, self.margin, self.margin)
        pygame.draw.rect(self.surface, self.color, rect)

    def update(self):
        self.blit()
        self.draw()
