from leitor import ler_matriz_arquivo
from aproximado import vizinho_mais_proximo
from exato import held_karp

caminho_arquivo = "arquivos/tsp1_253.txt"
matriz = ler_matriz_arquivo(caminho_arquivo)

rota_aprox, custo_aprox, tempo_aprox = vizinho_mais_proximo(matriz)
print("\n--- Algoritmo Aproximado (Vizinho Mais Próximo) ---")
print(caminho_arquivo)
print(f"Rota: {rota_aprox}")
print(f"Custo total: {custo_aprox}")
print(f"Tempo de execução: {tempo_aprox:.4f} segundos")

rota_exata, custo_exato, tempo_exato = held_karp(matriz)
print("\n--- Algoritmo Exato (Held-Karp) ---")
print(caminho_arquivo)
print(f"Rota: {rota_exata}")
print(f"Custo total: {custo_exato}")
print(f"Tempo de execução: {tempo_exato:.4f} segundos")