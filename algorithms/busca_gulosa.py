import heapq

def busca_gulosa(start, goal):
    # Cria uma fila de prioridade e adiciona o nó inicial com custo heurístico e nome como critério de desempate
    priority_queue = [(start.heuristic_cost, start.name, start)]
    visited = set()

    while priority_queue:
        # Obtém o nó com o menor custo heurístico
        current_cost, _, current_node = heapq.heappop(priority_queue)

        print("NODE ATUAL", current_node.name)
        if current_node == goal:
            # Se o nó atual é o objetivo, reconstruímos o caminho
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = current_node.parent
            return path[::-1]

        if current_node not in visited:
            visited.add(current_node)

            for neighbor in current_node.get_neighbors_profundidade():
                if neighbor not in visited:
                    print("Vizinho:", neighbor.name)
                    neighbor.parent = current_node
                    # Adiciona o vizinho na fila de prioridade com seu custo heurístico e nome como critério de desempate
                    heapq.heappush(priority_queue, (neighbor.heuristic_cost, neighbor.name, neighbor))
    return None
