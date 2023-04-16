import classes

class Forma_L(classes.Forma):
    def __init__(self, aglomeração):
        super().__init__(200, 250, 200, 275, 200, 300, 225, 300, aglomeração)

    def girar(self):

        if self.giro == 0:
            self.giro = 1

            self.bloco1.x += 25
            self.bloco1.y += 25
            self.bloco3.x -= 25
            self.bloco3.y -= 25
            self.bloco4.x -= 50

        elif self.giro == 1:
            self.giro = 2

            self.bloco1.x -= 25
            self.bloco1.y += 25
            self.bloco3.y -= 25
            self.bloco3.x += 25
            self.bloco4.y -= 50

        elif self.giro == 2:
            self.giro = 3

            self.bloco1.x -= 25
            self.bloco1.y -= 25
            self.bloco3.x += 25
            self.bloco3.y += 25
            self.bloco4.x += 50

        elif self.giro == 3:
            self.giro = 0

            self.bloco1.x += 25
            self.bloco1.y -= 25
            self.bloco3.x -= 25
            self.bloco3.y += 25
            self.bloco4.y += 50
