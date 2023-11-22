import pygame
from config import *
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


class Chao(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('assets/base.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (LARG_CHAO, ALT_CHAO))

        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = ALTURA-ALT_CHAO
    
    def update(self):
        self.rect[0] -= VEL_JOGO

def fora_tela(sprite):
    return sprite.rect[0] < -(sprite.rect[2])



pygame.init()
screen = pygame.display.set_mode((LARGURA, ALTURA))

BACKGROUND_DAY = pygame.transform.scale(BACKGROUND_DAY, (LARGURA, ALTURA))

bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)   

chao_group = pygame.sprite.Group()
for i in range(2):
    chao = Chao(LARG_CHAO*i)
    chao_group.add(chao)




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



    bird_group.update()
    chao_group.update()

    bird_group.draw(screen)
    chao_group.draw(screen)

    if pygame.sprite.groupcollide(bird_group, chao_group, False, False, pygame.sprite.collide_mask):
        break
 
    pygame.display.update()
pygame.quit()