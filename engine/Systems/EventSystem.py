from engine.Scenes.Lobby_scene import Lobby
from engine.Scenes.MainMenu_scene import MainMenu
from engine.Systems.Event import Event


class EventSystem():
    def __init__(self, sceneManager, engine):
        self.sceneManager = sceneManager
        self.engine = engine


    def process(self, event):
        #do a command from every event what exist
        if event == Event.LOBBY_MENU:
            self.sceneManager.change_scene(Lobby)
        elif event == Event.MAIN_MENU:
            self.sceneManager.change_scene(MainMenu)
        elif event == Event.QUIT_GAME:
            self.engine.quit()