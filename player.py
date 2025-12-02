import asyncio
import json

from gui import *
import pygame
import math

class Player:
    def __init__(self, x, y, radius=20, color=(255, 0, 0), speed=5, rotation_speed=5, angle=0):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.rotation_speed = rotation_speed
        self.angle = angle
        self.shoot = False


        self.data = {"pos": {"x": self.x, "y":self.y, "angle":self.angle},
                     "move":{"up":False, "down":False, "right":False, "left":False},
                     "rotate":{"left":False, "right":False}}



    async def handle_input(self):
        keys = pygame.key.get_pressed()


        if keys[pygame.K_LEFT]:
            self.angle -= self.rotation_speed
        if keys[pygame.K_RIGHT]:
            self.angle += self.rotation_speed


        if keys[pygame.K_SPACE] and not self.shoot:
            self.shoot = True
            await asyncio.sleep(0.5)
            self.shoot = False

        rad = math.radians(self.angle)

        self.data["rotate"]["left"] = keys[pygame.K_LEFT]
        self.data["rotate"]["right"] = keys[pygame.K_RIGHT]

        if keys[pygame.K_w]:
            self.x += math.cos(rad) * self.speed
            self.y += math.sin(rad) * self.speed
        if keys[pygame.K_s]:
            self.x -= math.cos(rad) * self.speed
            self.y -= math.sin(rad) * self.speed


        if keys[pygame.K_a]:
            self.x += math.cos(rad - math.pi/2) * self.speed
            self.y += math.sin(rad - math.pi/2) * self.speed
        if keys[pygame.K_d]:
            self.x += math.cos(rad + math.pi/2) * self.speed
            self.y += math.sin(rad + math.pi/2) * self.speed

        self.data["move"]["up"] = keys[pygame.K_w]
        self.data["move"]["down"] = keys[pygame.K_s]
        self.data["move"]["left"] = keys[pygame.K_a]
        self.data["move"]["right"] = keys[pygame.K_d]

        self.data["pos"]["x"] = self.x
        self.data["pos"]["y"] = self.y
        self.data["pos"]["angle"] = self.angle
        self.data["shoot"] = self.shoot

    def draw(self, screen):

        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

        if self.shoot:
            Text(100,100, "SHOOT").draw(screen)

        rad = math.radians(self.angle)
        end_x = self.x + math.cos(rad) * self.radius * 2
        end_y = self.y + math.sin(rad) * self.radius * 2
        pygame.draw.line(screen, (255, 255, 255), (self.x, self.y), (end_x, end_y), 2)


    def eat_data(self, data):

        print(type(data))

        key = data["players"]
        key = list(key.keys())[0]

        data = data["players"][key]

        print("I change pos from server")


        target_x = data["pos"]["x"]
        target_y = data["pos"]["y"]
        target_angle = data["pos"]["angle"]


        lerp_speed = 0
        self.x += (target_x - self.x) * lerp_speed
        self.y += (target_y - self.y) * lerp_speed
        self.angle += (target_angle - self.angle) * lerp_speed


    def get_data(self):
        return self.data



class ServerPlayer:
    def __init__(self, x, y, angle=0, radius=20, speed=5, rotation_speed=5):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.rotation_speed = rotation_speed
        self.angle = angle
        self.shoot = False

        self.data = {"pos": {"x": self.x, "y": self.y, "angle": self.angle},
                     "move": {"up": False, "down": False, "right": False, "left": False},
                     "rotate": {"left": False, "right": False},
                     "shoot": False}

    def update(self, client_data):
        """Оновлюємо позицію гравця за даними від клієнта"""
        # Оновлюємо прапорці
        self.data["move"] = client_data["move"]
        self.data["rotate"] = client_data["rotate"]
        self.shoot = client_data.get("shoot", False)
        self.data["shoot"] = self.shoot

        # Рухаємо кут
        if self.data["rotate"]["left"]:
            self.angle -= self.rotation_speed
        if self.data["rotate"]["right"]:
            self.angle += self.rotation_speed

        rad = math.radians(self.angle)

        # Рухаємо по осі
        if self.data["move"]["up"]:
            self.x += math.cos(rad) * self.speed
            self.y += math.sin(rad) * self.speed
        if self.data["move"]["down"]:
            self.x -= math.cos(rad) * self.speed
            self.y -= math.sin(rad) * self.speed
        if self.data["move"]["left"]:
            self.x += math.cos(rad - math.pi / 2) * self.speed
            self.y += math.sin(rad - math.pi / 2) * self.speed
        if self.data["move"]["right"]:
            self.x += math.cos(rad + math.pi / 2) * self.speed
            self.y += math.sin(rad + math.pi / 2) * self.speed


        self.data["pos"]["x"] = self.x
        self.data["pos"]["y"] = self.y
        self.data["pos"]["angle"] = self.angle

        print(self.data)

    def get_data(self):
        return self.data


def lerp(a, b, t):
    return a + (b - a) * t

class ClientPlayer:
    def __init__(self, x, y, angle=0, color=(0, 255, 0), radius=20, speed_lerp=0.2):
        self.x = x
        self.y = y
        self.angle = angle
        self.radius = radius
        self.color = color


        self.target_x = x
        self.target_y = y
        self.target_angle = angle
        self.shoot = False

        self.speed_lerp = speed_lerp

    def update_from_server(self, data):

        pos = data["pos"]
        self.target_x = pos["x"]
        self.target_y = pos["y"]
        self.target_angle = pos["angle"]
        self.shoot = data.get("shoot", False)

    def tick(self):

        self.x = lerp(self.x, self.target_x, self.speed_lerp)
        self.y = lerp(self.y, self.target_y, self.speed_lerp)
        self.angle = lerp(self.angle, self.target_angle, self.speed_lerp)

    def draw(self, screen):

        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

        rad = math.radians(self.angle)
        end_x = self.x + math.cos(rad) * self.radius * 2
        end_y = self.y + math.sin(rad) * self.radius * 2
        pygame.draw.line(screen, (255, 255, 255), (self.x, self.y), (end_x, end_y), 2)

        if self.shoot:

            Text(100, 100, "SHOOT", font_size=20).draw(screen)