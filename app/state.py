class State:
    def __init__(self, run):
        self.run = run

    @property
    def run(self):
        return self.__run

    @run.setter
    def run(self, state):
        if state in (True, False):
            self.__run = state