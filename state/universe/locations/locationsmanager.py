import logging

from app.mainfunctions.logger import pp

from abstractions.gamestate import ABCGameStateObject, ABCGameStateLocationsManager, ABCGameStateCharacter
from .locationobject import LocationState

logger = logging.getLogger(__name__)


class LocationsManager(ABCGameStateLocationsManager):
    def __init__(self, locations_data):
        self.__locations_data = locations_data
        self.__locations = {}  # type: {str: LocationState}

        if locations_data is not None:
            self.__init_location_objects()

    def __iter__(self):
        for location in self.__locations.values():
            yield location

    def __init_location_objects(self):
        # init locations
        for location_dumped_data in self.__locations_data:
            self.create_location(location_dumped_data)

        # init locations exits
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

    def add_object_on_location(self, obj, location):
        logger.debug("Request to add object <%s> on location <%s>.", obj, location)
        if not isinstance(location, LocationState):
            logger.debug("Wrong location object <%s>", location)
            return

        if location not in self:
            logger.debug("Unknown %s, not in managed locations.", location)
            return

        if issubclass(obj.__class__, ABCGameStateObject):
            result = location.add_object(obj)

            logger.debug("Request complete.")

            return result

    def remove_object_from_location(self, obj):
        logger.debug("Request to remove object <%s> from its location.", obj)

        if issubclass(obj.__class__, ABCGameStateCharacter) and obj.location in self:
            location = obj.location
            result = location.remove_object(obj)

            if result:
                obj.location = None

            logger.debug("Request complete.")

            return result
        else:
            logger.debug("Wrong game object <%s>", obj)

    def update(self):
        raise NotImplementedError
