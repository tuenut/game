import peewee

from app.data.models.bases import EntityBinding
from app.data.models.locations import Location


class Object(EntityBinding):
    location = peewee.ForeignKeyField(Location, default=None, null=True, backref='objects')
    position_x = peewee.IntegerField(default=None, null=True)
    position_y = peewee.IntegerField(default=None, null=True)
    size_x = peewee.IntegerField(default=0)
    size_y = peewee.IntegerField(default=0)

    @property
    def position(self):
        return self.position_x, self.position_y

    @property
    def size(self):
        return self.size_x, self.size_y

    def load(self, data: dict):
        raise NotImplementedError

    def dump(self) -> dict:
        return {
            'uuid': self.uuid,
            'type': self.type,
            'name': self.name,
            'position': self.position,
            'size': self.size,
            'location': self.location.uuid if self.location else None
        }

class LocationJunction(Object):
    next_location = peewee.ForeignKeyField(Location, default=None, null=True, backref='junctions_to')

    def load(self, data: dict):
        raise NotImplementedError

    def dump(self) -> dict:
        raise NotImplementedError