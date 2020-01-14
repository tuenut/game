from data.abstractions.objects import ABCObjectRepository

class ObjectRepository(ABCObjectRepository):
    @property
    def name(self):
        raise NotImplementedError

    @property
    def type(self):
        raise NotImplementedError

    @property
    def location(self):
        raise NotImplementedError