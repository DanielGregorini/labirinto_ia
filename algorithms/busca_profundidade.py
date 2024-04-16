from config.imports import *

def busca_em_profundidade(start: Node, goal, secondary):
    stack = [start]
    visited = set()

    while stack:
        current_node = stack.pop()
        #print("NODE ATUAL", current_node.name)
        if current_node in goal:
            # Se o nó atual é o objetivo, reconstruímos o caminho
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = current_node.parent
            return path[::-1]

        visited.add(current_node)

        for neighbor in current_node.get_neighbors_profundidade():
            #print(" vizinho: ",neighbor.name)
            if neighbor not in visited and neighbor not in stack:
                neighbor.parent = current_node
                stack.append(neighbor)
    return None