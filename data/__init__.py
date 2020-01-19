from app.config import REPO_TYPE
from data.abstractions.world import ABCWorldMapData

if REPO_TYPE == "json":
    from data.jsonrepo import JSONData as DataClass
    from app.config import JSON_REPO as source

__all__ = ['get_data_object']


def get_data_object():
    return DataClass(source=source)  # type: ABCWorldMapData
