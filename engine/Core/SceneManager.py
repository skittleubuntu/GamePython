
from engine.Scenes import *
from engine.Scenes.BaseScene import *
from engine.Settings.settings import Colors
import pygame, time

class SceneManager():
    def __init__(self, screen:pygame.display, inputSystem, settings):
        #scenes for rendering and updates
        self.scene = None
        self.overlay_scene = None
        self.darkness_overlay = None
        self.screen = screen


        #events for eventsystem
        self.event = []

        #-----
        self.scenes = {}
        self.overlay_scenes = {}
        #-------


        #pygame events
        self.pygame_event = None

        self.inputSystem = inputSystem
        self.settings = settings

        # once update variable created for updating scene when we create a overlay scene
        # for making all button un-hovered
        self.once_update = False




    #change the current scene
    def change_scene(self, scene:Scene, **kwargs):
        self.scene = self.scenes[scene]
        if kwargs:
            self.scene.set_kwargs(**kwargs)


    def set_overlay_scene(self, overlay_scene:OverlayScene, **kwargs):
        self.overlay_scene = self.overlay_scenes[overlay_scene]
        if kwargs:
            self.overlay_scene.set_kwargs(**kwargs)
        print("seted a new overlay Scene")

    def remove_overlay_scene(self):
        self.overlay_scene = None
        print("Overlay scene is off")


    #handle scene, updates and buttons
    def handle(self,):
        #updatating main scene or overlay scene
        if self.overlay_scene is None:
            self.scene.handle_button()
            self.scene.update()
            self.scene.update_gui()
            self.once_update = False
        else:
            if not self.once_update:
                self.scene.update()
                self.scene.update_gui()
                self.once_update = True
            self.overlay_scene.handle_button()
            self.overlay_scene.update()
            self.overlay_scene.update_gui()

    def render_scene(self):
        self.scene.render(self.screen)
        self.scene.gui.draw_elements(self.screen)
        if self.overlay_scene is not None:
            if self.darkness_overlay is None:
                self.darkness_overlay = pygame.Surface(
                    (self.settings.WIDTH, self.settings.HEIGHT)
                )
                self.darkness_overlay.set_alpha(122)
                self.darkness_overlay.fill(Colors.BLACK)

            self.screen.blit(self.darkness_overlay, (0, 0))
            self.overlay_scene.gui.draw_elements(self.screen)



    #send event to core (engine)
    def add_event(self, event):
        self.event.append(event)


    #prepearing scenes for render
    def initialization(self,scenes, overlay_scenes):
        # loading in percentes
        loading = 0
        #how many percent are plused when one scene is prepared
        percent = 100 / (len(scenes) + len(overlay_scenes))
        for scene in scenes:
            self.scenes[scene] = scene(self)
            loading += percent
            print(f"Loading: {loading}")

        for overlayScene in overlay_scenes:
            self.overlay_scenes[overlayScene] = overlayScene(self)
            loading += percent
            print(f"Loading: {loading}")