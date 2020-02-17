from django.db import models

# Create your models here.
from app.data.orm.entities.models import BaseEntityModel


class Location(BaseEntityModel):
    position_x = models.IntegerField(default=0)
    position_y = models.IntegerField(default=0)
    size_x = models.IntegerField(default=0)
    size_y = models.IntegerField(default=0)

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