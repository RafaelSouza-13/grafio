from grafo.GrafoDirecionado import GrafoDirecionado
from grafo.GrafoNaoDirecionado import GrafoNaoDirecionado
from algoritmos_busca.BuscaEmLargura import BuscaEmLargura
from algoritmos_busca.BuscaEmProfundidade import BuscaEmProfundidade
from utils.GrafoUtils import GrafoUtils

# Grafo conexo não orientado
x = 9
grafo = GrafoNaoDirecionado(x)
grafo.cria_aresta(0, 1)
grafo.cria_aresta(0, 2)
grafo.cria_aresta(1, 3)
grafo.cria_aresta(2, 3)
grafo.cria_aresta(2, 4)
grafo.cria_aresta(2, 5)
grafo.cria_aresta(3, 6)
grafo.cria_aresta(0, 7)
grafo.cria_aresta(6, 8)


#Grafo desconexo não orientado
# x = 11
# grafo = GrafoNaoDirecionado(x)
# grafo.cria_aresta(0, 1)
# grafo.cria_aresta(0, 2)
# grafo.cria_aresta(1, 3)
# grafo.cria_aresta(2, 3)
# grafo.cria_aresta(2, 4)
# grafo.cria_aresta(2, 5)
# grafo.cria_aresta(3, 6)
# grafo.cria_aresta(7, 8)
# grafo.cria_aresta(7, 9)


g1 = GrafoNaoDirecionado(4)
g1.cria_aresta(0, 1)
g1.cria_aresta(0, 2)
g1.cria_aresta(1, 3)
g1.cria_aresta(2, 3)

g2 = GrafoNaoDirecionado(2)
g2.cria_aresta(0, 1)

g3 = GrafoUtils.produto_carteziano(g1, g2)
g3.exibe_vertices()
g3.exibe_arestas()

print("///////////////")
# Grafo orientado
# x = 7
# grafo = GrafoDirecionado(x)
# grafo.cria_aresta(0, 1)
# grafo.cria_aresta(0, 3)
# grafo.cria_aresta(1, 2)
# grafo.cria_aresta(4, 5)
# grafo.cria_aresta(5, 4)
# grafo.cria_aresta(4, 6)
# grafo.cria_aresta(3, 4)

def string_para_inteiro(string):
    try:
        numero = int(string)
        return numero
    except ValueError:
        print()
        print("Entrada inválida...")
        return None

def menu():
    while True:
        print("------------------------------")
        print("Busca em profundidade - (dfs) - 1")
        print("Busca em largura - (bfs) - 2")
        print("Visualizar o grafo - 3")
        print("Visualizar o conjunto de vertices e arestas - 4")
        print("Visualizar os vertices e seus adjacentes - 5")
        print("Visualizar a matriz de adjacencias - 6")
        print("Sair - 0")
        valor = input("Escolha: ")
        print("------------------------------")
        if valor == '1':
            print(f"Escolha o id do vertice dentros os vertices")
            grafo.exibe_vertices()
            id_input = input("vertice escolhido: ")
            id = string_para_inteiro(id_input)
            if id is not None:
                print("Resultado busca em profundidade:")
                dfs = BuscaEmProfundidade(grafo, id)
                dfs.mostrar_resultados()
            print()
            input("Pressione Enter para continuar...")
        if valor == '2':
            print(f"Escolha o id do vertice dentros os vertices")
            grafo.exibe_vertices()
            id_input = input("vertice escolhido: ")
            id = string_para_inteiro(id_input)
            if id is not None:
                print("Resultado busca em largura:")
                bfs = BuscaEmLargura(grafo, id)
                bfs.mostrar_resultados()
            print()
            input("Pressione Enter para continuar...")
        elif valor == '3':
            grafo.exibe_grafo()
        elif valor == '4':
            grafo.exibe_vertices()
            grafo.exibe_arestas()
            print()
            input("Pressione Enter para continuar...")
        elif valor == '5':
            grafo.exibe_todos_vertices_adjacentes()
            print()
            input("Pressione Enter para continuar...")
        elif valor == '6':
            grafo.exibe_matriz()
        elif valor == '0':
            print("Finalizando o programa")
            break
        else:
            print("Opção inválida")

menu()






