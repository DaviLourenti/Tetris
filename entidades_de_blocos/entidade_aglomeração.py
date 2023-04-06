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
                    

    def desenhar(self, tela):
        for c in range(0, len(self.conjunto_de_blocos)):
            self.conjunto_de_blocos[c].desenhar(tela)
