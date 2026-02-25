import pygame

from engine.Scenes.BaseScene import Scene
from engine.Systems.Event import Event
from engine.Settings.settings import Colors

class Lobby(Scene):
    def __init__(self, sceneManager):
        #GUI system and backgrounds
        self.elements = [pygame.Rect((10,10,10,10))]


        #self scene manager for events
        self.sceneManager = sceneManager

    # check the pressed button
    def handle_button(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.sceneManager.add_event(Event.MAIN_MENU)

        if key[pygame.K_ESCAPE]:
            self.sceneManager.add_event(Event.QUIT_GAME)

    #drawing a gui and grounds
    def render(self, screen):
        for element in self.elements:
            pygame.draw.rect(screen, Colors.RED, element)


