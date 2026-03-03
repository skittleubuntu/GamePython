import pygame


class InputSystem():
    def __init__(self):
        self.previous_keys = None
        self.current_keys = pygame.key.get_pressed()



    #todo mouse clicker

    def update(self):
        #call one time in loop
        self.previous_keys = self.current_keys
        self.current_keys = pygame.key.get_pressed()

    def is_pressed(self, key: int) -> bool:
       #if prevoius stan is False than this button is clicked first time
        return self.current_keys[key] and not self.previous_keys[key]

    def is_held(self, key: int) -> bool:
        return self.current_keys[key]