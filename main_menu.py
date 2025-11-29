import asyncio

import pygame




class MainMenu():
    def __init__(self,screen):
        self.screen = screen



    def draw(self):
        pygame.draw.circle(self.screen, (255,255,255), (10,10), 10)




class SettingsMenu():
    def __init__(self,screen):
        self.screen = screen


    def draw(self):
        pygame.draw.circle(self.screen, (255,255,255), (10,10), 10)



