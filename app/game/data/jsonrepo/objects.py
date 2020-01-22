from abstractions.data import ABCDataObject


class ObjectData(ABCDataObject):
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
