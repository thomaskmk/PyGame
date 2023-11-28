import pygame
from assets import *
from config import *

def tela_inicial(window):
    clock = pygame.time.Clock()
    
    bg = pygame.image.load(assets['bg2']).convert()
    bg = pygame.transform.scale(bg, (LARGURA, ALTURA))
    bg_rect = bg.get_rect()
    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            if event.type == pygame.KEYDOWN:
                if not event.key == pygame.K_ESCAPE:
                    state = GAME
                    running = False
                else:
                    state = QUIT
                    running = False
                    
        window.blit(bg, bg_rect)
        pygame.display.update()

    return state