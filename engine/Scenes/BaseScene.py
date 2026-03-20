from abc import ABC, abstractmethod


class Scene(ABC):
    #Base class

    @abstractmethod
    def render(self, screen):
        #Scene render
        pass

    @abstractmethod
    def update(self):
        #Logic update
        pass

    @abstractmethod
    def handle_button(self):
        #input handeling
        pass


    def update_gui(self):
        self.gui.update_elements()
        for event in self.gui.events:
            self.sceneManager.add_event(event)
        self.gui.events = []

    def set_kwargs(self, **kwargs):
        pass


class OverlayScene(ABC):

    @abstractmethod
    def render(self, screen):
        # Scene render
        pass

    @abstractmethod
    def update(self):
        # Logic update
        pass

    @abstractmethod
    def handle_button(self):
        # input handeling
        pass

    def update_gui(self):
        self.gui.update_elements()
        for event in self.gui.events:
            self.sceneManager.add_event(event)
        self.gui.events = []

    def set_kwargs(self, **kwargs):
        pass