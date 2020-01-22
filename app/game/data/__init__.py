from app.config import REPO_TYPE
from abstractions.data import ABCDataController

if REPO_TYPE == "json":
    from app.game.data.jsonrepo import JSONDataController as DataClass
    from app.config import JSON_REPO as source

__all__ = ['get_data_object']


def get_data_object() -> ABCDataController:
    return DataClass(source=source)
