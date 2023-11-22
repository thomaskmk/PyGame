import pygame
from config import *
from sprites import *

pygame.init()
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('joguinho')
window.fill((0,0,0))

game = True

clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

player = jogador()
all_sprites.add(player)

while game:
    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.speedx += 4
            if event.key == pygame.K_LEFT:
                player.speedx -= 4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.speedx -= 4
            if event.key == pygame.K_LEFT:
                player.speedx += 4
    
    all_sprites.update()

    window.fill((0,0,0))
    all_sprites.draw(window)

    pygame.display.update()

pygame.quit()