import pygame
from config import *
from sprites import *

pygame.init()
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('joguinho')
window.fill(BLACK)

game = True

clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
all_obstaculos = pygame.sprite.Group()

player = jogador()


all_sprites.add(player)


while game:
    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.speedy = 10
    
    
    obstaculo1 = obstaculo('inferior')
    obstaculo2 = obstaculo('superior', obstaculo1.rect.top)
    all_sprites.add(obstaculo1)
    all_sprites.add(obstaculo2)
    all_obstaculos.add(obstaculo1)
    all_obstaculos.add(obstaculo2)
    
    all_sprites.update()
    all_sprites.draw(window)

    pygame.display.update()
    window.fill(BLACK)

pygame.quit()