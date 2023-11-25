import pygame
from config import *
from sprites import *
from tela_inicial import *
from tela_jogo import *
from tela_game_over import*
from assets import *

pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('sim')

state = INIT
while state != QUIT:
    if state == INIT:
        state = tela_inicial(window)
    if state == GAME:
        state = tela_jogo(window)
    if state == GAME_OVER:
        state = tela_game_over(window)

pygame.quit()