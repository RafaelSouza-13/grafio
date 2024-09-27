import numpy as np

from grafo.Vertice import Vertice
import matplotlib.pyplot as plt
import networkx as nx

class Grafo:
    def __init__(self, numero_vertices=0):
        self.total_vertices = numero_vertices
        self.vertices = self.inicia_vertices(numero_vertices)
        self.matriz_adjacencia = self.inicializa_matrix_adjacencia(numero_vertices)


    def inicia_vertices(self, numero_vertices):
        vertices = []
        for i in range(numero_vertices):
            vertice = Vertice(i)
            vertices.append(vertice)
        return vertices

    def inicializa_matrix_adjacencia(self, numero_vertices):
        return np.zeros((numero_vertices, numero_vertices), dtype=np.int32)

    def exibe_vertices(self):
        print("vertices: {", end="")
        for vertice in self.vertices:
            print(vertice, end=",")
        print("}")

    def adiciona_vertice(self, vertice):
        self.vertices.append(vertice)

    def exibe_matriz(self):
        fig, ax = plt.subplots()
        cax = ax.imshow(self.matriz_adjacencia, cmap='Spectral', interpolation='nearest')

        fig.colorbar(cax)

        ax.set_title('Matriz de ajdacencias')
        ax.set_xlabel('adjacentes')
        ax.set_ylabel('vertices')

        for i in range(self.matriz_adjacencia.shape[0]):
            for j in range(self.matriz_adjacencia.shape[1]):
                ax.text(j, i, str(self.matriz_adjacencia[i, j]),
                        ha='center', va='center',
                        color='white')

        ax.set_xticks(np.arange(self.matriz_adjacencia.shape[1]))
        ax.set_yticks(np.arange(self.matriz_adjacencia.shape[0]))
        ax.set_xticklabels(np.arange(self.matriz_adjacencia.shape[1]))
        ax.set_yticklabels(np.arange(self.matriz_adjacencia.shape[0]))

        plt.show()

    def exibe_vertice_adjacentes(self, id_vertice):
        vertice = list(filter(lambda x: x.id == id_vertice, self.vertices))
        if vertice:
            vertice[0].exibe_adjacentes()

    def exibe_todos_vertices_adjacentes(self):
        for vertice in self.vertices:
            vertice.exibe_adjacentes()


    def __getitem__(self, index):
        return self.vertices[index]
