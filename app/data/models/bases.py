import copy
import json
import logging
import peewee

from datetime import datetime as dt
from hashlib import sha3_256

database = peewee.SqliteDatabase(None)


class BaseModel(peewee.Model):
    logger = logging.getLogger(__name__)

    class Meta:
        database = database

    def load(self, data: dict):
        raise NotImplementedError

    def dump(self) -> dict:
        raise NotImplementedError


class EntityTypes(BaseModel):
    value = peewee.IntegerField(default=0, unique=True)
    description = peewee.CharField(max_length=255, default=None, null=True)


class Entity(BaseModel):
    uuid = peewee.CharField(max_length=64, default=None, null=True, unique=True)
    name = peewee.CharField(max_length=16, default=None, null=True, )
    type = peewee.ForeignKeyField(EntityTypes, default=None, null=True, backref="entities")


class EntityBinding(BaseModel):
    entity = peewee.ForeignKeyField(Entity, default=None, null=True, unique=True)
    created = peewee.DateTimeField(default=dt.now)

    @property
    def uuid(self):
        return self.entity.uuid

    @property
    def type(self):
        return self.entity.type.value

    @property
    def name(self):
        return self.entity.name

    @classmethod
    def create(cls, **query):
        if query.get('uuid'):
            raise Exception("Field <ingame_id> can not provide directly, only by automatic calculate.")

        self_class_kwargs = {key: val for key, val in query.items() if key in cls._meta.fields.keys()}
        instance = super().create(**self_class_kwargs)

        instance.entity = cls._create_entity_binding(instance, **query)
        instance.save()

        return instance

    @classmethod
    def _create_entity_binding(cls, instance, **query):
        entity_type = EntityTypes.get(value=query.get('type'))
        name = query.get('name')

        serialized_data = {
            field_name: getattr(instance, field_name)
            for field_name, field_type in cls._meta.fields.items()
            if not isinstance(field_type, peewee.ForeignKeyField)
        }
        serialized_data.update(
            {
                'type': query.get('type'),
                'name': name,
                'created': serialized_data['created'].timestamp()
            }
        )

        uuid = cls.generate_object_id(**serialized_data)

        try:
            entity = Entity.create(uuid=uuid, type=entity_type, name=name)
        except Exception as e:
            cls.logger.exception("Some Exception while use overrided creation method.")
            raise e

        return entity

    @staticmethod
    def generate_object_id(**kwargs):
        serialized_data = copy.deepcopy(kwargs)

        try:
            serialized_data.pop('uuid')
        except KeyError:
            pass

        stringified_object = json.dumps(serialized_data).encode()
        object_id = sha3_256(stringified_object).hexdigest()

        return object_id
