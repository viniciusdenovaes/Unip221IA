from typing import List

from estruturas.grafo import Grafo


class Estado:
    def __init__(self, grafo: Grafo, caminho: List[str]):
        self.grafo = grafo
        self.caminho: List[str] = caminho

    def gerar_filhos(self) -> List['Estado']:
        filhos = []
        u: str = self.caminho[-1]
        for v in self.grafo.lista_adjacencia[u]:
            if not v in self.caminho:
                novo_caminho = self.caminho.copy()
                novo_caminho.append(v)
                filhos.append(Estado(self.grafo, novo_caminho))

        return filhos

    def verifica_objetivo(self):
        numero_vertice_grafo = len(self.grafo.lista_adjacencia.keys())
        return len(self.caminho) == numero_vertice_grafo

    def __repr__(self):
        return 'estado' + str(self.caminho)







