from config.imports import *

def custo_caminho(caminho) -> float:
    custo: float = 0
   
    for i in range(len(caminho) - 1):
        custo += caminho[i].cost_ground
    return custo