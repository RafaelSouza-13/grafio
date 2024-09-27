from grafo.GrafoNaoDirecionado import GrafoNaoDirecionado
from grafo.Vertice import Vertice


class GrafoUtils:

    @staticmethod
    def produto_carteziano(grafo1, grafo2):
        produto = GrafoNaoDirecionado()
        vertice_map = {}
        for v in grafo1.vertices:
            for u in grafo2.vertices:
                vertice = Vertice((v, u))
                produto.adiciona_vertice(vertice)
                vertice_map[(v.id, u.id)] = vertice

        for v1 in grafo1.vertices:
            for v2 in grafo1.vertices:
                if GrafoUtils.existe_aresta(v1, v2):
                    for u in grafo2.vertices:
                        vertice1 = vertice_map[(v1.id, u.id)]
                        vertice2 = vertice_map[(v2.id, u.id)]
                        vertice1.adiciona_adjacente(vertice2)

        for u1 in grafo2.vertices:
            for u2 in grafo2.vertices:
                if GrafoUtils.existe_aresta(u1, u2):
                    for v in grafo1.vertices:
                        vertice1 = vertice_map[(v.id, u1.id)]
                        vertice2 = vertice_map[(v.id, u2.id)]
                        vertice1.adiciona_adjacente(vertice2)

        return produto

    @staticmethod
    def existe_aresta(vertice1, vertice2):
        return vertice2 in vertice1.adjacentes