import pygame
from pygame.locals import *

# Dados gerais do jogo.
LARGURA = 400  # Largura da tela
ALTURA = 700 # Altura da tela
FPS = 60 # Frames por segundo

# Dados gerais do chao:
LARG_CHAO = 2*LARGURA
ALT_CHAO = 100

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define o fundo
BACKGROUND_DAY = pygame.image.load('assets/background-day.png')

# Velocidade e gravidade
VELOCIDADE = 8
GRAVIDADE = 1
VEL_JOGO = 10
