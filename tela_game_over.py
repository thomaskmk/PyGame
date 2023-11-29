import pygame
from assets import *
from config import *

def tela_game_over(window, score):
    clock = pygame.time.Clock()
    bg = pygame.image.load(assets['bg1']).convert()
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
                if event.key == pygame.K_SPACE:
                    state = INIT
                    running = False
                if event.key == pygame.K_ESCAPE:
                    state = QUIT
                    running = False

        window.fill(BLACK)
        window.blit(bg, bg_rect)

        text_surface = assets['font'].render(f'{score}', True, (255, 189, 89))
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (570, 230)
        window.blit(text_surface, text_rect)

        pygame.display.update()

    return state

