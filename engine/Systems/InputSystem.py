import pygame


class InputSystem():
    def __init__(self):
        self.key = pygame.key
        self.mouse = pygame.mouse
        self.previous = None
        self.actual = None
    #check is the key held
    #check the previous stan of key and present

    def is_held(self, key) -> bool:
        self.handle()
        return self.previous[key] and self.actual[key]


    def handle(self):
        self.previous = self.actual
        self.actual = self.key.get_pressed()
