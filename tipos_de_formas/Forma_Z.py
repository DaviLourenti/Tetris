import entidades_de_blocos


class Forma_Z(entidades_de_blocos.Forma):
    def __init__(self, Bloco, aglomeração):
        super().__init__(Bloco, 200, 250, 225, 250, 225, 275, 250, 275, aglomeração)

    def girar(self):
        if self.giro == 0:
            self.giro = 1

            self.bloco1.x += 25
            self.bloco1.y += 25
            self.bloco3.x -= 25
            self.bloco3.y += 25
            self.bloco4.x -= 50

        elif self.giro == 1:
            self.giro = 0

            self.bloco1.x -= 25
            self.bloco1.y -= 25
            self.bloco3.x += 25
            self.bloco3.y -= 25
            self.bloco4.x += 50
