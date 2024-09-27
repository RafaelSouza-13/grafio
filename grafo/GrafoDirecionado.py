from grafo.Grafo import Grafo
import networkx as nx
import matplotlib.pyplot as plt

class GrafoDirecionado(Grafo):

    def __init__(self, numero_vertices=0, conteudo=None):
        super().__init__(numero_vertices)
        self.conteudo = conteudo

    def cria_aresta(self, id_vertice, id_vizinho, peso=0):
        vertice = list(filter(lambda x: x.id == id_vertice, self.vertices))
        vizinho = list(filter(lambda x: x.id == id_vizinho, self.vertices))
        if vertice:
            vertice[0].adiciona_adjacente(vizinho[0], peso)
            self.matriz_adjacencia[id_vertice][id_vizinho] = 1
            self.adiciona_aresta(vertice[0], vizinho[0])
        else:
            pass
            #Disparar exceção

    def exibe_arestas(self):
        print("arestas: {", end="")
        for vertice in self.vertices:
            for adjacente in vertice.adjacentes:
                print(f"{vertice} -> {adjacente})", end=",")
        print("}")

    def exibe_grafo(self):
        G = nx.DiGraph()
        added_edges = set()

        for vertice in self.vertices:
            for adj in vertice.adjacentes:
                adj_id = adj.vertice.id
                edge = (vertice.id, adj_id)
                if edge not in added_edges and (adj_id, vertice.id) not in added_edges:
                    G.add_edge(*edge)
                    added_edges.add(edge)

            for vertice in self.vertices:
                if len(vertice.adjacentes) == 0:
                    G.add_node(vertice.id)

        pos = nx.spring_layout(G)
        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=15, font_weight='bold',
                arrows=True)
        plt.title("Grafo Orientado")
        plt.show()
