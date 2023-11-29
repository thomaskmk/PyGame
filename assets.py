import pygame
import os
from config import *
import pygame

pygame.init()
pygame.font.init()

assets = {}
assets['bg2'] = 'assets/imagem/aviao_perdido.png'
assets['bg1'] = 'assets/imagem/game_over.png'
assets["aviao"] = "assets/imagem/aviao.png"
assets["obstaculo"] = "assets/imagem/arvore1_pixel.png"
assets['objetos'] = ['assets/imagem/objetos/bola8.png', 'assets/imagem/objetos/cadeira.png', 'assets/imagem/objetos/chave.png', 'assets/imagem/objetos/arrow.png', 'assets/imagem/objetos/foguete.png', 'assets/imagem/objetos/garrafa.png', 'assets/imagem/objetos/pneu.png', 'assets/imagem/objetos/sofa.png']
assets['font'] = pygame.font.Font(None, 40)
assets["background"] = "assets/imagem/ceu_pixels.png"