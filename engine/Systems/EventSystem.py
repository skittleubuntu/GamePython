from engine.Scenes.Lobby.Lobby_scene import LobbyScene
from engine.Scenes.MainMenu.MainMenu_scene import MainMenuScene
from engine.Scenes.Settings.Setting_Scene import SettingsScene, SetNewButtonOverlay
from engine.Systems.Event import Event
import time

class EventSystem():
    def __init__(self, sceneManager, engine):
        self.sceneManager = sceneManager
        self.engine = engine

        self.handlers = {
            Event.LOBBY_MENU: lambda: self.sceneManager.change_scene(LobbyScene),
            Event.MAIN_MENU: lambda: self.sceneManager.change_scene(MainMenuScene),
            Event.QUIT_GAME: self.engine.quit,
            Event.SETTING_MENU: lambda: self.sceneManager.change_scene(SettingsScene),
            Event.SET_NEW_BUTTON: lambda: self.sceneManager.set_overlay_scene(SetNewButtonOverlay),
            Event.OFF_OVERLAY: self.sceneManager.remove_overlay_scene
        }

    def process(self, event):
        if event in self.handlers:
            self.handlers[event]()