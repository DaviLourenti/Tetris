import pygame
import display
import random
import entidades_de_blocos
import tipos_de_formas


def main():
    cenario = display.Cenario(725)

    aglomeração = entidades_de_blocos.Aglomeração()
    formas = [
              tipos_de_formas.Forma_I, 
              tipos_de_formas.Forma_Q, 
              tipos_de_formas.Forma_S, 
              tipos_de_formas.Forma_T, 
              tipos_de_formas.Forma_Z, 
              tipos_de_formas.Forma_J, 
              tipos_de_formas.Forma_L
              ]
    f = formas[-2](aglomeração)
    #f.add_agromeração()
    
    tela = pygame.display.set_mode((display.TELA_LARGURA, display.TELA_ALTURA))
    relogio = pygame.time.Clock()

    tick_do_relogio = 30
    rodando = True

    while rodando:

        #restartando o player
        if f.colisão == True:
            aglomeração.aglomerar_forma(f)
            f = formas[random.randint(0, len(formas)-1)](aglomeração)
            
        #tempo de sincronização do jogo
        relogio.tick(tick_do_relogio)
        f.mover_pbaixo()

        # interação com o usuário
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
            
            else:
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
        
        if rodando == True:        
            aglomeração.conferir_e_lipar_linha()
            display.desenhar_tela(tela, f, cenario, aglomeração)



if __name__ == '__main__':
    print("(tetris) >> para jogar execute o arquivo index.exe ou index.py num compilador python")