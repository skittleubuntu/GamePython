import pygame

from engine.Core.SceneManager import SceneManager
from engine.Scenes.MainMenu_scene import MainMenu

from engine.Settings.settings import Colors, Settings
from engine.Systems.EventSystem import Event, EventSystem


class Game:
    def __init__(self):

        #core initialization (pygame)
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.WIDTH, self.settings.HEIGHT))
        self.clock = pygame.time.Clock()

        #engine systems

        self.sceneManager = SceneManager(self.screen, self.clock)
        self.sceneManager.change_scene(MainMenu)
        self.eventSystem = EventSystem(self.sceneManager)







    def run(self):
        running = True
        while running:
            #event loop
            for event in pygame.event.get():

                # handle events
                self.sceneManager.handle(event)
                if event.type == pygame.QUIT:
                    running = False



            #game loop
            self.screen.fill(Colors.BLACK)

            if self.sceneManager.event:
                print(self.sceneManager.event)
                self.eventSystem.procces(self.sceneManager.event)


            pygame.display.flip()
            self.clock.tick(self.settings.FPS)


