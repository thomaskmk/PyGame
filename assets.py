import pygame
import os
from config import *
import pygame

pygame.init()
pygame.font.init()

assets = {}
assets["Background"] = "assets/background-day.png"
assets["Base"] = "assets/base.png"
assets['bg2'] = 'assets/imagem/capa.png'
assets['bg1'] = 'assets/imagem/final.jpg'
assets["aviao"] = "assets/imagem/mini.png"
assets["obstaculo"] = "assets/imagem/obstaculo.png"
assets['font'] = pygame.font.Font(None, 40)

