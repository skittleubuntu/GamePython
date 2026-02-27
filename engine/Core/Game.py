import sys

import pygame

from engine.Core.SceneManager import SceneManager
from engine.Scenes.MainMenu_scene import MainMenu

from engine.Settings.settings import Colors, Settings
from engine.Systems.EventSystem import EventSystem
from engine.Systems.InputSystem import InputSystem


class Game:
    def __init__(self):

        #core initialization (pygame)
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.WIDTH, self.settings.HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        #engine systems
        self.inputSystem = InputSystem()
        self.sceneManager = SceneManager(self.screen, self.clock, self.inputSystem)
        self.sceneManager.change_scene(MainMenu)
        self.eventSystem = EventSystem(self.sceneManager, self)


    def run(self):
        while self.running:
            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()



            #game loop
            self.screen.fill(Colors.BLACK)


            #systems handles
            self.sceneManager.handle()
            self.inputSystem.handle()


            #============================================================
            # check every event from sceneManager
            if self.sceneManager.event:
                for event in self.sceneManager.event:
                    self.eventSystem.procces(event)
                # after processing all events clear the event list
                self.sceneManager.event = []
            # ============================================================


            self.sceneManager.render_scene()

            pygame.display.flip()
            self.clock.tick(self.settings.FPS)

    #shutdown a game and server
    def quit(self):
        self.running = False
        sys.exit()