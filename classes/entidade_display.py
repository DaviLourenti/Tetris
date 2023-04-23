import os
import pygame

TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_FUNDO = pygame.image.load(os.path.join('imagens', 'fundo.png'))
IMAGEM_CENARIO = pygame.image.load(os.path.join('imagens', 'cenario.png'))

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)

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


def desenhar_tela(tela, Forma, cenario, aglomeração, pontos, nomes_proximas_peças):
    tela.blit(IMAGEM_FUNDO, (0, 0))
    Forma.bloco1.desenhar(tela)
    Forma.bloco2.desenhar(tela)
    Forma.bloco3.desenhar(tela)
    Forma.bloco4.desenhar(tela)

    aglomeração.desenhar(tela)
    cenario.desenhar(tela)
    
    texto = FONTE_PONTOS.render(f"Pontuação: {pontos}", 1, (255, 255, 255))
    tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))
    
    texto2 = FONTE_PONTOS.render(f"{nomes_proximas_peças[1]}{nomes_proximas_peças[2]}", 1, (255, 255, 255))
    tela.blit(texto2, (TELA_LARGURA - 90 - texto.get_width(), 50))
    
    pygame.display.update()
