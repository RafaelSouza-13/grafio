from collections import deque

class BuscaEmLargura:
    def __init__(self, grafo, inicio):
        self.grafo = grafo
        self.tempo = 0
        self.visitado = set()
        self.tempo = 0
        self.resultados = []
        self.tempo_descoberta = {}
        self.ancestral = {}
        self.id_vertice = {}
        self.bfs(inicio)
        desconexos = self.checa_desconexos()
        while len(desconexos) != 0:
            self.tempo = 0
            self.bfs_visit(desconexos[0])
            desconexos = self.checa_desconexos()

    def bfs(self, inicio):
        # corrigir erro index out of range
        vertice = list(filter(lambda x: x.id == inicio, self.grafo.vertices))
        vertice = vertice[0]
        self.bfs_visit(vertice)

    def bfs_visit(self, vertice):
        fila = deque()
        fila.append(vertice)
        self.visitado.add(vertice)

        self.tempo_descoberta = {vertice: self.tempo}
        self.ancestral = {vertice: None}

        while fila:
            nivel_atual = len(fila)
            for _ in range(nivel_atual):
                vertice = fila.popleft()
                resultado = {
                    'vertice': vertice.id,
                    'tempo_descoberta': self.tempo_descoberta[vertice],
                    'ancestral': self.ancestral[vertice]
                }
                self.resultados.append(resultado)
                for adj in vertice.adjacentes:
                    if adj.vertice not in self.visitado:
                        self.visitado.add(adj.vertice)
                        fila.append(adj.vertice)
                        self.tempo_descoberta[adj.vertice] = self.tempo + 1
                        self.ancestral[adj.vertice] = vertice
            self.tempo += 1

    def checa_desconexos(self):
        desconexos = []
        for vertice in self.grafo.vertices:
            if vertice not in self.visitado:
                desconexos.append(vertice)
        return desconexos

    def mostrar_resultados(self):
        for resultado in self.resultados:
            print(
                f"Vértice: {resultado['vertice']}, Tempo de Descoberta: {resultado['tempo_descoberta']}, Ancestral: {resultado['ancestral']}")



