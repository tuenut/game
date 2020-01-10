import pygame


class Events:
    """
    Класс обработки событий.
    При получении события вызывается нужный коллбэк или дефолтный, который ничего не делает.
    todo хорошо бы, чтобы этот класс мог получать тип события и коллбэк, который на него надо повесить, снаружи
         типа есть метод для подписки коллбеков на события, соответственно, метод отписки.
         хотя это может быть плохой идеей.
         Вопрос нужна ли гибкость настройки ивентов без изменения кода?
         за:     можно использовать конфиг для настройки всех ивентов.
         против: Настройка ивентов захардкожена, исключены ошибки конфигурации.
         ввариант: Можно найти компромис в зависимости от типов ивентов,
                    менять конфиг только из приложения(контролируется валидность),
                    при загрузке конфига проверять валидность.

    """
    KEY_EVENTS_MOVING = (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN,)
    KEY_EVENTS_EXIT = (pygame.K_ESCAPE, pygame.K_q)
    KEY_EVENTS_CREATE_CHARACTER = (pygame.K_c,)

    def __init__(self, *args, **kwargs):
        self.on_exit = kwargs.get('on_exit', self.__default_callback)

    def __default_callback(self, *args, **kwargs):
        pass

    def check(self):
        for event in pygame.event.get():
            self.on_event(event)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.on_exit()

        elif event.type == pygame.KEYDOWN:
            self.on_press_key(event)

    def on_press_key(self, event):
        if event.key in self.KEY_EVENTS_EXIT:
            self.on_exit()

        # elif event.key in self.KEY_EVENTS_CREATE_CHARACTER:
        #     self.on_create_character()