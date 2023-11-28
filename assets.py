import pygame
import os
from config import *
import pygame

pygame.init()
pygame.font.init()

assets = {}
assets['bg2'] = 'assets/imagem/capa.png'
assets['bg1'] = 'assets/imagem/final.jpg'
assets["aviao"] = "assets/imagem/aviao.png"
assets["obstaculo"] = "assets/imagem/obstaculo.png"
assets['objetos'] = ['assets/imagem/objetos/bola8.png', 'assets/imagem/objetos/cadeira.png', 'assets/imagem/objetos/chave.png', 'assets/imagem/objetos/arrow.png', 'assets/imagem/objetos/foguete.png', 'assets/imagem/objetos/garrafa.png', 'assets/imagem/objetos/pneu.png', 'assets/imagem/objetos/sofa.png']
assets['font'] = pygame.font.Font(None, 40)
