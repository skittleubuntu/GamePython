import pygame


class Battle():
    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, (255, 0, 255), (10, 10), 10)