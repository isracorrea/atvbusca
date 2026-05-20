import networkx as nx
import matplotlib.pyplot as plt

# 1. Definição do Problema (Labirinto)
# 0 = Caminho livre, 1 = Parede
grid = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]

# 2. Modelagem do Grafo
G = nx.Graph()
linhas = len(grid)
colunas = len(grid[0])

# Adicionando os Nós (apenas caminhos livres)
for i in range(linhas):
    for j in range(colunas):
        if grid[i][j] == 0:
            G.add_node((i, j))

# Adicionando as Arestas (conectando vizinhos com peso 1)
direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Cima, Baixo, Esquerda, Direita

for (i, j) in G.nodes:
    for di, dj in direcoes:
        vizinho_i, vizinho_j = i + di, j + dj
        if (vizinho_i, vizinho_j) in G.nodes:
            # O NetworkX lida com grafos não-direcionados, então a ordem não importa
            G.add_edge((i, j), (vizinho_i, vizinho_j), weight=1)

# 3. Função Heurística (Distância de Manhattan)
def heuristica_manhattan(no_atual, no_destino):
    x1, y1 = no_atual
    x2, y2 = no_destino
    return abs(x1 - x2) + abs(y1 - y2)

# 4. Execução do A*
inicio = (0, 0)
destino = (4, 4)

try:
    # A chamada principal que resolve o problema
    caminho = nx.astar_path(G, inicio, destino, heuristic=heuristica_manhattan, weight='weight')
    print(f"Rota encontrada (Nós percorridos): {caminho}")
    print(f"Custo total: {len(caminho) - 1} passos")
except nx.NetworkXNoPath:
    print("Não há caminho possível até o destino!")

# 5. Visualização (Para demonstração no vídeo)
# Usamos a própria coordenada invertida para o gráfico ficar na orientação certa
posicoes = {(x, y): (y, -x) for x, y in G.nodes()} 

plt.figure(figsize=(6, 6))

# Desenha todos os caminhos possíveis em cinza claro
nx.draw(G, posicoes, node_color='lightgray', with_labels=True, node_size=600, font_size=8)

# Destaca o caminho encontrado pelo A* em verde
caminho_arestas = list(zip(caminho, caminho[1:]))
nx.draw_networkx_nodes(G, posicoes, nodelist=caminho, node_color='lightgreen', node_size=600)
nx.draw_networkx_edges(G, posicoes, edgelist=caminho_arestas, edge_color='green', width=3)

# Destaca a origem (azul) e destino (vermelho)
nx.draw_networkx_nodes(G, posicoes, nodelist=[inicio], node_color='blue', node_size=600)
nx.draw_networkx_nodes(G, posicoes, nodelist=[destino], node_color='red', node_size=600)

plt.title("Resolução do Labirinto com A*")
plt.show()