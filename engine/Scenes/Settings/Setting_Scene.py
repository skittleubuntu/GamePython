from engine.Core.GUIManager import *
from engine.Core.SceneManager import SceneManager
from engine.Scenes.BaseScene import Scene, OverlayScene
from engine.Systems.Event import *



class SettingsScene(Scene):
    def __init__(self, sceneManager):
        # GUI system and backgrounds
        # ============================================================
        self.gui = GUI(sceneManager)
        self.gui.add_button(Button(text="Overlay scene",width=400, callback=Event.SET_NEW_BUTTON))
        self.gui.add_button(Button(x=10, y=10, text="<-", callback=Event.MAIN_MENU))

        # ============================================================

        # self scene manager for control scenes
        self.sceneManager = sceneManager


    def render(self, screen):
        pass

    def update(self):
        self.gui.update_elements()
        for event in self.gui.events:
            self.sceneManager.add_event(event)
        self.gui.events = []



    #we dont need buttons on this scene
    def handle_button(self):
        pass

class SetNewButtonOverlay(OverlayScene):
    def __init__(self, scene_manager:SceneManager):
        self.scene_manager = scene_manager

    def render(self, screen):
        pass

    def update(self):
        pass

    def handle_button(self):
        if self.scene_manager.inputSystem.is_pressed(pygame.K_ESCAPE):
            self.scene_manager.add_event(Event.OFF_OVERLAY)