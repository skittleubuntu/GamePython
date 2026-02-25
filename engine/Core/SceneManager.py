
from engine.Scenes import *
import pygame

class SceneManager():
    def __init__(self, screen, clock):
        self.scene = None
        self.screen = screen
        self.clock = clock
        self.event = None

    #change the current scene
    def change_scene(self, scene):
        self.scene = scene(self)

    #full update of scene and render
    def handle(self,event):
        self.scene.handle_event(event)
        self.scene.update()
        print("SceneRender")
        self.scene.render(self.screen)


    #send event to core (engine)
    def add_event(self, event):
        self.event = event