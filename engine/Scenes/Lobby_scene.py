import pygame

from engine.Scenes.BaseScene import Scene
from engine.Scenes.MainMenu_scene import MainMenu
from engine.Settings.settings import Colors

class Lobby(Scene):
    def __init__(self, sceneManager):
        #GUI system and backgrounds
        self.elements = [pygame.Rect((10,10,10,10))]


        #self scene manager for events
        self.sceneManager = sceneManager


    def render(self,screen):
        for element in self.elements:
            pygame.draw.rect(screen,Colors.RED, element)




    def handle_event(self, keyboard, mouse):
        if keyboard[pygame.K_SPACE]:
            self.sceneManager.change_scene(MainMenu)
