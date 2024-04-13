def Encontrar_node_inicial(grafo):
    for linha in grafo:
        for node in linha:
            if node.is_agent:
                return node
    return None


def Encontrar_node_objetivo(grafo):
    for linha in grafo:
        for node in linha:
            if node.is_point:
                return node
    return None