import pygame
import os
import random


TELA_LARGURA = 500
TELA_ALTURA = 800

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


class Forma:
    def __init__(self, Bloco, x1,y1, x2,y2, x3,y3, x4,y4, aglomeração):
        self.velocidade = 0
        self.giro = 0
        self.colisão = False
        self.conexão_com_player = True
        self.conjunto_de_blocos = aglomeração.conjunto_de_blocos
        
        self.bloco1 = Bloco(x1, y1)
        self.bloco2 = Bloco(x2, y2)
        self.bloco3 = Bloco(x3, y3)
        self.bloco4 = Bloco(x4, y4)

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

                
             
class Aglomeração:
    def __init__(self):
        
        self.conjunto_de_blocos = []
        self.index_ocupados = []
        
    def aglomerar_forma(self, forma):  
            self.conjunto_de_blocos += [forma.bloco1]
            self.conjunto_de_blocos += [forma.bloco2]
            self.conjunto_de_blocos += [forma.bloco3]
            self.conjunto_de_blocos += [forma.bloco4]

            forma.conexão_com_player = False
    
    def puxar_tudo_pra_baixo(self):
        for c in range(0, len(self.conjunto_de_blocos)):
            self.conjunto_de_blocos[c].y += 25

    def conferir_e_lipar_linha(self):
        self.y_ocupados = []

        for c in range(0, len(self.conjunto_de_blocos)):
            self.y_ocupados += [self.conjunto_de_blocos[c].y]
        
        self.y_ocupados = list(set(self.y_ocupados))
        for c in range(0, len(self.y_ocupados)):
            self.x_ocupados = []
            self.index_ocupados = []
            
            for c2 in range(0, len(self.conjunto_de_blocos)):

                if self.conjunto_de_blocos[c2].y == self.y_ocupados[c]\
                    and self.conjunto_de_blocos[c2].x not in self.x_ocupados:
                    self.x_ocupados += [self.conjunto_de_blocos[c2].x]
                    self.index_ocupados += [c2]
                
                    if len(self.x_ocupados) == 18:
                        self.index_ocupados.sort()
                        self.index_ocupados.reverse()

                        for a in range(0, len(self.x_ocupados)):
                            self.conjunto_de_blocos.pop(self.index_ocupados[a])
                        
                        self.puxar_tudo_pra_baixo()
                        self.x_ocupados = []
                        self.index_ocupados = []
                        break
     
        
        # if len(self.y_ocupados) >= 3:
        #     for a in range(0, len(self.conjunto_de_blocos)):
        #         self.conjunto_de_blocos.pop(0)
        #         self.y_ocupados = []

          
        
    def desenhar(self, tela): 
        for c in range(0, len(self.conjunto_de_blocos)):     
                self.conjunto_de_blocos[c].desenhar(tela)
        


