from config import REPO_TYPE
from data.abstractions.world import ABCWorldData

if REPO_TYPE == "json":
    from data.jsonrepo import JSONWorldData as WorldDataClass
    from config import JSON_REPO as source

__all__ = ['get_data_object']


def get_data_object():
    return WorldDataClass(source)  # type: ABCWorldData
