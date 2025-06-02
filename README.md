Para executar as soluções e replicar os resultados, siga os passos abaixo:

### Estrutura dos Arquivos
O projeto está organizado com os seguintes arquivos:
* **main.py:** Script principal que executa os algoritmos.
* **exato.py:** Contém a implementação do algoritmo de Held-Karp.
* **aproximado.py:** Contém a implementação do algoritmo 2-aproximado.
* **leitor.py:** Função para ler as matrizes de adjacência dos arquivos de texto.
arquivos/: Diretório contendo os arquivos de entrada do TSP (tsp1_253.txt, etc.).

### Passo a Passo para Execução
* **Pré-requisitos:** Certifique-se de ter o Python 3 instalado. Nenhuma biblioteca externa é necessária.
* **Configuração:** Coloque todos os arquivos (.py) no mesmo diretório. Crie uma subpasta chamada arquivos e insira os arquivos .txt nela.

### Execução
1. Abra o arquivo main.py em um editor de texto.
2. Na linha *caminho_arquivo = "arquivos/tsp2_1248.txt"*, altere o nome do arquivo para a instância que deseja executar.
3. Abra um terminal ou prompt de comando, navegue até o diretório do projeto e execute o script com o comando: Bash
python main.py
4. Saída: O programa imprimirá no console a rota, o custo total e o tempo de execução para os algoritmos aproximado e exato.
