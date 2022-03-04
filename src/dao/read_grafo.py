from pathlib import Path

from estruturas.grafo import Grafo

def read_grafo(path: Path) -> Grafo:
    g = Grafo()
    with open(path) as f:
        lines = f.readlines()
        n_vertices = int(lines[0])
        print('numero d vertices: ', n_vertices)
        n_arestas = int(lines[n_vertices + 1])
        print('numero d arestas: ', n_arestas)
        for i in range(1, 1 + n_vertices):
            g.add_vertice(lines[i].replace('\n', ''))
        for i in range(1 + n_vertices + 1, 1 + n_vertices + 1 + n_arestas):
            v1, v2 = lines[i].replace('\n', '').split(' ')
            g.add_aresta(v1, v2)
        f.close()

    return g
