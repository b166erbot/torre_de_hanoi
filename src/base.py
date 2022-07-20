from operator import index
from .pecas import Peca, SemPeca


class Base:
    def __init__(self):
        self.caracter = "▒"
        self.tamanho_peca = 13
        astes = [
            [SemPeca()] + [Peca(numero) for numero in range(3, 15, 2)],
            [SemPeca() for _ in range(7)],
            [SemPeca() for _ in range(7)],
        ]
        self.astes = {
            nome: aste
            for nome, aste in
            zip(['primeira', 'segunda', 'terceira'], astes)
        }
        self.movimentos = 0

    def desenhar(self):
        retorno = [
            "  ".join([peca.caracteres() for peca in linha])
            for linha in zip(*self.astes.values())
        ]
        return retorno

    def _pegar_primeira_peca(self, aste):
        pecas = list(filter(lambda peca: peca.peca, self.astes[aste]))
        if len(pecas) == 0:
            raise IndexError("A aste que você selecionou não tem peças")
        return pecas[0]

    def _pegar_primeiro_index(self, aste):
        pecas = list(filter(lambda peca: peca.peca, self.astes[aste]))
        if len(pecas) == 0:
            return 0
        else:
            return self.astes[aste].index(pecas[0])

    def mover(self, aste1, aste2):
        peca1 = self._pegar_primeira_peca(aste1)
        index_peca1 = self.astes[aste1].index(peca1)
        self.astes[aste1].pop(index_peca1)
        self.astes[aste1].insert(index_peca1, SemPeca())
        index_peca2 = self._pegar_primeiro_index(aste2) - 1
        # a peça que irá retirar não importa pois sempre será SemPeca
        self.astes[aste2].pop(index_peca2)
        if index_peca2 == -1:
            self.astes[aste2].append(peca1)
        else:
            self.astes[aste2].insert(index_peca2, peca1)
        self.movimentos += 1


