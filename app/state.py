class State:
    """
    Класс для различных состояний. Можно использовать для приложения в целом
    todo в идеале нужен базовый класс состояний, от которого будут наследованы как минимум состояния приложения,
    todo  состояния игры
    """
    def __init__(self, run=False):
        self.run = run

    @property
    def run(self):
        return self.__run

    @run.setter
    def run(self, state):
        if state in (True, False):
            self.__run = state