import math
from time import perf_counter

def encontrar_vertice_minimo(chave, na_mst, n_vertices):
    min_valor = math.inf
    min_indice = -1
    for v in range(n_vertices):
        if not na_mst[v] and chave[v] < min_valor:
            min_valor = chave[v]
            min_indice = v
    return min_indice

def arvoreGeradoraMinima_PRIM(matriz):
    n_vertices = len(matriz)
    pai = [-1] * n_vertices             #o valor pai[i] nos diz qual é o "pai" do vértice i na árvore
    chave = [math.inf] * n_vertices     #Valores chave para escolher a aresta de peso mínimo
    na_mst = [False] * n_vertices       #Conjunto para verificar os vértices já incluídos na MST

    chave[0] = 0    #começa pelo primeiro vértice (vértice 0)
    pai[0] = -1     #vértice raiz tem pai = -1

    for _ in range(n_vertices):
        u = encontrar_vertice_minimo(chave, na_mst, n_vertices)
        
        #Se não houver mais vértices alcançáveis, para
        if u == -1:
            break
        
        na_mst[u] = True
        for v in range(n_vertices):
            peso = matriz[u][v]
            if peso > 0 and not na_mst[v] and chave[v] > peso:
                chave[v] = peso
                pai[v] = u

    return pai

def caminho_preordem(pai, n_vertices):

    #Constrói uma lista de adjacências para a MST a partir do array 'pai'
    adj_mst = [[] for _ in range(n_vertices)]
    for i in range(1, n_vertices):
        p = pai[i]
        if p != -1:
            adj_mst[p].append(i)

    caminho = []
    visitado = [False] * n_vertices

    dfs_recursivo(0, adj_mst, visitado, caminho)    #Percorre (DFS recursivo) para obter o caminho

    return caminho

def dfs_recursivo(u, adj_mst, visitado, caminho):

    visitado[u] = True
    caminho.append(u)

    for v in adj_mst[u]:
        if not visitado[v]:
            dfs_recursivo(v, adj_mst, visitado, caminho)

def tsp_aproximado(matriz):
    inicio = perf_counter()
    n_vertices = len(matriz)

    array_pai = arvoreGeradoraMinima_PRIM(matriz)
    rota_aprox = caminho_preordem(array_pai, n_vertices)

    custo_total = 0
    for i in range(n_vertices - 1):
        vertice_atual = rota_aprox[i]
        proximo_vertice = rota_aprox[i+1]
        custo_total += matriz[vertice_atual][proximo_vertice]

    #Adiciona o custo de volta ao início para fechar o ciclo
    ultimo_vertice = rota_aprox[-1]
    primeiro_vertice = rota_aprox[0]
    custo_total += matriz[ultimo_vertice][primeiro_vertice]

    rota_aprox.append(primeiro_vertice)     #Adiciona o nó inicial ao final da rota

    fim = perf_counter()
    tempo_execucao = fim - inicio

    return rota_aprox, custo_total, tempo_execucao