from engine.Core.GUISystem.GUIElement import GUIElement
import pygame
from engine.Settings.settings import Colors, Settings


class Button(GUIElement):
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

        self.font = pygame.font.Font("engine/Settings/Fonts/Pixel.ttf", self.get_optimal_size())

        #buttons states
        self.active = True
        self.hovered = False




    def draw(self,screen):

        #draw button, check hovering
        if self.hovered:
            pygame.draw.rect(screen, self.color_hover, (self.x,self.y,self.width,self.height))
        else:
            pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height))

        #draw text
        text = self.font.render(self.text, True, Colors.WHITE)
        textRect = text.get_rect()
        textRect.center = (self.x + self.width//2 , self.y + self.height//2)
        screen.blit(text,textRect)

