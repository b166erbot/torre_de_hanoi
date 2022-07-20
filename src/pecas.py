class Peca:
    def __init__(self, comprimento: int):
        self.caracter = "█"
        self.comprimento = comprimento
        self.centralizar = 13
        self.peca = True
    
    def __repr__(self):
        return f"Peça: {self.caracter * self.comprimento}"
    
    def __str__(self):
        return self.caracteres()

    def caracteres(self):
        linha =  self.caracter * self.comprimento
        linha = linha.center(self.centralizar)
        return linha


class SemPeca:
    def __init__(self):
        self.caracter = "▒"
        self.centralizar = 13
        self.peca = False
    
    def __repr__(self):
        return f"Sem Peça: {self.caracter}"
    
    def __str__(self):
        return self.caracteres()

    def caracteres(self):
        linha = self.caracter.center(self.centralizar)
        return linha
