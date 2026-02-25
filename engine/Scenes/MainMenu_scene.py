import pygame


from engine.Scenes.BaseScene import Scene
from engine.Scenes.Lobby_scene import Lobby
from engine.Settings.settings import Colors





class MainMenu(Scene):
    def __init__(self, sceneManager):
        #GUI system and backgrounds
        self.elements = [pygame.Rect((10,10,10,10))]


        #self scene manager for events
        self.sceneManager = sceneManager


    def render(self,screen):
        for element in self.elements:
            pygame.draw.rect(screen,Colors.BLUE, element)

    def handle_event(self, keyboard, mouse):
        if keyboard[pygame.K_SPACE]:
            self.sceneManager.change_scene(Lobby)
