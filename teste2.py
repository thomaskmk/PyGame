import pygame
import random
from config import *
from assets import *
from pygame.locals import * 

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.speed = VELOCIDADE

        self.image = pygame.image.load('assets/bluebird-downflap.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = LARGURA/2
        self.rect[1] = ALTURA/2   

    def update(self):

        self.speed += GRAVIDADE
        # Update altura
        self.rect[1] += self.speed

    def sobe(self):
        self.speed = -VELOCIDADE

class Canos(pygame.sprite.Sprite):
    def __init__(self, inverte, pos_x, tam_y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("assets/pipe-red.png").convert_alpha() 
        self.image = pygame.transform.scale(self.image, (LARG_CANO, ALT_CANO))

        self.rect = self.image.get_rect()
        self.rect[0] = pos_x
 
        if inverte:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect[1] = -(self.rect[3] - tam_y)
        else:
            self.rect[1] = ALTURA - tam_y 
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self):
        self.rect[0] -= VEL_JOGO


class Chao(pygame.sprite.Sprite):
    def __init__(self, pos_x):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('assets/base.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (LARG_CHAO, ALT_CHAO))

        self.rect = self.image.get_rect()
        self.rect[0] = pos_x
        self.rect[1] = ALTURA-ALT_CHAO
    
    def update(self):
        self.rect[0] -= VEL_JOGO

def fora_tela(sprite):
    return (sprite.rect[0] < -(sprite.rect[2]))
   
def random_canos(pos_x):
    tam = random.randint(100, 300)
    cano = Canos(False, pos_x, tam)
    cano_invertido = Canos(True, pos_x, ALTURA-tam-ESPACO_CANOS)
    return (cano, cano_invertido)   

pygame.init()
screen = pygame.display.set_mode((LARGURA, ALTURA))

BACKGROUND_DAY = pygame.image.load('assets/background-day.png')
BACKGROUND_DAY = pygame.transform.scale(BACKGROUND_DAY, (LARGURA, ALTURA))

bird_group = pygame.sprite.Group()
bird = Bird()  
bird_group.add(bird)

chao_group = pygame.sprite.Group()
for i in range(2):
    chao = Chao(LARG_CHAO*i)
    chao_group.add(chao)

cano_group = pygame.sprite.Group()
for i in range(2):
    canos = random_canos(LARGURA*i+600)
    cano_group.add(canos[0])
    cano_group.add(canos[1])

clock = pygame.time.Clock()
 
# Loop principal do jogo
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bird.sobe()
    
    screen.blit(BACKGROUND_DAY, (0,0))

    if fora_tela(chao_group.sprites()[0]):
        chao_group.remove(chao_group.sprites()[0])

        novo_chao = Chao(LARG_CHAO-20)
        chao_group.add(novo_chao)

    if fora_tela(cano_group.sprites()[0]):
        cano_group.remove(chao_group.sprites()[0])
        cano_group.remove(chao_group.sprites()[0])

        canos = random_canos(LARGURA*2)
        cano_group.add(canos[0])
        cano_group.add(canos[1])


    bird_group.update()
    chao_group.update() 
    cano_group.update()

    bird_group.draw(screen)
    cano_group.draw(screen)
    chao_group.draw(screen)

    pygame.display.update()

    if pygame.sprite.groupcollide(bird_group, chao_group, False, False, pygame.sprite.collide_mask) or pygame.sprite.groupcollide(bird_group, cano_group, False, False, pygame.sprite.collide_mask):
        break
pygame.quit()   