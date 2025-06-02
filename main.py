import os

from leitor import ler_matriz_arquivo
from aproximado import tsp_aproximado
from exato import held_karp

caminho_arquivo = "arquivos/tsp2_1248.txt"
matriz = ler_matriz_arquivo(caminho_arquivo)

rota_aprox, custo_aprox, tempo_aprox = tsp_aproximado(matriz)
print("\n--- Algoritmo Aproximado (PRIM + DFS) ---")
print(f"Arquivo: {os.path.basename(caminho_arquivo)}")
print(f"Rota: {rota_aprox}")
print(f"Custo total: {custo_aprox}")
print(f"Tempo de execução: {tempo_aprox:.10f} segundos")

rota_exata, custo_exato, tempo_exato = held_karp(matriz)
print("\n--- Algoritmo Exato (Held-Karp) ---")
print(f"Arquivo: {os.path.basename(caminho_arquivo)}")
print(f"Rota: {rota_exata}")
print(f"Custo total: {custo_exato}")
print(f"Tempo de execução: {tempo_exato:.10f} segundos")
