import pygame
import json

#screen
class Settings:


    def __init__(self):
        #game screen settings
        self.WIDTH = 1200
        self.HEIGHT = 700
        self.FPS = 120
        self.DT = None


        #input settings
        self.controls = {}

        #player name
        self.player_name = None

        #game info
        self.actual_fps = None




    #load controls
    def load_controls_from_json(self, json_file):
        with open(json_file) as f:
            data = json.load(f)
            for action in data:
                self.controls[action] = pygame.key.key_code(data[action])


    def load_settings_from_json(self, json_file):
        with open(json_file) as f:
            data = json.load(f)
            self.player_name = data["player_name"]
        print(self.player_name)


    #get key name
    def get_key_name(self, action):
        key = self.controls[action]
        return pygame.key.name(key)

    def update_game_info(self, clock):
        self.actual_fps = clock.get_fps()



class Colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    GRAY = (128, 128, 128)
    LIGHT_GRAY = (200, 200, 200)
    DARK_GRAY = (50, 50, 50)
    ORANGE = (255, 165, 0)
    PURPLE = (128, 0, 128)
    PINK = (255, 105, 180)
    BROWN = (139, 69, 19)
