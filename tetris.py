import pygame
import os
import random
import forma
import f_tipo

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
IMAGEM_FUNDO = pygame.image.load(os.path.join('imagens', 'fundo.png'))
IMAGEM_CENARIO = pygame.image.load(os.path.join('imagens', 'cenario.png'))


# class Cano:
#     DISTANCIA = 200
#     VELOCIDADE = 5

#     def __init__(self, x):
#         self.x = x
#         self.altura = 0
#         self.pos_topo = 0
#         self.pos_base = 0
#         self.CANO_TOPO = pygame.transform.flip(IMAGEM_CANO, False, True)
#         self.CANO_BASE = IMAGEM_CANO
#         self.passou = False
#         self.definir_altura()

class Cenario:
    LARGURA = IMAGEM_CENARIO.get_width()
    ALTURA = IMAGEM_CENARIO.get_height()
    IMAGEM = IMAGEM_CENARIO
    IMG_ROTACIONADA = pygame.transform.rotate(IMAGEM, 90)

    def __init__(self, y):
        self.y = y

    def desenhar(self, tela):
        tela.blit(self.IMAGEM, (0.9, self.y))#chão
        tela.blit(self.IMG_ROTACIONADA, (2, 3))#parede esquerda
        tela.blit(self.IMG_ROTACIONADA, (476, 3))#parede direita


def desenhar_tela(tela, Forma, cenario, aglomeração):
    tela.blit(IMAGEM_FUNDO, (0, 0))
    Forma.bloco1.desenhar(tela)
    Forma.bloco2.desenhar(tela)
    Forma.bloco3.desenhar(tela)
    Forma.bloco4.desenhar(tela)

    aglomeração.desenhar(tela)
    cenario.desenhar(tela)
    pygame.display.update()


def main():
    cenario = Cenario(725)

    aglomeração = forma.Aglomeração()
    formas = [f_tipo.Forma_i, f_tipo.Forma_q, f_tipo.Forma_s, f_tipo.Forma_t, f_tipo.Forma_z]
    f = formas[0](forma.Bloco, aglomeração)
    
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    relogio = pygame.time.Clock()

    tick_do_relogio = 30
    rodando = True

    while rodando:

        #restartando o player
        if f.colisão == True:
            aglomeração.aglomerar_forma(f)
            f = formas[random.randint(0, 4)](forma.Bloco, aglomeração)#
            
        #tempo de sincronização do jogo
        relogio.tick(tick_do_relogio)
        f.mover_pbaixo()

        # interação com o usuário
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_SPACE:
                    f.bloco1.baladinha_bloco()
                    f.bloco2.baladinha_bloco()
                    f.bloco3.baladinha_bloco()
                    f.bloco4.baladinha_bloco()
                
                if evento.key == pygame.K_RIGHT:
                    f.mover_direita()
                
                if evento.key == pygame.K_LEFT:
                    f.mover_esquerda()
                
                if evento.key == pygame.K_UP:
                    f.girar()

            #acelerar a decida
            tecla = pygame.key.get_pressed()
            if tecla[pygame.K_DOWN]:
                tick_do_relogio = 300
            else:
                tick_do_relogio = 30
                
        aglomeração.conferir_e_lipar_linha()
        desenhar_tela(tela, f, cenario, aglomeração)



if __name__ == '__main__':
    main()