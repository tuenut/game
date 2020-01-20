from state import ABCGameState
# from state.universe.locations.locationobject import LocationState


class ExitState(ABCGameState):
    def __init__(self, parent, next_location, access: bool, *args, **kwargs):
        self.parent = parent  # type: LocationState
        self.next_location = next_location  # type: LocationState or None
        self.access = access

    def update(self):
        raise NotImplementedError

    def __repr__(self):
        return "<ExitState from {parent} to {next_location}, accessible is {access} >".format(
            parent=self.parent,
            next_location=self.next_location,
            access=self.access
        )

    __str__ = __repr__