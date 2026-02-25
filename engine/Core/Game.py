import pygame

from engine.Core.SceneManager import SceneManager
from engine.Scenes.MainMenu_scene import MainMenu
from engine.Systems.InputSystems import InputSystems
from engine.Settings.settings import Colors, Settings

class Game:
    def __init__(self):

        #core initialization (pygame)
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.WIDTH, self.settings.HEIGHT))
        self.clock = pygame.time.Clock()

        #engine systems
        self.inputSystem = InputSystems()
        self.sceneManager = SceneManager(self.screen)
        self.sceneManager.change_scene(MainMenu)







    def run(self):
        running = True
        while running:
            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False



            #game loop
            self.screen.fill(Colors.BLACK)


            #get input data
            keyboard = self.inputSystem.get_keyboard()
            mouse = self.inputSystem.get_mouse()


            #handle events
            self.sceneManager.handle(keyboard, mouse)


            pygame.display.flip()
            self.clock.tick(self.settings.FPS)


