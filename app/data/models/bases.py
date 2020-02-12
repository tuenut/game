import copy
import json
import logging
import peewee

from datetime import datetime as dt
from hashlib import sha3_256

from config import SQLITE_REPO

database = peewee.SqliteDatabase(SQLITE_REPO)


class BaseModel(peewee.Model):
    logger = logging.getLogger(__name__)

    class Meta:
        database = database


class GameEntity(BaseModel):
    ingame_id = peewee.CharField(max_length=64, default=None, null=True, unique=True)
    ingame_type = peewee.CharField(max_length=16)
    ingame_name = peewee.CharField(max_length=16, default=None, null=True, )

    def load(self, data: dict):
        raise NotImplementedError

    def dump(self) -> dict:
        raise NotImplementedError


class EntityBinding(BaseModel):
    entity = peewee.ForeignKeyField(GameEntity, default=None, null=True, unique=True)
    created = peewee.DateTimeField(default=dt.now)

    @property
    def ingame_id(self):
        return self.entity.ingame_id

    @property
    def ingame_type(self):
        return self.entity.ingame_type

    @property
    def ingame_name(self):
        return self.entity.ingame_name

    @classmethod
    def create(cls, **query):
        if query.get('ingame_id'):
            raise Exception("Field <ingame_id> can not provide directly, only by automatic calculate.")

        self_class_kwargs = {key: val for key, val in query.items() if key in cls._meta.fields.keys()}
        instance = super().create(**self_class_kwargs)

        instance.entity = cls._create_entity_binding(instance, **query)

        return instance

    @classmethod
    def _create_entity_binding(cls, instance, **query):
        ingame_type = query.get('ingame_type')
        ingame_name = query.get('ingame_name')

        serrialized_data = {
            field_name: getattr(instance, field_name)
            for field_name, field_type in cls._meta.fields.items()
            if not isinstance(field_type, peewee.ForeignKeyField)
        }
        serrialized_data.update(
            {
                'ingame_type': ingame_type,
                'ingame_name': ingame_name,
                'created': serrialized_data['created'].timestamp()
            }
        )

        ingame_id = cls.generate_object_id(**serrialized_data)

        try:
            entity = GameEntity.create(ingame_id=ingame_id, ingame_type=ingame_type, ingame_name=ingame_name)
        except Exception as e:
            cls.logger.exception("Some Exception while use overrided creation method.")
            raise e

        return entity

    @staticmethod
    def generate_object_id(**kwargs):
        serrialized_data = copy.deepcopy(kwargs)

        try:
            serrialized_data.pop('ingame_id')
        except KeyError:
            pass

        stringified_object = json.dumps(serrialized_data).encode()
        object_id = sha3_256(stringified_object).hexdigest()

        return object_id
