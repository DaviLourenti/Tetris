import entidades_de_blocos

class Forma_I(entidades_de_blocos.Forma):
    def __init__(self, Bloco, aglomeração):
        super().__init__(Bloco, 225, 250, 225, 275, 225, 300, 225, 325, aglomeração)
    
    def girar(self):
        if self.giro == 0:
            if self.bloco1.x + 50 <= 476\
            and self.bloco2.x + 50 <= 476\
            and self.bloco3.x + 50 <= 476\
            and self.bloco4.x + 50 <= 476\
            and self.bloco1.x - 50 >= 1\
            and self.bloco2.x - 50 >= 1\
            and self.bloco3.x - 50 >= 1\
            and self.bloco4.x - 50 >= 1:
                self.giro = 1

                self.bloco1.x -= 50
                self.bloco1.y += 50
                self.bloco2.x -= 25
                self.bloco2.y += 25
                self.bloco4.x += 25 
                self.bloco4.y -= 25

        elif self.giro == 1:
            if self.bloco1.y + 50 <= 725\
            and self.bloco2.y + 50 <= 725\
            and self.bloco3.y + 50 <= 725\
            and self.bloco4.y + 50 <= 725:
                self.giro = 0
                
                self.bloco1.x += 50
                self.bloco1.y -= 50
                self.bloco2.x += 25
                self.bloco2.y -= 25
                self.bloco4.x -= 25 
                self.bloco4.y += 25