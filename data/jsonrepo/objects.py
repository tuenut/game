from data.abstractions.objects import ABCObjectRepository

class ObjectData(ABCObjectRepository):
    @property
    def name(self):
        raise NotImplementedError

    @property
    def type(self):
        raise NotImplementedError

    @property
    def location_id(self):
        raise NotImplementedError