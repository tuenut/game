import logging

from app.mainfunctions.logger import pp

from state.abstractions import ABCGameStateObject
from state.characters.base import Character
from .locationobject import LocationState

logger = logging.getLogger(__name__)


class LocationsManager:
    def __init__(self, locations_data):
        self.__locations_data = locations_data
        self.__locations = {}  # type: {str: LocationState}

        if locations_data is not None:
            self.__init_location_objects()

    def __iter__(self):
        for location in self.__locations.values():
            yield location

    def __init_location_objects(self):
        for location_dumped_data in self.__locations_data:
            self.create_location(location_dumped_data)

        for location in self:
            location_exits = location.data.get('exits')

            for location_exit in location_exits:
                next_location = self.get_location(location_exits[location_exit]['location_id'])
                location_exits[location_exit]['next_location'] = next_location

            location.init_exits(location_exits)

    def create_location(self, location_dumped_data: dict):
        location = LocationState(location_dumped_data)
        self.__locations.update({location.id: location})

    def get_location(self, location):
        """Location getter.

        Returns
        -------
            location : LocationState or None
        """
        logger.debug("Request location <%s>", location)

        result = None

        if self.__is_valid_location_state_object(location):
            result = location
        elif isinstance(location, str):
            result = self.__locations.get(location)
        else:
            logger.debug("Can't get location <%s>", location)
            return result

        logger.debug("Find location <%s>", result)

        return result

    def __is_valid_location_state_object(self, location):
        logger.debug("Check is %s a valid location", location)

        is_location = False
        in_locations = False

        try:
            is_location = issubclass(location.__class__, LocationState)
            in_locations = location in self
        except Exception as e:
            result = False
        else:
            result = is_location and in_locations

        logger.debug(
            "Is LocationState object: <%s>. Is in locations: <%s>. Result: <%s>.",
            is_location, in_locations, result
        )

        return result

    def add_object_on_location(self, obj: ABCGameStateObject, location: LocationState):
        logger.debug("Request to add object <%s> on location <%s>.", obj, location)

        if issubclass(obj.__class__, Character) and location in self:
            result = location.add_character(obj)
            if result:
                obj.location = location

            logger.debug("Request complete.")

            return result
        else:
            logger.debug("Wrong location object <%s>", location)

    def remove_object_from_location(self, obj: ABCGameStateObject):
        logger.debug("Request to remove object <%s> from its location.", obj)

        if issubclass(obj.__class__, Character) and obj.location in self:
            location = obj.location
            result = location.remove_character(obj)

            if result:
                obj.location = None

            logger.debug("Request complete.")

            return result
        else:
            logger.debug("Wrong game object <%s>", obj)
