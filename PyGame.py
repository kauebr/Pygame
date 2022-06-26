import pygame
from pygame.locals import *
from sys import exit


pygame.init()
largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Flappy Birds')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    pygame.draw.rect(tela, (255, 0, 0), (333, 33, 33, 40))
    pygame.draw.circle(tela, (000, 0, 120), (340, 420), 40)
    pygame.display.update()
https://www.youtube.com/watch?v=FbgiJnqyF_I&list=PLJ8PYFcmwFOxtJS4EZTGEPxMEo4YdbxdQ&index=3