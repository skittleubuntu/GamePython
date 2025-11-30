import asyncio
from gui import *
import pygame



class MainMenu:
    def __init__(self, screen, start_callback, settings_callback):
        self.screen = screen
        self.gui = GUI()


        self.gui.add_button(Button(100, 100, text="Start", callback=start_callback))
        self.gui.add_button(Button(100, 200, text="Settings", callback=settings_callback))
        self.gui.add_text(Text(50, 50, "Main Menu"))

    def draw(self):
        self.screen.fill((0,0,0))
        for button in self.gui.buttons:
            button.draw(self.screen)
        for text in self.gui._texts:
            text.draw(self.screen)

    def update(self):
        pass



class SettingsMenu():
    def __init__(self,screen):
        self.screen = screen


    def draw(self):
        pygame.draw.circle(self.screen, (255,255,255), (10,10), 10)



