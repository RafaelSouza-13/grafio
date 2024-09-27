class Adjacente:
    def __init__(self, vertice, peso=0):
        self.vertice = vertice
        self.peso = peso

    def __eq__(self, other):
        return self.vertice == other

    def __str__(self):
        return str(self.vertice.id)

    def __repr__(self):
        return str(self.vertice.id)