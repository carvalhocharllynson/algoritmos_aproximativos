from time import perf_counter
from itertools import combinations

def held_karp(matriz):
    inicio = perf_counter()
    n = len(matriz)
    memo = {}

    for k in range(1, n):
        memo[(1 << k, k)] = (matriz[0][k], [0, k])

    for tamanho in range(2, n):
        for subconjunto in combinations(range(1, n), tamanho):
            bits = sum(1 << k for k in subconjunto)
            for k in subconjunto:
                anterior_bits = bits & ~(1 << k)
                melhor_custo = float('inf')
                melhor_caminho = []
                for m in subconjunto:
                    if m == k:
                        continue
                    custo_anterior, caminho_anterior = memo[(anterior_bits, m)]
                    custo = custo_anterior + matriz[m][k]
                    if custo < melhor_custo:
                        melhor_custo = custo
                        melhor_caminho = caminho_anterior + [k]
                memo[(bits, k)] = (melhor_custo, melhor_caminho)

    bits_final = (1 << n) - 2
    melhor_custo = float('inf')
    melhor_rota = []

    for k in range(1, n):
        custo, caminho = memo[(bits_final, k)]
        custo += matriz[k][0]
        if custo < melhor_custo:
            melhor_custo = custo
            melhor_rota = caminho + [0]

    fim = perf_counter()
    return melhor_rota, melhor_custo, fim - inicio