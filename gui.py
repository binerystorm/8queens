import pygame
import pygame.display as pd
import pygame.event as pe
import time

running = True
pygame.init()

scr = pd.set_mode((400, 400))
pd.set_caption("Chess board")

while running:
    for event in pe.get():
        if event.type == pygame.QUIT:
            running = False
