import pygame


class Events:
    def __init__(self, on_exit):
        self.on_exit = on_exit

    def check(self):
        for event in pygame.event.get():
            self.on_event(event)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.on_exit()

        elif event.type == pygame.KEYDOWN:
            self.on_press_key(event)

    def on_press_key(self, event):
        if event.key == pygame.K_ESCAPE:
            self.on_exit()