import pygame
from os import path
from pygame.locals import *

# Dados gerais do jogo.
LARGURA = 1000  # Largura da tela
ALTURA = 600 # Altura da tela
FPS = 60 # Frames por segundo

INIT = 0
GAME = 1
GAME_OVER = 2
QUIT = 3

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 150)
YELLOW = (255, 255, 0)