from data.abstractions.objects import ABCObjectRepository


class ObjectData(ABCObjectRepository):
    def __init__(self, **kwargs):
        pass

    @property
    def data_fields(self):
        raise NotImplementedError

    @property
    def name(self):
        raise NotImplementedError

    @property
    def type(self):
        raise NotImplementedError

    @property
    def location(self):
        raise NotImplementedError
