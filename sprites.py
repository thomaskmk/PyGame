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

        self.ultimo_tiro = pygame.time.get_ticks()
        self.intervalo = 1000
    
    def update(self):
        self.rect.y += self.speedy

        if self.rect.y <= 0:
            self.rect.y = 1
            self.speedy = 0
        
        if self.rect.y >= ALTURA:
            self.rect.y = ALTURA - 25
            self.speedy = 0
    
    def atira(self, grupos):
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
        tempo = now - self.ultimo_tiro

        # Se já pode atirar novamente...
        if tempo > self.intervalo:
            # Marca o tick da nova imagem.
            self.ultimo_tiro = now
            # A nova bala vai ser criada logo acima e no centro horizontal da nave
            new_bullet = tiro(self.rect.y)
            grupos[0].add(new_bullet) # Adiciona no grupo all_sprites
            grupos[1].add(new_bullet) # Adiciona no grupo de tiros


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
        
        self.img = random.choice(assets['objetos'])
        self.image = pygame.image.load(self.img).convert_alpha()
        self.image = pygame.transform.scale(self.image,(60, 60))
        self.rect = self.image.get_rect()
        self.rect.top = random.randint(150, ALTURA-100)
        self.rect.x = LARGURA + 100
        self.speedx = 12
        self.mask = pygame.mask.from_surface(self.image)
        
    def update(self):
        self.rect.x -= self.speedx


        #if self.img != 'assets/imagem/objetos/arrow.png' and self.img != 'assets/imagem/objetos/foguete.png':
            #self.image = pygame.transform.rotate(self.image, 1)

class tiro(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, centerx):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(assets['tiros']).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.speedx = 20  # Velocidade fixa para cima

    def update(self):
        # A bala só se move no eixo x
        self.rect.x += self.speedx

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.x >= LARGURA + 200:
            self.kill()


        