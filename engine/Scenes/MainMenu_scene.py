import pygame


from engine.Scenes.BaseScene import Scene
from engine.Scenes.Lobby_scene import Lobby
from engine.Settings.settings import Colors
from engine.Systems.EventSystem import Event


class MainMenu(Scene):
    def __init__(self, sceneManager):
        #GUI system and backgrounds
        self.elements = [pygame.Rect((10,10,10,10))]

        #self scene manager for control scenes
        self.sceneManager = sceneManager

        #events for update
        self.events = []




    def render(self,screen):
        for element in self.elements:
            pygame.draw.rect(screen,Colors.BLUE, element)




    def handle_event(self,event):
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_SPACE:
               self.sceneManager.add_event(Event.LOBBY_MENU)
