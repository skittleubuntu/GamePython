import pygame

class InputSystems():
    def __init__(self):
        self.keyboard = pygame.key
        self.mouse = pygame.mouse

    #return pressed keys
    def get_keyboard(self):
        return self.keyboard.get_pressed()

    def get_mouse(self):
        return self.mouse