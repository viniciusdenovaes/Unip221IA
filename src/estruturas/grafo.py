from typing import Dict, Set


class Grafo:
    def __init__(self):
        self.lista_adjacencia: Dict[str, Set[str]] = {}

    def add_vertice(self, vertice: str):
        self.lista_adjacencia[vertice] = set()

    def add_aresta(self, vertice1: str, vertice2: str):
        self.lista_adjacencia[vertice1].add(vertice2)
        self.lista_adjacencia[vertice2].add(vertice1)

    def __repr__(self):
        res = '\n'
        for field, value in self.__dict__.items():
            res += str(field) + ':\n\t' + str(value).replace('\n', '\n\t')
            res += '\n'
        res += '\n'
        return res

    def __str__(self):
        return self.__repr__()



