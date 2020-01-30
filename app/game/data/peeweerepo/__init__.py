import peewee
import json

from hashlib import sha3_256

from app.config import SQLITE_REPO
from app.game.render.config import CELL_SIZE

database = peewee.SqliteDatabase(SQLITE_REPO)

class BaseModel(peewee.Model):
    class Meta:
        database = database


class Location(BaseModel):
    position_x = peewee.IntegerField()
    position_y = peewee.IntegerField()
    object_id = peewee.CharField(max_length=64, default=None, null=True, unique=True)
    object_type = peewee.CharField(max_length=16, default=None, null=True)
    object_name = peewee.CharField(max_length=16, default=None, null=True)
    object_size_x = peewee.IntegerField(default=CELL_SIZE)
    object_size_y = peewee.IntegerField(default=CELL_SIZE)


def generate_object_id(obj: dict):
    serrialized_object = {key: val for key, val in obj.items() if key != 'object_id'}
    stringified_object = json.dumps(serrialized_object).encode()
    object_id = sha3_256(stringified_object).hexdigest()

    return object_id


if __name__ == "__main__":
    database.connect()
    database.drop_tables([Location])
    database.create_tables([Location])

    location_dict = {'position_x': 0, 'position_y': 0, 'object_type': "location"}
    location_dict['object_id'] = generate_object_id(location_dict)

    location = Location(**location_dict)

    location.save()
