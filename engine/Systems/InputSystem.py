import pygame


class InputSystem():
    def __init__(self):
        self.previous_keys = None
        self.current_keys = pygame.key.get_pressed()


        #last pressed letter
        self.pressed_letter = None
        self.mouse = pygame.mouse
        self.is_lmb_pressed = False


    #todo mouse clicker

    def update(self):
        #call one time in loop
        self.previous_keys = self.current_keys
        self.current_keys = pygame.key.get_pressed()


    def get_pressed_letter(self):
        if self.pressed_letter:
            letter = self.pressed_letter.unicode
            return letter

    def get_pressed_key(self):
        if self.pressed_letter:
            key = self.pressed_letter.key
            return key


    def get_mouse_pos(self):
        return self.mouse.get_pos()

    #handle pygame event for checking the last pressed letter
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.pressed_letter = event
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.is_lmb_pressed = True

    #clear the buffer of the last pressed button on end of the cycle
    def clear_bufeer(self):
        self.pressed_letter = None
        self.is_lmb_pressed = False



    def is_pressed(self, key: int) -> bool:
       #if prevoius stan is False than this button is clicked first time
        return self.current_keys[key] and not self.previous_keys[key]

    def is_held(self, key: int) -> bool:
        return self.current_keys[key]