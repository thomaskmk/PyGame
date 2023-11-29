import pygame
from config import *
from sprites import *
from assets import *

# Iniciando dados   
def tela_jogo(window):
    clock = pygame.time.Clock()

    background = pygame.image.load(assets["background"]).convert()
    background = pygame.transform.scale(background, (LARGURA, ALTURA))
    background_rect = background.get_rect()
    pygame.font.init()

    # Grupos de sprites
    all_sprites = pygame.sprite.Group()
    all_obstaculos = pygame.sprite.Group()
    all_objetos = pygame.sprite.Group()

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
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game = False
                state = QUIT
            # Se o usuário apertar espaço, o jogador "pula"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.speedy = 10
                if event.key == pygame.K_DOWN:
                    player.speedy = -10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player.speedy = 0
                if event.key == pygame.K_DOWN:
                    player.speedy = 0
        
        # Geração dos obstáculos
        now = pygame.time.get_ticks() # Momento atual do jogo
        if now - tick_inicial >= 1000: # Tempo entre o surgimento de cada par de obstáculos (4 segundos)
            obstaculo1 = obstaculo('inferior')
            obstaculo1.update()
            obstaculo2 = obstaculo('superior', obstaculo1.rect.top)
            obstaculo2.update()
            obj = objetos()
            obj.update()
            
            all_sprites.add(obstaculo1)
            all_sprites.add(obstaculo2)
            all_sprites.add(obj)
            all_obstaculos.add(obstaculo1)
            all_obstaculos.add(obstaculo2)
            all_objetos.add(obj)

            tick_inicial = now # Atualiza a variável parâmetro

        if pygame.sprite.spritecollide(player, all_obstaculos, False, pygame.sprite.collide_mask):
            game = False
            state = GAME_OVER
        
        all_sprites.update()   # Roda o método uptade de cada sprite
        window.fill(BLACK)
        window.blit(background, background_rect)
        all_sprites.draw(window) # Mostra as sprites na tela

        # Pontuação
        text_surface = assets['font'].render(f'{score}', True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (LARGURA/2, 10)
        window.blit(text_surface, text_rect)

        pygame.display.update() # Atualiza a tela

    return state