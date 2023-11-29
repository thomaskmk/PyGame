import pygame
import os
from config import *

pygame.init()
pygame.font.init()

assets = {}
assets['bg2'] = 'assets/imagem/aviao_perdido.png'
assets['bg1'] = 'assets/imagem/game_over.png'
assets["aviao"] = "assets/imagem/aviao.png"
assets["obstaculo"] = ["assets/imagem/predio.png", "assets/imagem/predio2.png", "assets/imagem/predio3.png"]
assets['nuvem'] = 'assets/imagem/cloud.png'
assets['objetos'] = ['assets/imagem/objetos/bola8.png', 'assets/imagem/objetos/cadeira.png', 'assets/imagem/objetos/chave.png', 'assets/imagem/objetos/arrow.png', 'assets/imagem/objetos/foguete.png', 'assets/imagem/objetos/garrafa.png', 'assets/imagem/objetos/pneu.png', 'assets/imagem/objetos/sofa.png']
assets['font'] = pygame.font.Font('assets/font/ka1.ttf', 42)
assets["background"] = "assets/imagem/background.png"
assets["tiros"] = "assets/imagem/tiro_laser.png"

explosion_anim = []
for i in range(9):
    # Os arquivos de animação são numerados de 00 a 08
    filename = os.path.join('assets/imagem/explosao', 'regularExplosion0{}.png'.format(i))
    explosion_anim.append(filename)
assets['exp_anim'] = explosion_anim