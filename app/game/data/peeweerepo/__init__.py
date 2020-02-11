from app.game.data.peeweerepo.bases import database, EntityBinding, GameEntity
from app.game.data.peeweerepo.characters import Character
from app.game.data.peeweerepo.locations import Location

from config import PLAYABLE_CHARACTER_TYPE, NON_PLAYABLE_CHARACTER_TYPE
from app.utils.logger import configure_logger


class DataController:
    pass


if __name__ == "__main__":
    logger = configure_logger()

    with database.connection_context():
        database.drop_tables([Location, GameEntity, Character])
        logger.debug(database.get_tables())

        if not database.get_tables():
            database.create_tables([Location, GameEntity, Character])

            locations = [
                {
                    'position_x': 0,
                    'position_y': 0,
                    'ingame_type': "location"
                },
                {
                    'position_x': 1,
                    'position_y': 1,
                    'ingame_type': "location"
                },
            ]

            for location in locations:
                Location.create(**location)

            characters = [
                {
                    'ingame_type': PLAYABLE_CHARACTER_TYPE,
                    'ingame_name': 'test_player',
                },
                {
                    'ingame_type': NON_PLAYABLE_CHARACTER_TYPE,
                    'ingame_name': 'test_npc',
                },
            ]

            for character in characters:
                Character.create(**character)
