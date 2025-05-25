import time

def vizinho_mais_proximo(matriz):
    inicio = time.time()
    n = len(matriz)
    visitado = [False] * n
    rota = [0]
    custo_total = 0
    atual = 0
    visitado[0] = True

    for _ in range(n - 1):
        proximo = None
        menor_distancia = float('inf')
        for j in range(n):
            if not visitado[j] and matriz[atual][j] < menor_distancia:
                menor_distancia = matriz[atual][j]
                proximo = j
        rota.append(proximo)
        custo_total += menor_distancia
        visitado[proximo] = True
        atual = proximo

    custo_total += matriz[atual][0]
    rota.append(0)
    fim = time.time()
    return rota, custo_total, fim - inicio