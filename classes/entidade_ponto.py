class Ponto:
    def __init__(self, pontos = 0):
        self.pontos = pontos
    
    def add_pontos(self, quantidade_pontos):
        self.pontos += quantidade_pontos
    
    def sub_pontos(self, quantidade_pontos):
        self.pontos -= quantidade_pontos
    
class Afeta:
    def __init__(self, aaa) -> None:
        self.aaa = aaa
 
    def aumentar(self, opa):
        opa.add_pontos(self.aaa)
        
def teste():
    p1 = Ponto(10)
    p2 = Ponto(10)

    a = Afeta(25)
    a.aumentar(p2)

    print(p1.pontos)
    print(p2.pontos)
    
