import os
import random
import pygame

IMAGENS_BLOCO = [
    pygame.image.load(os.path.join('imagens', 'bloco_azul.jpg')),
    pygame.image.load(os.path.join('imagens', 'bloco_vermelho.jpg')),
    pygame.image.load(os.path.join('imagens', 'bloco_amarelo.jpg')),
    pygame.image.load(os.path.join('imagens', 'bloco_verde.jpg')),
    pygame.image.load(os.path.join('imagens', 'bloco_rosa.jpg')),
    pygame.image.load(os.path.join('imagens', 'bloco_roxo.jpg')),
]

class Bloco:
    IMGS = IMAGENS_BLOCO

    def __init__(self, x, y, index_imagem):
        self.x = x
        self.altura = y
        self.y = y
        self.imagem = self.IMGS[index_imagem]

    def baladinha_bloco(self):
        self.imagem = self.IMGS[random.randint(0, len(self.IMGS)-1)]
        self.y -= 25

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, self.y))
