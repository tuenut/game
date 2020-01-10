class World:
    """Класс для описания состояния игрового мира.
    Содержит информацию об игровом поле, локациях.
    """

    __locations_list = None

    def __init__(self, world_repository):
        self.__map = world_repository

    @property
    def locations_list(self):
        """
        Нужно для сообщения информации обо всех локациях в мире наружу.
        todo Скорее всего, метод должен сообщать метаинформацию, а не список объектов.
        :return:
        """
        if self.__locations_list is None:
            self.__locations_list = [location for x_row in self.__map.grid for location in x_row]

        return self.__locations_list

    @property
    def grid(self):
        return self.__map.grid

    def move(self, direction):
        raise NotImplementedError

    def get_location(self):
        raise NotImplementedError

    def add_object_on_location(self, obj, location):
        """
        По идее, об объектах локации никто, кроме мира знать не должен. Мир наружу сообщает только информацию о локациях.
        Тогда КтоТо снаружи обращается к Миру с запросом разместить Объект на локации (например) с координатами X,Y.
         Мир находит у себя эту локацию и вызывает ее метод.
        :param obj:
        :param location:
        :return:
        """
        if location in self.locations_list:
            location.add_object(obj) # todo чот это не правильно по идее
            # todo если кто-то обращается к Миру, чтобы добавить объект на локацию, передает и объект и локацию, а
            # todo метод добавления есть у локации, то какой сымсл передавать это миру, если можно просто вызвать
            # todo метод у локации?