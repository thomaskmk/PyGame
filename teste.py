import pygame
from config import *
from sprites import *

# Iniciando dados
pygame.init()
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('joguinho')
window.fill(BLACK)
clock = pygame.time.Clock()
game = True

# Grupos de sprites
all_sprites = pygame.sprite.Group()
all_obstaculos = pygame.sprite.Group()

# Adicionando o jogador
player = jogador()
all_sprites.add(player)

tick_inicial = 0 # Tick inicial (parâmetro para gerar os obstáculos)

# Loop principal do jogo
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
    
    # Geração dos obstáculos
    now = pygame.time.get_ticks() # Momento atual do jogo
    if now - tick_inicial >= 4000: # Tempo entre o surgimento de cada par de obstáculos (4 segundos)
        obstaculo1 = obstaculo('inferior')
        obstaculo1.update()
        obstaculo2 = obstaculo('superior', obstaculo1.rect.top)
        obstaculo2.update()
        all_sprites.add(obstaculo1)
        all_sprites.add(obstaculo2)
        all_obstaculos.add(obstaculo1)
        all_obstaculos.add(obstaculo2)

        tick_inicial = now # Atualiza a variável parâmetro
    
    all_sprites.update() # Roda o método uptade de cada sprite
    all_sprites.draw(window) # Mostra as sprites na tela

    pygame.display.update() # Atualiza a tela
    window.fill(BLACK)

pygame.quit()