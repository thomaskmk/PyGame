import pygame
from config import *
from sprites import *
import random

# Sprites
class jogador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('imagem/teste.jpg').convert()
        self.image = pygame.transform.scale(self.image, (25,25))
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA - 0.8*LARGURA
        self.rect.bottom = 10
        self.speedy = 0
        self.accely = -0.5
    
    def update(self):
        self.speedy += self.accely
        self.rect.y -= self.speedy

        if self.rect.y <= 0:
            self.rect.y = 0
            self.speedy = 0
        
        if self.rect.y + 25 >= ALTURA:
            self.rect.y = ALTURA - 25
            self.speedy = 0

class obstaculo(pygame.sprite.Sprite):
    def __init__(self, position, top_inferior = None):
        pygame.sprite.Sprite.__init__(self)

        if position == 'inferior':
            self.image = pygame.image.load('imagem/obstaculo.png').convert()
            self.rect = self.image.get_rect()
            self.rect.top = random.randint(50, ALTURA-100)
        else:
            self.image = pygame.image.load('imagem/obstaculo.png').convert()
            self.rect = self.image.get_rect()
            self.rect.bottom = top_inferior - 50 

        self.rect.centerx = LARGURA
        self.speedx = 1
    
    def update(self):
        self.rect.x -= self.speedx

        # Mantem dentro da tela
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0
##################################################################################


# Jogo
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