import pygame
from gui import *
from player import *

class Battle():
    def __init__(self, screen, exit_from_battle):
        self.screen = screen
        self.gui = GUI()
        self.players = [Player(100, 100)]
        self.exit_window = ExitWindow(self.screen, exit_from_battle, self.close_exit_window)
        self.exit_window_opened = False

    def draw(self):

        pygame.draw.circle(self.screen, (255, 0, 255), (10, 10), 10)
        if self.exit_window_opened:
            self.exit_window.draw()
            self.exit_window.gui.check_buttons()

    def update(self):
        for player in self.players:
            asyncio.create_task(player.handle_input())
            player.draw(self.screen)
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            print("Presed")
            self.exit_window_opened = True

    def close_exit_window(self):
        self.exit_window_opened = False





class ExitWindow():
    def __init__(self, screen, exit_from_battle, close_exit_window):
        self.screen = screen
        self.gui = GUI()
        self.gui.add_button(Button(100,200, callback=exit_from_battle, text="Yes"))
        self.gui.add_button(Button(400, 500, callback=close_exit_window, text="No"))

    def draw(self):
        for button in self.gui.buttons:
            button.draw(self.screen)

