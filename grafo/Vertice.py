from grafo.Adjacente import Adjacente

class Vertice:
    def __init__(self, id):
        self.id = id
        self.adjacentes = []

    def adiciona_adjacente(self, vizinho, peso=0):
        adjacente = Adjacente(vizinho, peso)
        self.adjacentes.append(adjacente)

    def exibe_adjacentes(self):
        if len(self.adjacentes) == 0:
            print(f"adjacentes[{self.id}]:{{}}")
            return
        print(f"adjacentes[{self.id}]: {{", end="")
        for i, elemento in enumerate(self.adjacentes):
            if i == len(self.adjacentes) - 1:
                print(f"{elemento.vertice.id}}}")
            else:
                print(f"{elemento.vertice.id},", end=" ")

    def __eq__(self, other):
        return self.id == other.id

    def __getitem__(self, index):
        return self.adjacentes[index]

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self.id)

    def __hash__(self):
        return hash(self.id)