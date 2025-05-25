def ler_matriz_arquivo(caminho_arquivo):
    with open(caminho_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()
    matriz = [list(map(int, linha.strip().split())) for linha in linhas]
    return matriz