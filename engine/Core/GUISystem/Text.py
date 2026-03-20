import pygame

from engine.Core.GUISystem.GUIElement import GUIElement
from engine.Settings.settings import Colors, Settings

class Text(GUIElement):
    def __init__(self, x=100, y=100, textSize=50, color=Colors.WHITE, text=None, bg=None):
        # base text parametrs
        self.x = x
        self.y = y
        self.color = color
        self.text = text
        self.textSize = textSize
        self.bg = bg


        self.font = pygame.font.Font("engine/Settings/Fonts/Pixel.ttf", self.textSize)

    def draw(self, screen):
        # draw text
        text = self.font.render(self.text, True, self.color)
        textRect = text.get_rect()
        textRect.topleft = (self.x, self.y)
        screen.blit(text, textRect)
        # todo bg

    def edit_text(self, text_to_change):
        self.text = text_to_change
