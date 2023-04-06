import entidades_de_blocos

class Forma_S(entidades_de_blocos.Forma):
    def __init__(self, aglomeração):
        super().__init__(225, 250, 250, 250, 225, 275, 200, 275, aglomeração)

    def girar(self):
        if self.giro == 0:
            self.giro = 1

            self.bloco2.x -= 25
            self.bloco2.y -= 25
            self.bloco3.x += 25
            self.bloco3.y -= 25
            self.bloco4.x += 50

        elif self.giro == 1:
            self.giro = 0
            
            self.bloco2.x += 25
            self.bloco2.y += 25
            self.bloco3.x -= 25
            self.bloco3.y += 25
            self.bloco4.x -= 50