import pygame
import random
import classes
import classes.entidade_display as entidade_display
import tipos_de_formas

class classe_principal:
    def __init__(self) -> None:
        self.pontos = classes.Ponto()
    
        self.aglomeração_de_formas = classes.Aglomeração()
        self.formas=[
                tipos_de_formas.Forma_I, tipos_de_formas.Forma_Q, tipos_de_formas.Forma_S, tipos_de_formas.Forma_T, 
                tipos_de_formas.Forma_Z, tipos_de_formas.Forma_J, tipos_de_formas.Forma_L
                ]
        self.proximas_formas = [random.randint(0, len(self.formas)-1) for f in range(0, 3)]
        self.f_player = self.formas[self.proximas_formas[0]](self.aglomeração_de_formas)
        
        self.cenario = entidade_display.Cenario(725)
        self.tela = pygame.display.set_mode((entidade_display.TELA_LARGURA, entidade_display.TELA_ALTURA))
        self.taxa_velocidade_de_atualização_do_jogo = pygame.time.Clock()
        
        self.velocidade_do_jogo = 30
        self.taxa_de_aceleração_do_jogo = 0
        
        self.rodando = True
        self.formas_que_ja_foram = []
        self.taxa_de_repetição_por_peça = 1


    def restartando_o_player(self):
        if self.f_player.colisão == True:
            self.aglomeração_de_formas.aglomerar_forma(self.f_player)
            
            self.proximas_formas.pop(0)
            self.forma_aleatoria = random.randint(0, len(self.formas)-1)
            self.proximas_formas += [self.forma_aleatoria]
            
            self.f_player = self.formas[self.proximas_formas[0]](self.aglomeração_de_formas)
        
            self.formas_que_ja_foram.append(self.formas[self.forma_aleatoria])
            #garantindo que todas as peças aparecem em uma mesma janela de tempo
            def taxa_de_repetição_de_peças(taxa_por_ciclo):
                for item in self.formas_que_ja_foram:
                    if self.formas.count(item) == 1 and self.formas_que_ja_foram.count(item) == taxa_por_ciclo:
                        self.formas.pop(self.formas.index(item))
                        
            taxa_de_repetição_de_peças(self.taxa_de_repetição_por_peça)
            
            if len(self.formas) == 0:
                self.formas = list(set(self.formas_que_ja_foram))
                self.formas_que_ja_foram = []


    def config_de_queda(self): #tempo de sincronização do jogo, velocidade de atuazação de framerate
        self.taxa_velocidade_de_atualização_do_jogo.tick(self.velocidade_do_jogo)
        self.f_player.mover_pbaixo(self.pontos)
        
        #aceleração aumenta com os pontos
        if self.pontos.quantidade % 50 == 0 and self.pontos.quantidade < 200:
            self.taxa_de_aceleração_do_jogo += 25
            self.pontos.quantidade += 1
            
        elif self.pontos.quantidade % 50 == 0:
            self.taxa_de_aceleração_do_jogo += 5
            self.pontos.quantidade += 1


    def interação_com_o_usuário(self):
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                self.rodando = False
                pygame.quit()
            
            else:
                if evento.type == pygame.KEYDOWN:

                    if evento.key == pygame.K_SPACE:
                        self.f_player.bloco1.baladinha_bloco()
                        self.f_player.bloco2.baladinha_bloco()
                        self.f_player.bloco3.baladinha_bloco()
                        self.f_player.bloco4.baladinha_bloco()
                    
                    if evento.key == pygame.K_RIGHT:
                        self.f_player.mover_direita()
                    
                    if evento.key == pygame.K_LEFT:
                        self.f_player.mover_esquerda()
                    
                    if evento.key == pygame.K_UP:
                        self.f_player.girar()

                #acelerar a decida
                self.tecla = pygame.key.get_pressed()
                
                if self.tecla[pygame.K_DOWN]:
                    self.velocidade_do_jogo = 500 + self.taxa_de_aceleração_do_jogo
                else:
                    self.velocidade_do_jogo = 30 + self.taxa_de_aceleração_do_jogo
    
    
    def atualizar_tela(self): 
        if self.rodando == True:
            
            if self.aglomeração_de_formas.conferir_linha(self.pontos) == True:
                self.taxa_de_aceleração_do_jogo += 25*4
            
            self.nomes_todas_as_peças = [
                "Forma_I", "Forma_Q", "Forma_S", "Forma_T",
                "Forma_Z", "Forma_J", "Forma_L"
            ]
            
            self.nomes_proximas_peças = []
            for i in self.proximas_formas:
                self.nomes_proximas_peças += [self.nomes_todas_as_peças[i]]
              
                
            entidade_display.desenhar_tela(self.tela, self.f_player, self.cenario, self.aglomeração_de_formas, self.pontos.quantidade, self.nomes_proximas_peças)


    def main(self):
        while self.rodando:
            self.restartando_o_player()
            self.config_de_queda()
            self.interação_com_o_usuário()
            self.atualizar_tela()




func_principal = classe_principal()
func_principal.main()

if __name__ == '__main__':
    print("(tetris) >> para jogar execute o arquivo index.exe ou index.py num interpretador python")