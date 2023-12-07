# This file was created by: Alex Aguerria
# Sources: 
'''
https://youtu.be/nF_crEtmpBo?si=jz-qfuisnQHB_mM3
'''

from settings import *
from sprites import *

import pygame

pygame.init()

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    pygame.display.update()
    clock.tick(30)


