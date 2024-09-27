from grafo.Grafo import Grafo
import networkx as nx
import matplotlib.pyplot as plt

class GrafoNaoDirecionado(Grafo):

    def __init__(self, numero_vertices=0, conteudo=None):
        super().__init__(numero_vertices)
        self.conteudo = conteudo

    def cria_aresta(self, id_vertice, id_vizinho, peso=0):
        vertice = list(filter(lambda x: x.id == id_vertice, self.vertices))
        vizinho = list(filter(lambda x: x.id == id_vizinho, self.vertices))

        if vertice and vizinho and vertice != vizinho:
            vertice[0].adiciona_adjacente(vizinho[0], peso)
            vizinho[0].adiciona_adjacente(vertice[0], peso)
            self.matriz_adjacencia[id_vertice][id_vizinho] = 1
            self.matriz_adjacencia[id_vizinho][id_vertice] = 1
        elif vertice and vizinho and vertice == vizinho:
            vertice[0].adiciona_adjacente(vizinho[0], peso)
            self.matriz_adjacencia[id_vertice][id_vizinho] = 1
        else:
            pass
            #Disparar exceção

    def exibe_arestas(self):
        vertice_arestas_imprimidas = []
        print("arestas: {", end="")
        for vertice in self.vertices:
            for adjacente in vertice.adjacentes:
                if adjacente.vertice not in vertice_arestas_imprimidas:
                    print(f"({vertice} <-> {adjacente})", end=",")
            vertice_arestas_imprimidas.append(vertice)
        print("}")

    def exibe_grafo(self):
        G = nx.Graph()
        added_edges = set()

        for vertice in self.vertices:
            for adj in vertice.adjacentes:
                adj_id = adj.vertice.id
                if (vertice.id, adj_id) not in added_edges and (adj_id, vertice.id) not in added_edges:
                    G.add_edge(vertice.id, adj_id)
                    added_edges.add((vertice.id, adj_id))
        for vertice in self.vertices:
            if len(vertice.adjacentes) == 0:
                G.add_node(vertice)
        G_simples = nx.Graph(G)

        pos = nx.spring_layout(G_simples)
        nx.draw(G_simples, pos, with_labels=True, node_color="lightblue", node_size=1000, font_size=10,
                font_color="black")
        plt.show()
