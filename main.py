import pygame
import sys
pygame.init()
from settings import *




screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE, pygame.NOFRAME)
pygame.display.set_caption("My Game")


clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    screen.fill((30, 30, 30))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
