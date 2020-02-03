from app.config import REPO_TYPE
from abstractions.data.datacontroller import ABCDataController

if REPO_TYPE == "JSON":
    from app.game.data.jsonrepo import DataController
    from app.config import JSON_REPO as source
elif REPO_TYPE == "SQLITE":
    from app.game.data.peeweerepo import DataController

__all__ = ['get_data_object']


def get_data_object() -> ABCDataController:
    return DataController(source=source)
