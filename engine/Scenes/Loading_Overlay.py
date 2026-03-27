from engine.Core.GUISystem.GUIManager import *
from engine.Core.SceneManager import SceneManager
from engine.Scenes.BaseScene import Scene, OverlayScene
from engine.Systems.Event import *
from engine.Core.GUISystem.Text import Text



class LoadingScene(OverlayScene):
    def __init__(self, scene_manager:SceneManager):
        self.scene_manager = scene_manager

        #=========
        self.gui = GUI(scene_manager)
        self.gui.add_text(Text(text=f"Loading...", textSize=20))

        #======


    def render(self, screen):
        pass

    def update(self):
        pass


    def handle_button(self):
        pass