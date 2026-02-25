import pygame
from engine.Settings.settings import Colors

class Player():
    def __init__(self):
        self.x = 100
        self.y = 100


    def render(self,screen):
        pygame.draw.circle(screen,Colors.BLUE, (self.x, self.y) ,10)