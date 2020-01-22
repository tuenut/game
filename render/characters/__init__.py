import logging

from abstractions.data import PLAYABLE_CHARACTER
from abstractions.gamestate import ABCGameStateCharactersManager
from render.config import CELL_SIZE, CELL_BORDER, MAP_MARGIN_Y, MAP_MARGIN_X, EXIT_HEIGHT
from render.characters.player import PlayerRenderObject

logger = logging.getLogger(__name__)


class CharactersRenderManager:
    def __init__(self, parent_surface, character_objects: ABCGameStateCharactersManager):
        self.parent_surface = parent_surface
        self.__characters_state = character_objects
        self.characters = []

        self.__init_draw()

    def __init_draw(self):
        for character in self.__characters_state:
            self.characters.append(PlayerRenderObject(self.parent_surface, character))

    def update(self):
        for character in self.characters:
            character.update()
