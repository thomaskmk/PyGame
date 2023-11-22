import pygame
from config import *
from telas import *
from telas import *
from sprites import *
from pygame.locals import *

class jogo:
    def __init__(self):
        pygame.init()
        self.game = True
        self.tela = pygame.display.set_mode((LARGURA, ALTURA), 0, 0)
        self.grupo_professor = pygame.sprite.Group()
        pygame.display.set_caption('nome do jogo')
        self.relogio = pygame.time.Clock()

    def eventos(self):
        tela_inicial = True
        jogando = False
        tela_game_over = False
        fim = game_over()
        while self.game:

            if tela_inicial:
                self.tela.fill((0, 0, 0))
                Inicio = inicio()
                Inicio.desenha(self.tela)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_t:
                            tela_inicial = False
                            tela_game_over = True

            elif tela_game_over:
                fim.desenha(self.tela)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game = False

            self.relogio.tick(FPS)
            pygame.display.update()

        return True

jogo = jogo()
jogo.eventos()
pygame.quit()