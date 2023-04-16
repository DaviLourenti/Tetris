import os
import pygame

TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_FUNDO = pygame.image.load(os.path.join('imagens', 'fundo.png'))
IMAGEM_CENARIO = pygame.image.load(os.path.join('imagens', 'cenario.png'))


class Cenario:
    
    LARGURA = IMAGEM_CENARIO.get_width()
    ALTURA = IMAGEM_CENARIO.get_height()
    IMAGEM = IMAGEM_CENARIO
    IMG_ROTACIONADA = pygame.transform.rotate(IMAGEM, 90)

    def __init__(self, y):
        self.y = y

    def desenhar(self, tela):
        tela.blit(self.IMAGEM, (0.9, self.y))  # chão
        tela.blit(self.IMG_ROTACIONADA, (2, 3))  # parede esquerda
        tela.blit(self.IMG_ROTACIONADA, (476, 3))  # parede direita


def desenhar_tela(tela, Forma, cenario, aglomeração):
    tela.blit(IMAGEM_FUNDO, (0, 0))
    Forma.bloco1.desenhar(tela)
    Forma.bloco2.desenhar(tela)
    Forma.bloco3.desenhar(tela)
    Forma.bloco4.desenhar(tela)

    aglomeração.desenhar(tela)
    cenario.desenhar(tela)
    pygame.display.update()
