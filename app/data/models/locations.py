import peewee

from app.data.models.bases import EntityBinding
from config import CELL_SIZE


class Location(EntityBinding):
    position_x = peewee.IntegerField(default=None, null=True)
    position_y = peewee.IntegerField(default=None, null=True)
    size_x = peewee.IntegerField(default=CELL_SIZE)
    size_y = peewee.IntegerField(default=CELL_SIZE)

    @property
    def size(self):
        return self.size_x, self.size_y

    @property
    def position(self):
        return self.position_x, self.position_y

    def load(self, data: dict):
        raise NotImplementedError

    def dump(self) -> dict:
        return {
            'uuid': self.uuid,
            'type': self.type,
            'name': self.name,
            'position': self.position,
            'size': self.size
        }
