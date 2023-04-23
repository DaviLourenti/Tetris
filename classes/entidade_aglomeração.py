class Aglomeração:
    def __init__(self):

        self.conjunto_de_blocos = []
        self.indices_da_linha = []


    def aglomerar_forma(self, forma):
        self.conjunto_de_blocos += [forma.bloco1]
        self.conjunto_de_blocos += [forma.bloco2]
        self.conjunto_de_blocos += [forma.bloco3]
        self.conjunto_de_blocos += [forma.bloco4]

        forma.conexão_com_player = False


    def __puxar_tudo_pra_baixo(self):
        for c in range(len(self.conjunto_de_blocos)):
            #if self.conjunto_de_blocos[c].y < y_linha_excluida:
            self.conjunto_de_blocos[c].y += 25


    def __apagar_linha(self):
        self.indices_da_linha.sort()
        self.indices_da_linha.reverse()
        
        for i in range(len(self.x_preenchidos)):
            self.conjunto_de_blocos.pop(self.indices_da_linha[i])
        
        self.x_preenchidos = []
        self.indices_da_linha = []


    def conferir_linha(self, classe_pontos):
        self.y_preenchidos = list(set([item.y for item in self.conjunto_de_blocos]))
        
        for c in range(len(self.y_preenchidos)): #verifivação de linha em linha 
            
            self.x_preenchidos = []
            self.indices_da_linha = []

            for c2 in range(len(self.conjunto_de_blocos)): #procurando uma sequencia de 18 blocos seguidos na mesma linha
                
                if self.conjunto_de_blocos[c2].y == self.y_preenchidos[c] and self.conjunto_de_blocos[c2].x not in self.x_preenchidos:

                    self.x_preenchidos.append(self.conjunto_de_blocos[c2].x)
                    self.indices_da_linha.append(c2)

                    if len(self.x_preenchidos) == 18:

                        self.__apagar_linha()
                        self.__puxar_tudo_pra_baixo()
                        classe_pontos.add_pontos(100)
                        return True
                    

    def desenhar(self, tela):
        for c in range(0, len(self.conjunto_de_blocos)):
            self.conjunto_de_blocos[c].desenhar(tela)
