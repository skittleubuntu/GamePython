import asyncio
from gui import *
import pygame
import math

class Player:
    def __init__(self, x, y, radius=20, color=(255, 0, 0), speed=5, rotation_speed=5):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.rotation_speed = rotation_speed
        self.angle = 0
        self.shoot = False


    async def handle_input(self):
        keys = pygame.key.get_pressed()


        if keys[pygame.K_LEFT]:
            self.angle -= self.rotation_speed
        if keys[pygame.K_RIGHT]:
            self.angle += self.rotation_speed


        if keys[pygame.K_SPACE] and not self.shoot:
            self.shoot = True
            await asyncio.sleep(2)
            self.shoot = False

        rad = math.radians(self.angle)

        if keys[pygame.K_UP]:
            self.x += math.cos(rad) * self.speed
            self.y += math.sin(rad) * self.speed
        if keys[pygame.K_DOWN]:
            self.x -= math.cos(rad) * self.speed
            self.y -= math.sin(rad) * self.speed


        if keys[pygame.K_a]:
            self.x += math.cos(rad - math.pi/2) * self.speed
            self.y += math.sin(rad - math.pi/2) * self.speed
        if keys[pygame.K_d]:
            self.x += math.cos(rad + math.pi/2) * self.speed
            self.y += math.sin(rad + math.pi/2) * self.speed

    def draw(self, screen):

        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

        if self.shoot:
            Text(100,100, "SHOOT").draw(screen)

        rad = math.radians(self.angle)
        end_x = self.x + math.cos(rad) * self.radius * 2
        end_y = self.y + math.sin(rad) * self.radius * 2
        pygame.draw.line(screen, (255, 255, 255), (self.x, self.y), (end_x, end_y), 2)
