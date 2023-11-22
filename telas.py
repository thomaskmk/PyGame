import pygame

class inicio:
    def __init__(self):
        self.imagem = pygame.image.load('imagem/capa.png')
        
    def desenha(self, tela):
        tela.blit(self.imagem, (0, 0))

class game_over:
    def __init__(self):
        self.imagem = pygame.image.load('imagem/cj_dando_grau.jpg')

    def desenha(self, tela):
        tela.blit(self.imagem, (0, 0))