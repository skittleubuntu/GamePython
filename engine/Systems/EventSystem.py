from engine.Scenes.Lobby.Lobby_scene import LobbyScene
from engine.Scenes.MainMenu.MainMenu_scene import MainMenuScene
from engine.Scenes.Settings.Setting_Scene import SettingsScene
from engine.Scenes.Settings.SetNewButton_Overlayscene import *

from engine.Systems.Event import Event
import time

class EventSystem():
    def __init__(self, sceneManager, engine):
        self.sceneManager = sceneManager
        self.engine = engine

    def process(self, event):
        if event == Event.LOBBY_MENU:
            self.sceneManager.change_scene(LobbyScene)

        elif event == Event.MAIN_MENU:
            self.sceneManager.change_scene(MainMenuScene)

        elif event == Event.QUIT_GAME:
            self.engine.quit()

        elif event == Event.SETTING_MENU:
            self.sceneManager.change_scene(SettingsScene)


        elif event == Event.SET_NEW_BUTTON_UP:
            self.sceneManager.set_overlay_scene(SetNewButton, flag="UP")

        elif event == Event.OFF_OVERLAY:
            self.sceneManager.remove_overlay_scene()