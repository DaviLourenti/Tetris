import pygame
import random
import classes
import classes.entidade_display as entidade_display
import tipos_de_formas


def main():
    cenario = entidade_display.Cenario(725)

    aglomeração = classes.Aglomeração()
    formas = [
              tipos_de_formas.Forma_I, 
              tipos_de_formas.Forma_Q, 
              tipos_de_formas.Forma_S, 
              tipos_de_formas.Forma_T, 
              tipos_de_formas.Forma_Z, 
              tipos_de_formas.Forma_J, 
              tipos_de_formas.Forma_L
              ]
    forma_aleatoria = random.randint(0, len(formas)-1)
    f = formas[forma_aleatoria](aglomeração)
    
    tela = pygame.display.set_mode((entidade_display.TELA_LARGURA, entidade_display.TELA_ALTURA))
    relogio = pygame.time.Clock()
    tick_do_relogio = 30
    
    rodando = True
    formas_que_ja_foram = []
    
    while rodando:
        
        #restartando o player
        if f.colisão == True:
            aglomeração.aglomerar_forma(f)
            
            forma_aleatoria = random.randint(0, len(formas)-1)
            f = formas[forma_aleatoria](aglomeração)
        
            formas_que_ja_foram.append(formas[forma_aleatoria])
            
            #garantindo que todas as peças aparecem em uma mesma janela de tempo
            for item in formas_que_ja_foram:
                if formas.count(item) == 1 and formas_que_ja_foram.count(item) == 2:
                    formas.pop(formas.index(item))
            
            if len(formas) == 0:
                formas = list(set(formas_que_ja_foram)) 
                formas_que_ja_foram = []
            
        #tempo de sincronização do jogo, velocidade de atuazação de framerate
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
            aglomeração.conferir_linha()
            entidade_display.desenhar_tela(tela, f, cenario, aglomeração)



if __name__ == '__main__':
    print("(tetris) >> para jogar execute o arquivo index.exe ou index.py num compilador python")