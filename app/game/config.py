import pygame
from abstractions.data import SOUTH, NORTH, EAST, WEST

NAVIGATION = {
    pygame.K_LEFT: WEST,
    pygame.K_RIGHT: EAST,
    pygame.K_UP: NORTH,
    pygame.K_DOWN: SOUTH,
}
