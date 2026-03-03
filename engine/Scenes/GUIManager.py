import pygame.draw
from engine.Settings.settings import Colors

class Button():
    def __init__(self,x=100,y=100, width=100, height=100,color=Colors.RED, color_hover=Colors.GREEN, text=None,callback=None):
        #base button parametrs
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.color_hover = color_hover
        self.callback = callback
        self.text = text

        #buttons states
        self.active = True
        self.hovered = False




    def draw(self,screen):
        if self.hovered:
            pygame.draw.rect(screen, self.color_hover, (self.x,self.y,self.width,self.height))
        else:
            pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height))


        #TODO text

    def is_hovered(self, m_pos):
        return (m_pos[0] > self.x and m_pos[0] < self.x + self.width) and (m_pos[1] > self.y and m_pos[1] < self.y + self.height)


class GUI():
    def __init__(self):
        #gui elements for update
        self.buttons = []
        self.texts = []
        self.entries = []

        # Events from button
        self.events = []


    #add a new button to gui boxes
    def add_button(self, button:Button):
        self.buttons.append(button)

    def update_elements(self):
        m_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            if button.is_hovered(m_pos):
                button.hovered = True
            else:
                button.hovered = False
            #todo
            if button.hovered and pygame.mouse.get_pressed()[0]:
                self.events.append(button.callback)


    def draw_elements(self,screen):
        for button in self.buttons:
            button.draw(screen)
