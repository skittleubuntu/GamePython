import pygame

from client import Client
from gui import *
from player import *

class Battle():
    def __init__(self, screen, exit_from_battle):
        self.screen = screen
        self.gui = GUI()
        self.main_player = Player(100,100)
        self.exit_window = ExitWindow(self.screen, exit_from_battle, self.close_exit_window)
        self.exit_window_opened = False

        self.client = Client(self.main_player)
        self.client_started = False

        self.other_players = {}



    def draw(self):
        pygame.draw.circle(self.screen, (255, 0, 255), (10, 10), 10)
        if self.exit_window_opened:
            self.exit_window.draw()
            self.exit_window.gui.check_buttons()


    async def update(self):
        if not self.client_started:
            loop = asyncio.get_running_loop()
            await self.client.start(loop)

            self.client_started = True


        asyncio.create_task(self.main_player.handle_input())

        self.main_player.draw(self.screen)

        data = self.client.get_data()
        if data is not None and "players" in data:
            for key, pdata in data["players"].items():

                if key == str(self.client.transport.get_extra_info("sockname")):
                    continue

                if key not in self.other_players:
                    self.other_players[key] = ClientPlayer(pdata["pos"]["x"], pdata["pos"]["y"])

                self.other_players[key].update_from_server(pdata)
                self.other_players[key].tick()
                self.other_players[key].draw(self.screen)





        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            print("Presed")
            self.exit_window_opened = True


        await self.client.send_info(self.main_player.get_data())

    def close_exit_window(self):
        self.exit_window_opened = False





class ExitWindow():
    def __init__(self, screen, exit_from_battle, close_exit_window):
        self.screen = screen
        self.gui = GUI()
        self.gui.add_button(Button(100,200, callback=exit_from_battle, text="Yes"))
        self.gui.add_button(Button(200, 200, callback=close_exit_window, text="No"))

    def draw(self):
        for button in self.gui.buttons:
            button.draw(self.screen)

