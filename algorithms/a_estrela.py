from config.imports import *

def a_estrela(start: Node, goal):
    # Fila de prioridade para os nós a serem explorados, iniciando com o nó inicial
    # Cada entrada na fila tem o formato: (f_score, nome do nó, node)
    priority_queue = []
    heapq.heappush(priority_queue, (start.heuristic_cost + start.actual_cost, start.name, start))
    start.actual_cost = 0  # Custo do caminho real do início ao nó atual

    # Dicionário para armazenar o melhor custo até cada nó
    actual_costs = {start: start.actual_cost}

    # Conjunto de nós visitados para evitar processamento repetido
    visited = set()

    while priority_queue:
        # Remove o nó com o menor f_score da fila
        _, _, current_node = heapq.heappop(priority_queue)
        #print("NODE ATUAL:", current_node.name)

        # Verifica se alcançou o objetivo
        if current_node in goal:
            # Reconstrói o caminho do objetivo até o início seguindo os pais
            path = []
            while current_node:
                print(current_node.name)
                path.append(current_node)
                ##if(not current_node.is_point):
                current_node = current_node.parent
                #else:
                    #current_node = None
            return path[::-1]

        # Marca o nó como visitado após a verificação do objetivo para evitar prematuro fechamento
        visited.add(current_node)

        # Explora os vizinhos do nó atual
        for neighbor in current_node.get_neighbors_profundidade():
            if neighbor not in visited:
                # Calcula o custo atual do caminho passando pelo nó atual até o vizinho
                tentative_g_score = actual_costs[current_node] + neighbor.cost_ground

                # Se o caminho é melhor, atualiza
                if tentative_g_score < actual_costs.get(neighbor, float('inf')):
                    neighbor.parent = current_node
                    neighbor.actual_cost = tentative_g_score
                    actual_costs[neighbor] = tentative_g_score
                    f_score = tentative_g_score + neighbor.heuristic_cost
                    heapq.heappush(priority_queue, (f_score, neighbor.name, neighbor))

    return None
