import random
import display


class Bloco:
    IMGS = display.IMAGENS_BLOCO

    def __init__(self, x, y):
        self.x = x
        self.altura = y
        self.y = y
        self.imagem = self.IMGS[0]

    def baladinha_bloco(self):
        self.imagem = self.IMGS[random.randint(0, len(self.IMGS)-1)]
        self.y -= 25

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, self.y))
