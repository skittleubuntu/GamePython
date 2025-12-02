import pygame
from settings import *

class GUI:
    def __init__(self):
        self._buttons: list[Button] = []
        self._texts: list[Text] = []


    def add_button(self, button):
        self._buttons.append(button)

    def add_text(self, text):
        self._texts.append(text)

    @property
    def buttons(self):
        return self._buttons

    @property
    def texts(self):
        return self._texts

    def check_buttons(self):
        mx, my = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()[0]

        for button in self._buttons:
            button.is_hovered = button.rect.collidepoint(mx, my)
            if pressed and button.is_hovered:
                button.on_click()


class Button:
    def __init__(self, x, y, width=100, height=50, color=Colors.RED, hover_color=Colors.GREEN,
                 text='Button', font_size=30, callback=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.callback = callback

    def draw(self, screen):
        pygame.draw.rect(screen, self.hover_color if self.is_hovered else self.color, self.rect)
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def on_click(self):
        if self.callback:
            self.callback()


class Text:
    def __init__(self, x, y, text, font_size=30, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.color = color

    def draw(self, screen):
        text_surf = self.font.render(self.text, True, self.color)
        screen.blit(text_surf, (self.x, self.y))
