import pygame
from pygame.locals import *

# Dados gerais do jogo.
LARGURA = 400  # Largura da tela
ALTURA = 800 # Altura da tela
FPS = 30 # Frames por segundo

# Dados gerais do chao:
LARG_CHAO = 2*LARGURA
ALT_CHAO = 100

# Dados gerais do cano:
LARG_CANO = 80
ALT_CANO = 500
ESPACO_CANOS = 200

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


# Velocidade e gravidade
VELOCIDADE = 10
GRAVIDADE = 1
VEL_JOGO = 10
