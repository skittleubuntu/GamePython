from idlelib.debugger_r import GUIAdapter
import asyncio
import pygame
import sys
pygame.init()
from settings import *
from main_menu import *
from battle import Battle






class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Resizable Object")
        self.clock = pygame.time.Clock()

        #windows
        self.battle = Battle(self.screen)
        self.setting_window = SettingsMenu(self.screen)
        self.main_window = MainMenu(self.screen)


        self.current_window = MainMenu(self.screen)




    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

                if event.type == pygame.VIDEORESIZE:
                    Settings.WIDTH, Settings.HEIGHT = event.w, event.h
                    screen = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT), pygame.RESIZABLE)

            key = pygame.key.get_pressed()


            if key[pygame.K_1]:
                self.current_window = self.battle

            if key[pygame.K_2]:
                self.current_window = self.main_window




            self.current_window.draw()
            pygame.display.flip()
            self.clock.tick(60)


    def quit(self):
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    Game().run()





