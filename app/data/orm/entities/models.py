import uuid

from django.db import models

# Create your models here.
class Entity(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class EntityType(models.Model):
    value = models.IntegerField(default=0, unique=True)
    description = models.CharField(max_length=255, default=None, null=True)


class BaseEntityModel(models.Model):
    uuid = models.OneToOneField('entiti.Entity', null=False, on_delete=models.CASCADE)
    type = models.ForeignKey('entiti.EntityType', default=None, null=True, on_delete=models.SET_DEFAULT)
    name = models.CharField(max_length=32, default=None, null=True)

    def load(self, data: dict):
        raise NotImplementedError

    def dump(self) -> dict:
        raise NotImplementedError

    class Meta:
        abstract = True