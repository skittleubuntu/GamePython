from engine.Core.GUISystem.GUIElement import GUIElement
import pygame
from engine.Settings.settings import Colors, Settings

class Entry(GUIElement):
    def __init__(self,x=100,y=100, width=100, height=100,color=Colors.YELLOW, color_selected=Colors.ORANGE, text=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.color_selected = color_selected
        self.text = text


        #when entry is selected we can write a text
        self.selected = False

        #writen text in entry
        self.writed_text = ""

        self.font = pygame.font.Font("engine/Settings/Fonts/Pixel.ttf", self.get_optimal_size() // 2)




    def draw(self,screen):

        #draw entry, check selecting

        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height))

        if self.selected:
            pygame.draw.rect(screen, self.color_selected, (self.x,self.y,self.width,self.height), 2)

        #draw text
        if self.writed_text != "":
            text = self.font.render(self.writed_text, True, Colors.WHITE)
        else:
            text = self.font.render(self.text, True, Colors.GRAY)
        textRect = text.get_rect()
        textRect.center = (self.x + self.width//3 , self.y + self.height//2)
        screen.blit(text,textRect)