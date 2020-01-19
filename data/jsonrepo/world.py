from data import ABCWorldMapData
from data.jsonrepo.locations import LocationData


class WorldMapData(ABCWorldMapData):
    """Класс для хранения данных о состояния мира."""

    def dump(self):
        pass

    # todo все передаваемые наружу данные должны быть серриализованы. Не передавать объекты!

    def __init__(self, ):
        raise NotImplementedError

    def get_location(self, location_id):
        return self.__world.get(location_id)

    def get_next_location(self, location, direction):
        """

        :param location:
        :param direction:
        :return:
            location : вернет ту же самую локацию, если соседняя не существует.
        """
        x, y = location.location_id[0], location.location_id[1]
        pos = (x, y)

        if direction == "down":
            pos = (x, y + 1)
        elif direction == "left":
            pos = (x - 1, y)
        elif direction == "right":
            pos = (x + 1, y)
        elif direction == "up":
            pos = (x, y - 1)

        return self.get_location(pos)

    @property
    def locations(self):
        return list(self.__world.values())

    @property
    def locations_ids(self):
        return list(self.__world.keys())