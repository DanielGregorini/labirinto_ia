from config.imports import *

def encontrar_node_inicial(grafo):
    for linha in grafo:
        for node in linha:
            if node.is_agent:
                return node
    return None

def encontrar_node_objetivo(grafo):
    for linha in grafo:
        for node in linha:
            if node.is_point:
                return node
    return None

#retorna a lista de todos os objetivos
def encontrar_node_objetivo_lista(grafo):
    nodes = []
    for linha in grafo:
        for node in linha:
            if node.is_point:
                nodes.append(node) 
    return nodes

def encontrar_node_objetivo_secundario_lista(grafo):
    nodes = []
    for linha in grafo:
        for node in linha:
            if node.is_secondary:
                nodes.append(node) 
    return nodes