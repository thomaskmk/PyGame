import pygame
from config import *
from tela_inicial import *

class jogo:
    def __init__(self):
        pygame.init()
        self.game = True
        self.tela = pygame.display.set_mode((1280, 720), 0, 0)
        pygame.display.set_caption('nome do jogo')

    def eventos(self):
        tela_inicial = True
        
        while self.game:
            if tela_inicial:
                self.tela.fill((0, 0, 0))
                x = inicio()
                x.desenha(self.tela)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game = False
                    if event.type == pygame.KEYDOWN:
                        self.game = True

            pygame.display.update()

        return True

jogo = jogo()
jogo.eventos()
pygame.quit()