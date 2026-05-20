# Resolução de Labirinto usando Busca A* (A-Star)

Este projeto é a entrega da atividade de Inteligência Artificial (2026.1 - T01). O objetivo é modelar um problema de busca em formato de grafo e resolvê-lo utilizando o algoritmo A* através da biblioteca `networkx` em Python.

## 1. Descrição do Problema
O problema escolhido foi a resolução de um labirinto (grid 2D). O cenário é representado por uma matriz onde `0` indica um caminho livre e `1` indica uma parede (obstáculo). 

O agente precisa encontrar a rota mais curta do ponto inicial `(0, 0)` até o ponto de destino `(4, 4)`.
* **Nós do Grafo:** Cada célula livre da matriz.
* **Arestas:** Movimentos possíveis (cima, baixo, esquerda, direita) com custo igual a 1.
* **Heurística:** Foi utilizada a **Distância de Manhattan**, pois o movimento diagonal não é permitido.

## 2. Como rodar o projeto passo a passo

**Pré-requisitos:**
Certifique-se de ter o Python instalado na sua máquina. Você precisará instalar as bibliotecas `networkx` para a estrutura de grafos e `matplotlib` para a visualização.

No terminal, execute o comando:
pip install networkx matplotlib

**Execução:**
Faça o clone deste repositório e, dentro da pasta do projeto, rode o script principal:
python labirinto_astar.py

O terminal exibirá a lista de nós percorridos e o custo total. Em seguida, uma janela gráfica se abrirá mostrando a representação visual do labirinto, com o caminho ideal destacado em verde.

## 3. Apresentação (Vídeo)
A explicação completa da modelagem, implementação do código, execução e discussão sobre as limitações do modelo estão disponíveis no vídeo abaixo:

* **Link do YouTube:** [COLE O LINK DO SEU VÍDEO AQUI]