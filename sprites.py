import pygame
import random
from assets import *
from config import *

class jogador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(assets['aviao']).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 60))
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA - 0.8*LARGURA
        self.rect.bottom = 10
        self.mask = pygame.mask.from_surface(self.image)
        self.speedy = 0
    
    def update(self):
        self.rect.y -= self.speedy

        if self.rect.y <= 0:
            self.rect.y = 0
            self.speedy = 0
        
        if self.rect.y + 25 >= ALTURA:
            self.rect.y = ALTURA - 25
            self.speedy = 0

class obstaculo(pygame.sprite.Sprite):
    def __init__(self, position, top_obs_inferior = None):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(assets['obstaculo']).convert_alpha()
        self.image = pygame.transform.scale(self.image, (LARG_CANO, ALT_CANO))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
 
        if position == 'inferior':
            self.rect.top = random.randint(200, ALTURA-50)
        else:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottom = top_obs_inferior - 150

        self.rect.x = LARGURA + 200
        self.speedx = 7

    def update(self):
        self.rect.x -= self.speedx

class objetos(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = random.choice(assets['objetos'])
        self.image = pygame.image.load(self.image).convert_alpha()
        self.image = pygame.transform.scale(self.image,(60, 60))
        self.rect = self.image.get_rect()
        self.rect.top = random.randint(150, ALTURA-100)
        self.rect.x = LARGURA + 100
        self.speedx = 12
        self.mask = pygame.mask.from_surface(self.image)
        
    def update(self):
        self.rect.x -= self.speedx