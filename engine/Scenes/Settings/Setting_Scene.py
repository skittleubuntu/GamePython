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


        self.gui.add_button(Button(text=f"{self.sceneManager.settings.get_key_name("up")}", callback=Event.SET_NEW_BUTTON_UP, x=240, width=50, height=50, y=260), id="up_button")
        self.gui.add_button(Button(text=f"{self.sceneManager.settings.get_key_name("down")}", callback=Event.SET_NEW_BUTTON_DOWN, x=340,width=50, height=50, y=320), id="down_button")
        self.gui.add_button(Button(text=f"{self.sceneManager.settings.get_key_name("right")}", callback=Event.SET_NEW_BUTTON_RIGHT, x=390,width=50, height=50, y=380), id="right_button")
        self.gui.add_button(Button(text=f"{self.sceneManager.settings.get_key_name("left")}", callback=Event.SET_NEW_BUTTON_LEFT, x=340,width=50, height=50, y=440), id="left_button")

        self.gui.add_text(Text(x=100, y=200, textSize=30, text="Movement:"))
        self.gui.add_text(Text(x=100, y=260, textSize=50, text="UP:"))
        self.gui.add_text(Text(x=100, y=320, textSize=50, text="DOWN:"))
        self.gui.add_text(Text(x=100, y=380, textSize=50, text="RIGHT:"))
        self.gui.add_text(Text(x=100, y=440, textSize=50, text="LEFT:"))

        self.gui.add_text(Text(x=600, y=100, textSize=70, color=Colors.YELLOW, text="Settings"))


        self.gui.add_button(Button(x=10, y=10, text="<-", callback=Event.MAIN_MENU, width=50, height=50))

        # ============================================================


        #flags for updating
        self.buttons_updated = False


    def render(self, screen):
        pass

    def update(self):
        if self.sceneManager.settings.is_setting_updated and self.buttons_updated == False:
            print("Updating buttons...")
            up_button = self.gui.get_button_by_id("up_button")
            down_button = self.gui.get_button_by_id("down_button")
            left_button = self.gui.get_button_by_id("left_button")
            right_button = self.gui.get_button_by_id("right_button")

            up_button.change_text(f"{self.sceneManager.settings.get_key_name("up")}")
            down_button.change_text(f"{self.sceneManager.settings.get_key_name("down")}")
            left_button.change_text(f"{self.sceneManager.settings.get_key_name("left")}")
            right_button.change_text(f"{self.sceneManager.settings.get_key_name("right")}")

            #set flag for only one update
            self.buttons_updated = True








    #we dont need buttons on this scene
    def handle_button(self):
        pass


