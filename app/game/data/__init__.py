from config import REPO_TYPE
from abstractions.data import ABCDataController

__all__ = ['get_data_object']


def get_data_object() -> ABCDataController:
    if REPO_TYPE == "JSON":
        from app.game.data.__DEPRECATED__jsonrepo import DataController
        from config import JSON_REPO as source
    elif REPO_TYPE == "SQLITE":
        from app.game.data.peeweerepo import DataController
        from config import SQLITE_REPO as source
    else:
        raise Exception("Unknown data repository type <{}>.".format(REPO_TYPE))

    return DataController(source=source)
