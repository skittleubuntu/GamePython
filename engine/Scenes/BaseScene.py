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
