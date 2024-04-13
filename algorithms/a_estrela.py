import heapq

def a_estrela(start, goal):
    # Fila de prioridade para os nós a serem explorados, iniciando com o nó inicial
    # Cada entrada na fila tem o formato: (f_score, nome do nó, node)
    priority_queue = [(start.heuristic_cost + start.actual_cost, start.name, start)]
    start.actual_cost = 0  # Custo do caminho real do início ao nó atual

    # Conjunto de nós visitados para evitar processamento repetido
    visited = set()

    while priority_queue:
        # Remove o nó com o menor f_score da fila
        _, _, current_node = heapq.heappop(priority_queue)

        #print("NODE ATUAL:", current_node.name)
        if current_node == goal:
            # Reconstrói o caminho do objetivo até o início seguindo os pais
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = current_node.parent
            return path[::-1]

        if current_node not in visited:
            visited.add(current_node)

            # Explora os vizinhos do nó atual
            for neighbor in current_node.get_neighbors_profundidade():
                if neighbor not in visited:
                    # Calcula o custo atual do caminho passando pelo nó atual até o vizinho
                    tentative_g_score = current_node.actual_cost + neighbor.cost_ground
                    
                    # Se o caminho é melhor, atualiza
                    if tentative_g_score < neighbor.actual_cost:
                        neighbor.parent = current_node
                        neighbor.actual_cost = tentative_g_score
                        f_score = tentative_g_score + neighbor.heuristic_cost

                        #print("Vizinho:", neighbor.name, "com f_score:", f_score)
                        # Adiciona ou atualiza o vizinho na fila de prioridade
                        heapq.heappush(priority_queue, (f_score, neighbor.name, neighbor))
    return None
