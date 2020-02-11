import peewee

from app.game.data.peeweerepo.bases import EntityBinding
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
    def objects(self):
        raise NotImplementedError

    def load(self, data: dict):
        raise NotImplementedError

    def dump(self) -> dict:
        raise NotImplementedError