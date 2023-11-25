import pygame
from config import *
from sprites import *

# Iniciando dados   
def tela_jogo(window):
    clock = pygame.time.Clock()
    pygame.font.init()

    # Grupos de sprites
    all_sprites = pygame.sprite.Group()
    all_obstaculos = pygame.sprite.Group()

    # Adicionando o jogador
    player = jogador()
    all_sprites.add(player)

    tick_inicial = 0 # Tick inicial (parâmetro para gerar os obstáculos)
    score = 0 # Inicia pontuação
    # Loop principal do jogo
    game = True
    while game:
        clock.tick(FPS)
        # Atualiza eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                
            # Se o usuário apertar espaço, o jogador "pula"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.speedy = 10
        
        all_sprites.update() # Roda o método uptade de cada sprite
        
        # Geração dos obstáculos
        now = pygame.time.get_ticks() # Momento atual do jogo
        if now - tick_inicial >= 2000: # Tempo entre o surgimento de cada par de obstáculos (4 segundos)
            obstaculo1 = obstaculo('inferior')
            obstaculo1.update()
            obstaculo2 = obstaculo('superior', obstaculo1.rect.top)
            obstaculo2.update()
            all_sprites.add(obstaculo1)
            all_sprites.add(obstaculo2)
            all_obstaculos.add(obstaculo1)
            all_obstaculos.add(obstaculo2)

            tick_inicial = now # Atualiza a variável parâmetro

        for obs in all_obstaculos:
            if obs.rect.x < - 100:
                obs.kill()
            if obs.rect.x+ 80 == player.rect.x:
                score += 0.5
        
        hits = pygame.sprite.spritecollide(player, all_obstaculos, True, pygame.sprite.collide_mask)
        if len(hits) > 0:
            game = False
            state = GAME_OVER
        
        window.fill(BLACK)
        all_sprites.draw(window) # Mostra as sprites na tela

        # Pontuação
        text_surface = assets['font'].render(f'{score:.0f}', True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (LARGURA/2, 10)
        window.blit(text_surface, text_rect)

        pygame.display.update() # Atualiza a tela

    return state