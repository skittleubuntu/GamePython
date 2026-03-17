import sys

import pygame,os
import time
from engine.Core.SceneManager import SceneManager
from engine.Scenes.Lobby.Lobby_scene import LobbyScene
from engine.Scenes.MainMenu.MainMenu_scene import MainMenuScene
from engine.Scenes.Settings.Setting_Scene import SettingsScene, SetNewButtonOverlay

from engine.Settings.settings import Colors, Settings
from engine.Systems.EventSystem import EventSystem
from engine.Systems.InputSystem import InputSystem


class Game:
    def __init__(self):

        #core initialization (pygame)
        pygame.init()
        self.settings = Settings()
        self.settings.load_from_json("engine/Data/controls.json")
        self.screen = pygame.display.set_mode((self.settings.WIDTH, self.settings.HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        os.system(
            '''osascript -e 'tell application "System Events" to set frontmost of the first process whose unix id is {} to true' '''.format(
                os.getpid()))

        #engine systems
        self.inputSystem = InputSystem()
        self.sceneManager = SceneManager(self.screen, self.inputSystem, self.settings)
        self.eventSystem = EventSystem(self.sceneManager, self)

        # initialization engine systems
        scenes = [MainMenuScene, SettingsScene, LobbyScene, ]
        overlay_scenes = [SetNewButtonOverlay]
        self.sceneManager.initialization(scenes, overlay_scenes)
        self.sceneManager.change_scene(MainMenuScene)


        #checking the powerfull of engine (fps, time beetwen cycles)
        #todo


    def run(self):
        while self.running:

            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

                self.inputSystem.handle_event(event)


            #game loop
            self.screen.fill(Colors.BLACK)
            #systems handles
            self.sceneManager.handle()
            self.inputSystem.update()


            #============================================================
            # check every event from sceneManager
            if self.sceneManager.event:
                for event in self.sceneManager.event:
                    print(f"Events: {event}")
                    self.eventSystem.process(event)
                # after processing all events clear the event list
                self.sceneManager.event = []
            # ============================================================


            self.sceneManager.render_scene()
            #update the DT time (delta time)
            pygame.display.flip()
            self.settings.DT = self.clock.tick(self.settings.FPS) / 1000
            self.inputSystem.clear_bufeer()



    #shutdown a game and server
    def quit(self):
        self.running = False
        sys.exit()