import pygame
from config import *
from sprites import *
from tela_inicial import *
from tela_jogo import *
from tela_game_over import*
from assets import *

# Inicia o pygame
pygame.init()
pygame.mixer.init()

# Abre a janela
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Avião perdido')

# Alterna os estados do jogo
state = INIT
while state != QUIT:
    if state == INIT:
        # Toca a musica do inicio
        pygame.mixer.music.load('assets/sons/musica_de_fundo.mp3')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(loops=-1)

        state = tela_inicial(window)

    if state == GAME:
        x = tela_jogo(window)
        state = x[0]

    if state == GAME_OVER:
        # Toca a musica da tela de game_over
        pygame.mixer.music.load('assets/sons/musica_game_over.mp3')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(loops=-1)
        score = x[1]
        
        state = tela_game_over(window, score)

pygame.quit()