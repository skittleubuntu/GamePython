import pygame

from engine.Entity.Player import Player
from engine.Scenes.BaseScene import Scene

from engine.Settings.settings import Colors
from engine.Systems.Event import Event
from engine.Scenes.GUIManager import GUI, Button



class MainMenu(Scene):
    def __init__(self, sceneManager):
        #GUI system and backgrounds

        self.gui = GUI()
        self.gui.add_button(Button(x=10, y=60, width=500, height=100, callback=Event.LOBBY_MENU))

        self.elements = [pygame.Rect((10,10,10,10))]


        #self scene manager for control scenes
        self.sceneManager = sceneManager
        self.player = Player()




    #draw grounds
    def render(self,screen):
        for element in self.elements:
            pygame.draw.rect(screen,Colors.BLUE, element)
        self.player.render(screen)


    def update(self):
        self.gui.update_elements()
        for event in self.gui.events:
            self.sceneManager.add_event(event)


    #check the pressed button
    def handle_button(self):

        inputSystem = self.sceneManager.inputSystem

        if inputSystem.is_held(pygame.K_w):
            self.player.y -= 5
        if inputSystem.is_held(pygame.K_s):
            self.player.y += 5
        if inputSystem.is_held(pygame.K_d):
            self.player.x += 5
        if inputSystem.is_held(pygame.K_a):
            self.player.x -= 5

        if inputSystem.is_pressed(pygame.K_SPACE):
            self.sceneManager.add_event(Event.LOBBY_MENU)
            print("Switch to lobby")

