import pygame
import asyncio
from settings import Settings
from main_menu import *
from battle import Battle
from player import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))
        pygame.display.set_caption("Game Example")
        self.clock = pygame.time.Clock()


        # windows
        self.battle = Battle(self.screen, exit_from_battle=self.exit_from_battle)

        self.setting_window = SettingsMenu(self.screen)


        self.main_window = MainMenu(self.screen,
                                    start_callback=self.start_battle,
                                    settings_callback=self.open_settings)



        self.current_window = self.main_window


    def exit_from_battle(self):
        self.current_window = self.main_window


    def start_battle(self):
        self.current_window = self.battle

    def open_settings(self):
        self.current_window = self.setting_window

    async def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

            self.screen.fill((0, 0, 0))


            self.current_window.gui.check_buttons()
            self.current_window.update()

            self.current_window.draw()

            pygame.display.flip()
            self.clock.tick(60)
            await asyncio.sleep(0)

    def quit(self):
        pygame.quit()
        import sys
        sys.exit()


if __name__ == "__main__":
    asyncio.run(Game().run())
