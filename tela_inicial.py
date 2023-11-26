import pygame
from assets import *
from config import *

def tela_inicial(window):
    clock = pygame.time.Clock()
    bg = pygame.image.load(assets['bg2']).convert()
    bg_rect = bg.get_rect()
    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state = GAME
                    running = False
        window.fill(BLACK)
        window.blit(bg, bg_rect)

    return state