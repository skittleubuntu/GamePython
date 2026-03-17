import pygame

from engine.Entity.Player import Player
from engine.Scenes.BaseScene import Scene

from engine.Settings.settings import Colors
from engine.Systems.Event import Event
from engine.Core.GUISystem.GUIManager import GUI, Button, Text, Entry



class MainMenuScene(Scene):
    def __init__(self, sceneManager):
        #GUI system and backgrounds
        #============================================================
        self.gui = GUI(sceneManager)
        self.gui.add_button(Button(x=10, y=60, width=100, height=100, callback=Event.LOBBY_MENU, text="Start"))
        self.gui.add_button(Button(x=10, y =170, width=100, height=100, callback=Event.SETTING_MENU, text="Settings"))

        self.gui.add_text(Text(x=500, y=60, text="Pixel", textSize=100, color=Colors.YELLOW))
        self.gui.add_text(Text(x=600, y=180, text="Battle", textSize=100, color=Colors.YELLOW))

        self.gui.add_entry(Entry(x=500, text="write some text", width=1000, color=Colors.GRAY), "first")




        #============================================================


        #self scene manager for control scenes
        self.sceneManager = sceneManager
        self.player = Player()




    #draw grounds
    def render(self,screen):
        self.player.render(screen)


    def update(self):
        self.gui.update_elements()
        for event in self.gui.events:
            self.sceneManager.add_event(event)
        self.gui.events = []


    #check the pressed button
    def handle_button(self):
        inputSystem = self.sceneManager.inputSystem
        controls = self.sceneManager.settings.controls

        if inputSystem.is_held(controls["up"]):
            self.player.y -= 5
        if inputSystem.is_held(controls["down"]):
            self.player.y += 5
        if inputSystem.is_held(controls["right"]):
            self.player.x += 5
        if inputSystem.is_held(controls["left"]):
            self.player.x -= 5

        if inputSystem.is_pressed(pygame.K_SPACE):
            self.sceneManager.add_event(Event.LOBBY_MENU)
            print("Switch to lobby")

