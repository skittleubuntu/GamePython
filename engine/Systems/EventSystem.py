from engine.Scenes.Lobby_scene import Lobby


class Event():
    LOBBY_MENU = 1
    MAIN_MENU = 2


class EventSystem():
    def __init__(self, sceneManager):
        self.sceneManager = sceneManager


    def procces(self, event):
        if event == Event.LOBBY_MENU:
            self.sceneManager.change_scene(Lobby)
            self.sceneManager.event = None