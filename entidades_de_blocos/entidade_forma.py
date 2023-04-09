from random import randint
from . import entidade_bloco
class Forma:
    def __init__(self, x1,y1, x2,y2, x3,y3, x4,y4, aglomeração):
        self.velocidade = 0
        self.giro = 0
        self.colisão = False
        self.conexão_com_player = True
        self.conjunto_de_blocos = aglomeração.conjunto_de_blocos
        self.cor = randint(0, 5)
        
        
        self.bloco1 = entidade_bloco.Bloco(x1, y1, self.cor)
        self.bloco2 = entidade_bloco.Bloco(x2, y2, self.cor)
        self.bloco3 = entidade_bloco.Bloco(x3, y3, self.cor)
        self.bloco4 = entidade_bloco.Bloco(x4, y4, self.cor)

    def bool_colisão_direita(self):
        for c in range(0, len(self.conjunto_de_blocos)):

            if self.bloco1.y == self.conjunto_de_blocos[c].y\
            and self.bloco1.x + 25 == self.conjunto_de_blocos[c].x:
                return True

            elif self.bloco2.y == self.conjunto_de_blocos[c].y\
            and self.bloco2.x + 25 == self.conjunto_de_blocos[c].x:
                return True

            elif self.bloco3.y == self.conjunto_de_blocos[c].y\
            and self.bloco3.x + 25 == self.conjunto_de_blocos[c].x:
                return True

            elif self.bloco4.y == self.conjunto_de_blocos[c].y\
            and self.bloco4.x + 25 == self.conjunto_de_blocos[c].x:
                return True

    def mover_direita(self):
        if self.conexão_com_player == True\
        and self.bloco1.x + 50 < 476\
        and self.bloco2.x + 50 < 476\
        and self.bloco3.x + 50 < 476\
        and self.bloco4.x + 50 < 476\
        and self.bool_colisão_direita() != True:

            self.bloco1.x += 25
            self.bloco2.x += 25
            self.bloco3.x += 25
            self.bloco4.x += 25

    def bool_colisão_esquerda(self):
        for c in range(0, len(self.conjunto_de_blocos)):

            if self.bloco1.y == self.conjunto_de_blocos[c].y\
            and self.bloco1.x - 25 == self.conjunto_de_blocos[c].x:
                return True

            elif self.bloco2.y == self.conjunto_de_blocos[c].y\
            and self.bloco2.x - 25 == self.conjunto_de_blocos[c].x:
                return True

            elif self.bloco3.y == self.conjunto_de_blocos[c].y\
            and self.bloco3.x - 25 == self.conjunto_de_blocos[c].x:
                return True

            elif self.bloco4.y == self.conjunto_de_blocos[c].y\
            and self.bloco4.x - 25 == self.conjunto_de_blocos[c].x:
                return True

    def mover_esquerda(self):

        if self.conexão_com_player == True\
        and self.bloco1.x - 25 > 1\
        and self.bloco2.x - 25 > 1\
        and self.bloco3.x - 25 > 1\
        and self.bloco4.x - 25 > 1\
        and self.bool_colisão_esquerda() != True:
        
            self.bloco1.x -= 25
            self.bloco2.x -= 25
            self.bloco3.x -= 25
            self.bloco4.x -= 25

    def bool_colisão_y(self):
        for c in range(0, len(self.conjunto_de_blocos)):

            if self.bloco1.y + 25 == self.conjunto_de_blocos[c].y\
            and self.bloco1.x == self.conjunto_de_blocos[c].x:
                return True

            elif self.bloco2.y + 25 == self.conjunto_de_blocos[c].y\
            and self.bloco2.x == self.conjunto_de_blocos[c].x:
                return True

            elif self.bloco3.y + 25 == self.conjunto_de_blocos[c].y\
            and self.bloco3.x == self.conjunto_de_blocos[c].x:
                return True

            elif self.bloco4.y + 25 == self.conjunto_de_blocos[c].y\
            and self.bloco4.x == self.conjunto_de_blocos[c].x:
                return True

    def mover_pbaixo(self):

        if self.conexão_com_player == True:

            if self.bloco1.y + 25 < 725\
            and self.bloco2.y + 25 < 725\
            and self.bloco3.y + 25 < 725\
            and self.bloco4.y + 25 < 725\
            and self.bool_colisão_y() != True:
            
                if self.velocidade >= 25:
                    self.bloco1.y += self.velocidade
                    self.bloco2.y += self.velocidade
                    self.bloco3.y += self.velocidade
                    self.bloco4.y += self.velocidade
                    self.velocidade = 0

                self.velocidade += 1
            
            elif self.velocidade >= 25:
                self.velocidade = 0
                self.colisão = True
            else:
                self.velocidade += 1 #ultimo movimento mesmo depois de colidir