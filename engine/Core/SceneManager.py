
from engine.Scenes import *
import pygame

class SceneManager():
    def __init__(self, screen, clock):
        self.scene = None
        self.screen = screen
        self.clock = clock
        self.event = []
        self.keyboard = pygame.key
        self.mouse = pygame.mouse

    #change the current scene
    def change_scene(self, scene):
        self.scene = scene(self)


    #handle events
    def handle(self,):
        self.scene.handle_button()


    def render_scene(self):
        self.scene.render(self.screen)


    #send event to core (engine)
    def add_event(self, event):
        self.event.append(event)