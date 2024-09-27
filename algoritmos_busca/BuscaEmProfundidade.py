class BuscaEmProfundidade:
    def __init__(self, grafo, inicio):
        self.grafo = grafo
        self.resultados = []
        self.tempo = 0
        self.tempo_descoberta = {}
        self.tempo_finalizacao = {}
        self.ancestral = {}
        self.visitado = set()
        self.dfs(inicio)
        desconexos = self.checa_desconexos()
        while len(desconexos) != 0:
            self.dfs_visit(desconexos[0])
            desconexos = self.checa_desconexos()



    def dfs(self, inicio):
        # corrigir erro index out of range
        vertice = list(filter(lambda x: x.id == inicio, self.grafo.vertices))
        vertice = vertice[0]
        self.dfs_visit(vertice)

    def dfs_visit(self, vertice):
        self.tempo += 1
        self.tempo_descoberta[vertice] = self.tempo
        self.visitado.add(vertice)
        resultado = {
            'vertice': vertice.id,
            'tempo_descoberta': self.tempo_descoberta[vertice],
            'tempo_finalizacao': None,
            'ancestral': self.ancestral.get(vertice, None)
        }
        self.resultados.append(resultado)

        for adjacente in vertice.adjacentes:
            if adjacente.vertice not in self.visitado:
                self.ancestral[adjacente.vertice] = vertice
                self.dfs_visit(adjacente.vertice)

        self.tempo += 1
        self.tempo_finalizacao[vertice] = self.tempo

        for resultado in self.resultados:
            if resultado['vertice'] == vertice.id:
                resultado['tempo_finalizacao'] = self.tempo_finalizacao[vertice]

    def checa_desconexos(self):
        desconexos = []
        for vertice in self.grafo.vertices:
            if vertice not in self.visitado:
                desconexos.append(vertice)
        return desconexos

    def mostrar_resultados(self):
        for resultado in self.resultados:
            print(
                f"Vértice: {resultado['vertice']}, Tempo de Descoberta: {resultado['tempo_descoberta']}, Tempo de Finalização: {resultado['tempo_finalizacao']}, Ancestral: {resultado['ancestral']}")
