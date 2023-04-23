class Ponto:
    def __init__(self, pontos = 0):
        self.quantidade = pontos
    
    def add_pontos(self, valor):
        self.quantidade += valor
    
    def sub_pontos(self, valor):
        self.quantidade -= valor 