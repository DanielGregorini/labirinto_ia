from config.imports import *

def carregar_mapa(mapa_escolha):
    arquivo_mapa = {
        '1': ('maps/mapa1.json', 4, 2),
        '2': ('maps/mapa2.json', 5, 5),
        '3': ('maps/mapa3.json', 9, 8),
        '4': ('maps/mapa4.json', 10, 12)
    }

    if mapa_escolha in arquivo_mapa:
        arquivo, largura, altura = arquivo_mapa[mapa_escolha]
        with open(arquivo) as arquivo:
            dados = json.load(arquivo)
        return criar_grafo_mapa(dados, largura, altura)
    
    return None