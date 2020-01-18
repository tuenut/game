class State:
    """
    Класс для различных состояний. Можно использовать для приложения в целом
    todo в идеале нужен базовый класс состояний, от которого будут наследованы как минимум состояния приложения,
    todo  состояния игры
    """

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
