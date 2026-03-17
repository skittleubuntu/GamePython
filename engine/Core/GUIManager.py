import pygame.draw

from engine.Core.SceneManager import SceneManager
from engine.Settings.settings import Colors, Settings

#make a text size lower and lower while we dont find a optimal size
#--OPTIMIZE REQUIRED
def get_optimal_size(text, width):
    textSize = width
    while True:
        font = pygame.font.Font("engine/Settings/Fonts/Pixel.ttf", textSize)
        if font.size(text)[0] <= width - 20:
            break
        textSize -= 1

    return textSize



class Text:
    def __init__(self,x=100,y=100, textSize=50,color=Colors.WHITE, text=None, bg=None):
        #base text parametrs
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
        #todo bg


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

        self.font = pygame.font.Font("engine/Settings/Fonts/Pixel.ttf", get_optimal_size(self.text, self.width))

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


    def is_hovered(self, m_pos):
        return (m_pos[0] > self.x and m_pos[0] < self.x + self.width) and (m_pos[1] > self.y and m_pos[1] < self.y + self.height)


class Entry():
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

        self.font = pygame.font.Font("engine/Settings/Fonts/Pixel.ttf", get_optimal_size(self.text, self.width) // 2)


    def is_hovered(self, m_pos):
        return (m_pos[0] > self.x and m_pos[0] < self.x + self.width) and (m_pos[1] > self.y and m_pos[1] < self.y + self.height)

    def draw(self,screen):

        #draw entry, check selecting

        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height))

        if self.selected:
            pygame.draw.rect(screen, self.color_selected, (self.x,self.y,self.width,self.height), 2)

        #draw text
        if self.writed_text != "":
            text = self.font.render(self.writed_text, True, Colors.WHITE)
        else:
            text = self.font.render(self.text, True, Colors.WHITE)
        textRect = text.get_rect()
        textRect.center = (self.x + self.width//3 , self.y + self.height//2)
        screen.blit(text,textRect)

class GUI():
    def __init__(self, scene_manager:SceneManager):
        #gui elements for update
        self.buttons = []
        self.texts = []
        self.entries = []


        #entries placed by id
        self.entries_id = {}
        self.selected_entry = None

        #scene manager for adaptive checking
        self.scene_manager = scene_manager

        # Events from button
        self.events = []


    #add a new button to gui boxes
    def add_button(self, button:Button):
        self.buttons.append(button)

    # add a new text to gui boxes
    def add_text(self, text: Text):
        self.texts.append(text)


    #add a new entry and id for this entry is important for future import text from entries
    def add_entry(self, entry:Entry, id):
        self.entries.append(entry)
        #cannot exist 2 entries with same id
        #todo cheking entries canot be 2 same id
        self.entries_id[id] = entry

    #when we select a new entry all previous entries ale unselected
    def make_all_entry_unselected(self):
        for entry in self.entries:
            entry.selected = False
        self.selected_entry = None

    #update buttons (is their hovered or not)
    def update_elements(self):

            #button updates
            m_pos = pygame.mouse.get_pos()
            for button in self.buttons:
                if button.is_hovered(m_pos) and self.scene_manager.overlay_scene is None:
                    button.hovered = True
                else:
                    button.hovered = False
                #todo mouse system
                if button.hovered and self.scene_manager.inputSystem.is_lmb_pressed:
                    self.events.append(button.callback)
                    break

            #entry updates

            for entry in self.entries:

                if entry.is_hovered(m_pos) and self.scene_manager.overlay_scene is None and self.scene_manager.inputSystem.is_lmb_pressed:
                    self.make_all_entry_unselected()
                    entry.selected = True
                    print("new seelcted entri")
                    self.selected_entry = entry
                    break
                elif self.scene_manager.inputSystem.is_lmb_pressed:
                    self.make_all_entry_unselected()




            if self.selected_entry is not None:
                letter = self.scene_manager.inputSystem.get_pressed_letter()
                key = self.scene_manager.inputSystem.get_pressed_key()
                if key == pygame.K_BACKSPACE:
                    self.selected_entry.writed_text = self.selected_entry.writed_text[:-1]

                elif letter:
                    self.selected_entry.writed_text += letter









    #draw all elements (Button, Text, Entry)
    def draw_elements(self,screen):
        for button in self.buttons:
            button.draw(screen)

        for text in self.texts:
            text.draw(screen)

        for entry in self.entries:
            entry.draw(screen)
