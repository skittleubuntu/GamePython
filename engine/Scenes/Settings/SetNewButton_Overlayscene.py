from engine.Core.GUISystem.GUIManager import *
from engine.Core.SceneManager import SceneManager
from engine.Scenes.BaseScene import Scene, OverlayScene
from engine.Systems.Event import *
from engine.Core.GUISystem.Text import Text



class SetNewButton(OverlayScene):
    def __init__(self, scene_manager:SceneManager):
        self.scene_manager = scene_manager

        #=========
        self.gui = GUI(scene_manager)
        self.gui.add_text(Text(text=f"Press button for changing control {None}", textSize=20), id="main_text")

        #======

        self.flag_button = None

    def render(self, screen):
        pass

    def update(self):
        pass


    def handle_button(self):

        #left from overlay scene
        if self.scene_manager.inputSystem.is_pressed(pygame.K_ESCAPE):
            self.scene_manager.add_event(Event.OFF_OVERLAY)


    #checking what buuton we need to change
    def set_kwargs(self, **kwargs):
        main_text = self.gui.get_text_by_id("main_text")
        main_text.edit_text(f"Press button for changing control {kwargs["flag"]}")
        self.flag_button = kwargs["flag"]
