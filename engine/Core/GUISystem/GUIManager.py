import pygame.draw

from engine.Core.GUISystem.GUIElement import GUIElement
from engine.Core.SceneManager import SceneManager
from engine.Settings.settings import Colors, Settings
from engine.Core.GUISystem.Text import Text
from engine.Core.GUISystem.Entry import Entry
from engine.Core.GUISystem.Button import Button









class GUI():
    def __init__(self, scene_manager:SceneManager):
        #gui elements for update
        self.buttons = []
        self.texts = []
        self.entries = []


        #entries,textes placed by id
        self.entries_id = {}
        self.textes_id = {}
        self.selected_entry = None

        #scene manager for adaptive checking
        self.scene_manager = scene_manager

        # Events from button
        self.events = []


    #add a new button to gui boxes
    def add_button(self, button:Button):
        self.buttons.append(button)

    # add a new text to gui boxes
    def add_text(self, text: Text, id=None):
        self.texts.append(text)

        if id:
            self.textes_id[id] = text


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
            #todo update only when mouse is moving
            #button updates
            m_pos = self.scene_manager.inputSystem.get_mouse_pos()
            for button in self.buttons:
                if button.is_hovered(m_pos) and self.scene_manager.overlay_scene is None:
                    button.hovered = True
                else:
                    button.hovered = False
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




    def get_text_by_id(self, id) -> Text:
        #todo checking for correct id
        return self.textes_id[id]


    def get_entry_by_id(self, id) -> Entry:
        # todo checking for correct id
        return self.entries_id[id]





    #draw all elements (Button, Text, Entry)
    def draw_elements(self,screen):
        for button in self.buttons:
            button.draw(screen)

        for text in self.texts:
            text.draw(screen)

        for entry in self.entries:
            entry.draw(screen)
