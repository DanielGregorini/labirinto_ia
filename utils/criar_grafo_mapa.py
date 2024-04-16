from config.imports import *

def print_matriz(matriz):
    for row in matriz:
        print(" ".join(str(node.name if node else "-") for node in row))

def print_node_and_neighbors(node):
    print(f"Nome do nó: {node.name}")
    print(f"  Propriedades do nó:")
    print(f"    Custo heurístico: {node.heuristic_cost}")
    print(f"    Tipo do terreno: {node.type_ground}")
    print(f"    Custo do terreno: {node.cost_ground}")
    print(f"    É agente: {node.is_agent}")
    print(f"    É ponto: {node.is_point}")
    print(f"    É secundario: {node.is_secondary}")
    print(f"  Vizinhos:")
    print(f"    Vizinho a Cima: {node.neighbor_top.name if node.neighbor_top else None}")
    print(f"    Vizinho e Baixo: {node.neighbor_down.name if node.neighbor_down else None}")
    print(f"    Vizinho à Esquerda: {node.neighbor_left.name if node.neighbor_left else None}")
    print(f"    Vizinho à Direita: {node.neighbor_right.name if node.neighbor_right else None}")
    print()

def criar_grafo_mapa(mapa, rows:int, columns:int):
    grafo = []  # Lista para armazenar os objetos Node correspondentes
    
    for name_node, props in mapa.items():
        # Extrai as propriedades do nó do JSON
        name = props["name"]
        heuristic_cost = props.get("heuristic_cost", 0)
        type_ground = props.get("type_ground", "")
        cost_ground = props.get("cost_ground", 0)
        is_agent = props.get("is_agent", False)
        is_point = props.get("is_point", False)
        is_secondary = props.get("is_secondary", False)
        column = props.get("column", 0)
        row = props.get("row", 0)
        
        # Cria um objeto Node com as propriedades extraídas
        node = Node(name, heuristic_cost, type_ground, cost_ground, is_agent, is_point, is_secondary, column, row)
        
        # Adiciona o nó à lista
        grafo.append(node)
    
    # Cria uma matriz para armazenar os nós
    matriz_grafo = [[None for _ in range(columns)] for _ in range(rows)]
    
    # Adiciona os nós à matriz com base em suas coordenadas
    for node in grafo:
        matriz_grafo[node.row - 1][node.column - 1] = node
        
    for node in grafo:
        column = node.column
        row = node.row
        
        # Adiciona vizinho ao Norte
        if row > 1:
            neighbor_top = next((n for n in grafo if n.column == column and n.row == row - 1), None)
            if neighbor_top:
                node.add_neighbor('top', neighbor_top)
        
        # Adiciona vizinho ao Sul
        if row < rows:
            neighbor_down = next((n for n in grafo if n.column == column and n.row == row + 1), None)
            if neighbor_down:
                node.add_neighbor('down', neighbor_down)
        
        # Adiciona vizinho à Esquerda
        if column > 1:
            neighbor_left = next((n for n in grafo if n.column == column - 1 and n.row == row), None)
            if neighbor_left:
                node.add_neighbor('left', neighbor_left)
        
        # Adiciona vizinho à Direita
        if column < columns:
            neighbor_right = next((n for n in grafo if n.column == column + 1 and n.row == row), None)
            if neighbor_right:
                node.add_neighbor('right', neighbor_right)   
       
    print_matriz(matriz_grafo)
    print()
    for node in grafo:
        print_node_and_neighbors(node)
    
    return matriz_grafo