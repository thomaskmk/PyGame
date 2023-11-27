from typing import Any
import pygame
import random
from assets import *
from config import *

class jogador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(assets['aviao']).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,30))
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA - 0.8*LARGURA
        self.rect.bottom = 10
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

        if position == 'inferior':
            self.image = pygame.image.load(assets['obstaculo']).convert()
            self.rect = self.image.get_rect()
            self.rect.top = random.randint(150, ALTURA-100)
        else:
            self.image = pygame.image.load(assets['obstaculo']).convert()
            self.rect = self.image.get_rect()
            self.rect.bottom = top_obs_inferior - 150

        self.rect.x = LARGURA
        self.speedx = 4

    def update(self):
        self.rect.x -= self.speedx