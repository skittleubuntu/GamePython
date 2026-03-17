import pygame

from engine.Scenes.BaseScene import Scene
from engine.Systems.Event import Event
from engine.Settings.settings import Colors
from engine.Core.GUISystem.GUIManager import GUI

class LobbyScene(Scene):
    def __init__(self, sceneManager):
        #GUI system and backgrounds
        self.gui = GUI(sceneManager)

        #self scene manager for events
        self.sceneManager = sceneManager

    # check the pressed button
    def handle_button(self):
        key = pygame.key.get_pressed()

        inputSystem = self.sceneManager.inputSystem

        if key[pygame.K_SPACE] and inputSystem.is_pressed(pygame.K_SPACE):
            self.sceneManager.add_event(Event.MAIN_MENU)
            print("Switch to main menu")


        if key[pygame.K_ESCAPE]:
            self.sceneManager.add_event(Event.QUIT_GAME)

    #drawing a gui and grounds
    def render(self, screen):
        for element in self.elements:
            pygame.draw.rect(screen, Colors.RED, element)


    def update(self):
        pass