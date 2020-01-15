from config import REPO_TYPE
from data.abstractions import ABCWorldData

if REPO_TYPE == "json":
    from data.jsonrepo import JSONWorldData as WorldDataClass
    from config import JSON_REPO as source

__all__ = ['WorldData']

WorldData = WorldDataClass(source)  #type: ABCWorldData
