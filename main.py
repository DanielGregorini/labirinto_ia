import json

from classes.node import Node

from utils.printar_mapa import Printar_mapa
from utils.criar_grafo_mapa import Criar_grafo_mapa

'''while True:
    print("Selecione o mapa 1 ou 2: ")
    mapa_escolha = input()

    # Valida a escolha do mapa
    if mapa_escolha == '1' or mapa_escolha == '2':
        break  # Sai do loop se a escolha for válida
    else:
        print("Escolha inválida. Por favor, selecione o mapa 1 ou 2.")

while True:
    print("\nSelecione o método de ordenação:")
    print("1- Busca em largura")
    print("2- Busca em profundidade")
    print("3- Busca gulosa")
    print("4- Busca A*")
    algoritmo_escolha = input()

    # Valida a escolha do algoritmo
    if algoritmo_escolha in ['1', '2', '3', '4']:
        break  # Sai do loop se a escolha for válida
    else:
        print("Escolha inválida. Por favor, selecione uma das opções de algoritmo disponíveis.")'''

# Carrega o arquivo JSON do diretório atual

with open('maps/mapa1.json') as arquivo:
    dados = json.load(arquivo)

##print(dados)

mapa = Criar_grafo_mapa(dados, 4, 2)
Printar_mapa(mapa)