from config.imports import *

def limpar_node_parente(mapa):
    for linha in mapa:
        for elemento in linha:
            elemento.parent = None