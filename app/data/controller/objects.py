from abstractions.data import ABCData

from app.data.models import Object


class ObjectsDataController(ABCData):
    def load(self, data: dict):
        raise NotImplementedError

    def dump(self) -> list:
        return [obj.dump() for obj in self.objects]

    def __init__(self):
        self.objects = Object.select()
