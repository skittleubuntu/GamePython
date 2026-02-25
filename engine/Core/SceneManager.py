
from engine.Scenes import *
import pygame

class SceneManager():
    def __init__(self, screen, clock):
        self.scene = None
        self.screen = screen
        self.clock = clock

    #change the current scene
    def change_scene(self, scene):
        self.scene = scene(self)


    def handle(self, keyboard, mouse):
        self.scene.handle_event(keyboard, mouse)
        self.scene.update()
        self.scene.render(self.screen)