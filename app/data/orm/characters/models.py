from django.db import models

# Create your models here.
from app.data.orm.entities.models import BaseEntityModel


class Character(BaseEntityModel):
    location = models.ForeignKey('locations.Location', default=None, null=True, on_delete=models.SET_DEFAULT)
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    size_x = models.IntegerField()
    size_y = models.IntegerField()

    @property
    def position(self):
        return self.position_x, self.position_y

    @property
    def size(self):
        return self.size_x, self.size_y

    def load(self, data: dict):
        pass

    def dump(self) -> dict:
        pass