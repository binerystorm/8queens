import pygame
import pygame.display as pd
import pygame.event as pe
import time

class Piece:
    spacing = 25
    color_table = {
    1: (0,255,0)
    2: (255,0,0)
    }

    def __init__(self, type: int, screen):
        self.type = type
        self.color = self.color_table[self.type]
        self.pos = (1*self.spacing, 1*self.spacing)
        self.peice = pygame.Rect(screen, )

    def move(self, x, y):
        self.pos = (self.pos[0] + (x * self.spacing), self.pos[1] + (y * self.spacing))


def draw_background(scr):
    width, height = scr.get_size()
    X = Y = 8
    xspacing = width//X
    yspacing = height//Y
    color = 0

    for y in range(Y):
        for x in range(X):
            if (y % 2) == 0:
                if (color % 2) == 0:
                    pygame.draw.rect(scr, (0,0,0), pygame.Rect(x*xspacing, y*yspacing, xspacing, yspacing))
                else:
                    pygame.draw.rect(scr, (200,200,200), pygame.Rect(x*xspacing, y*yspacing, xspacing, yspacing))
            else:
                if (color % 2) == 0:
                    pygame.draw.rect(scr, (200,200,200), pygame.Rect(x*xspacing, y*yspacing, xspacing, yspacing))
                else:
                    pygame.draw.rect(scr, (0,0,0), pygame.Rect(x*xspacing, y*yspacing, xspacing, yspacing))
            color += 1


running: bool = True
pygame.init()

scr = pd.set_mode((400, 400))
pd.set_caption("Chess board")

while running:
    draw_background(scr)
    # pygame.draw.rect(scr, (225,0,0), pygame.Rect(100,100,100,100))
    pd.flip()
    for event in pe.get():
        if event.type == pygame.QUIT:
            running = False
