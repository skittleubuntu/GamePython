from engine.Core.GUISystem.GUIManager import *
from engine.Core.SceneManager import SceneManager
from engine.Scenes.BaseScene import Scene, OverlayScene
from engine.Systems.Event import *



class SettingsScene(Scene):
    def __init__(self, sceneManager):



        # self scene manager for control scenes
        self.sceneManager = sceneManager


        # GUI system and backgrounds
        # ============================================================
        self.gui = GUI(sceneManager)


        self.gui.add_button(Button(text=f"{self.sceneManager.settings.get_key_name("up")}", callback=Event.SET_NEW_BUTTON_UP, x=240, width=50, height=50, y=260))

        self.gui.add_text(Text(x=100, y=200, textSize=30, text="Movement:"))
        self.gui.add_text(Text(x=100, y=260, textSize=50, text="UP:"))
        self.gui.add_text(Text(x=100, y=320, textSize=50, text="DOWN:"))
        self.gui.add_text(Text(x=100, y=380, textSize=50, text="RIGHT:"))
        self.gui.add_text(Text(x=100, y=440, textSize=50, text="LEFT:"))

        self.gui.add_text(Text(x=600, y=100, textSize=70, color=Colors.YELLOW, text="Settings"))


        self.gui.add_button(Button(x=10, y=10, text="<-", callback=Event.MAIN_MENU, width=50, height=50))

        # ============================================================



    def render(self, screen):
        pass

    def update(self):
        pass

    #we dont need buttons on this scene
    def handle_button(self):
        pass


