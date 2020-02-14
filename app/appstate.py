class AppState:
    """Класс для различных состояний приложения."""

    def __init__(self):
        self.__run = None

    @property
    def runned(self):
        return self.__run

    @property
    def stopped(self):
        return not self.__run

    def run(self):
        self.__run = True

    def stop(self):
        self.__run = False
