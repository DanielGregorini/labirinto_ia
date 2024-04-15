from config.imports import *

def busca_em_largura(start:Node, goal):
    fila = deque([(start, [])])  # Inicializa a fila com o nó inicial e o caminho percorrido até ele
    visitados = set()

    while fila:
        current_node, path = fila.popleft()
        #print(current_node.name)
        if current_node in goal:
            # Se o nó atual é o objetivo, retorna o caminho até ele
            return path + [current_node]

        visitados.add(current_node)

        # Obtém todos os vizinhos possíveis do nó atual
        neighbors = current_node.get_neighbors_largura()
        
        #print("Atual", current_node.name)
        # Adiciona os vizinhos não visitados à fila com o caminho atualizado
        for neighbor in neighbors:
            #print(neighbor.name)
            if neighbor not in visitados:
                fila.append((neighbor, path + [current_node]))  # Não inclui o nó atual no caminho ao adicionar um vizinho

    # Se nenhum caminho for encontrado, retorna None
    return None