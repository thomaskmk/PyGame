import pygame
class jogo:
    def __init__(self):
        pygame.init()
        self.imagem = pygame.image.load('capa.png')
        self.tela = pygame.display.set_mode((1280, 720), 0, 0)
        pygame.display.set_caption('nome do jogo')
        self.game = True

    def eventos(self):
        while self.game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False
                pygame.display.update()
            self.tela.fill((0, 0, 0))
            self.tela.blit(self.imagem, (0, 0))
        return True


jogo = jogo()
jogo.eventos()
pygame.quit()