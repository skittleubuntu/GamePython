
from engine.Scenes import *
import pygame

class SceneManager():
    def __init__(self, screen, clock, inputSystem):
        self.scene = None
        self.screen = screen
        self.clock = clock
        self.event = []
        self.keyboard = pygame.key
        self.mouse = pygame.mouse
        self.inputSystem = inputSystem

    #change the current scene
    def change_scene(self, scene):
        self.scene = scene(self)


    #handle scene, updates and buttons
    def handle(self,):
        self.scene.handle_button()
        self.scene.update()


    def render_scene(self):
        self.scene.render(self.screen)
        self.scene.gui.draw_elements(self.screen)


    #send event to core (engine)
    def add_event(self, event):
        self.event.append(event)