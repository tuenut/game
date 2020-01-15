class LocationPropertiesMixin:
    @property
    def coordinates(self):
        return self._coordinates

    @property
    def down(self):
        return self._down

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def up(self):
        return self._up

    @property
    def exits(self):
        return self.down, self.left, self.right, self.up

    @property
    def objects(self):
        return self._objects_on_location

    @property
    def characters(self):
        return self._characters_on_location

    @property
    def data(self):
        return {
            "exits": self.exits,
            "objects": self.objects,
            "characters": self.characters,
            "coordinates": self.coordinates
        }