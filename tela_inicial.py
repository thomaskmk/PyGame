import pygame
class inicio:
    def __init__(self):
        self.imagem = pygame.image.load('imagem/capa.png')
        
    def desenha(self, tela):
        tela.blit(self.imagem, (0, 0))