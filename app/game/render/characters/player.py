import logging
import pygame  # type: ignore

from abstractions.data import PLAYABLE_CHARACTER, NON_PLAYABLE_CHARACTER
from app.game.render.config import CELL_SIZE, CELL_BORDER, MAP_MARGIN_Y, MAP_MARGIN_X, EXIT_HEIGHT
from abstractions.gamestate import ABCGameStateCharacter

logger = logging.getLogger(__name__)


class PlayerRenderObject:
    """Класс отвечает за отрисовку одной двери в ячейке/на локации."""

    COLORS = {
        PLAYABLE_CHARACTER: (255, 200, 0),
        NON_PLAYABLE_CHARACTER: (255, 0, 200, )
    }

    @classmethod
    def get_x(cls, x):
        return x * (CELL_SIZE + CELL_BORDER) + MAP_MARGIN_X

    @classmethod
    def get_y(cls, y):
        return y * (CELL_SIZE + CELL_BORDER) + MAP_MARGIN_X

    @classmethod
    def get_coordinates(cls, x, y):
        return cls.get_x(x), cls.get_y(y)

    def __init__(self, parent_surface, character_state: ABCGameStateCharacter):
        self.parent_surface = parent_surface

        self.surface = pygame.Surface((CELL_SIZE, CELL_SIZE)).convert()
        self.surface.fill((255, 0, 255))
        self.surface.set_colorkey((255, 0, 255))
        self.surface = self.surface.convert_alpha()

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
        return self.get_x(self.__character.location.position[0])

    @property
    def y(self):
        return self.get_y(self.__character.location.position[1])

    def blit(self):
        self.parent_surface.blit(self.surface, (self.x, self.y))

    def draw(self):
        rect = ((CELL_SIZE - self.margin) / 2, (CELL_SIZE - self.margin) / 2, self.margin, self.margin)
        pygame.draw.rect(self.surface, self.COLORS[self.__character.type], rect)

    def update(self):
        self.blit()
        self.draw()
