import pygame

from engine.Entity.Player import Player
from engine.Scenes.BaseScene import Scene

from engine.Settings.settings import Colors
from engine.Systems.Event import Event
from engine.Core.GUISystem.Text import Text
from engine.Core.GUISystem.Entry import Entry
from engine.Core.GUISystem.Button import Button
from engine.Core.GUISystem.GUIManager import GUI



class MainMenuScene(Scene):
    def __init__(self, sceneManager):
        #GUI system and backgrounds
        #============================================================
        self.gui = GUI(sceneManager)
        self.gui.add_button(Button(x=10, y=60, width=100, height=100, callback=Event.LOBBY_MENU, text="Start"))
        self.gui.add_button(Button(x=10, y =170, width=100, height=100, callback=Event.SETTING_MENU, text="Settings"))

        self.gui.add_text(Text(x=500, y=60, text="Pixel", textSize=100, color=Colors.YELLOW))
        self.gui.add_text(Text(x=600, y=180, text="Battle", textSize=100, color=Colors.YELLOW))

        self.gui.add_entry(Entry(x=500, text="write some text", width=1000, color=Colors.DARK_GRAY), "first")


        self.gui.add_text(Text(x=1000, y=10, textSize=70, color=Colors.ORANGE, text=None), id="FPS")

        #============================================================


        #self scene manager for control scenes
        self.sceneManager = sceneManager
        self.input_system = self.sceneManager.inputSystem
        self.player = Player()




    #draw grounds
    def render(self,screen):
        self.player.render(screen)


    def update(self):
        fps_text = self.gui.get_text_by_id("FPS")
        fps_text.edit_text(f"{self.sceneManager.settings.actual_fps}")


    #check the pressed button
    def handle_button(self):

        controls = self.sceneManager.settings.controls

        if self.input_system.is_held(controls["up"]):
            self.player.y -= 100 * self.sceneManager.settings.DT
        if self.input_system.is_held(controls["down"]):
            self.player.y += 100 * self.sceneManager.settings.DT
        if self.input_system.is_held(controls["right"]):
            self.player.x += 100 * self.sceneManager.settings.DT
        if self.input_system.is_held(controls["left"]):
            self.player.x -= 100 * self.sceneManager.settings.DT

        if self.input_system.is_pressed(pygame.K_SPACE):
            self.sceneManager.add_event(Event.LOBBY_MENU)
            print("Switch to lobby")

