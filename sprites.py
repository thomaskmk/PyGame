import pygame
from config import *

class jogador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('imagem/teste.jpg').convert()
        self.image_menor = pygame.transform.scale(self.image, (128, 128))
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA / 2
        self.rect.bottom = ALTURA - 10
        self.speedx = 0
    
    def update(self):
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > ALTURA:
            self.rect.left = ALTURA