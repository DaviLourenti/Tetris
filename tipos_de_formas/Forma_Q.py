import entidades_de_blocos

class Forma_Q(entidades_de_blocos.Forma):
    def __init__(self, Bloco, aglomeração):
        super().__init__(Bloco, 200, 250, 225, 250, 200, 275, 225, 275, aglomeração)

    def girar(self):
        pass