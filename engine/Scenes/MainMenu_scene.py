import pygame

from engine.Entity.Player import Player
from engine.Scenes.BaseScene import Scene

from engine.Settings.settings import Colors
from engine.Systems.Event import Event



class MainMenu(Scene):
    def __init__(self, sceneManager):
        #GUI system and backgrounds
        self.elements = [pygame.Rect((10,10,10,10))]

        #self scene manager for control scenes
        self.sceneManager = sceneManager

        self.player = Player()




    #draw gui and grounds
    def render(self,screen):
        for element in self.elements:
            pygame.draw.rect(screen,Colors.BLUE, element)
        self.player.render(screen)


    #check the pressed button
    def handle_button(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            self.player.y -= 5
        if key[pygame.K_s]:
            self.player.y += 5
        if key[pygame.K_d]:
            self.player.x += 5
        if key[pygame.K_a]:
            self.player.x -= 5

        if key[pygame.K_SPACE]:

            self.sceneManager.add_event(Event.LOBBY_MENU)




