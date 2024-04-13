import json

from classes.node import Node

from utils.printar_mapa import Printar_mapa
from utils.criar_grafo_mapa import Criar_grafo_mapa
from utils.encontrar_inicio import Encontrar_node_inicial
from utils.encontrar_inicio  import Encontrar_node_objetivo

from algorithms.busca_profundidade import busca_em_profundidade
from algorithms.busca_largura import busca_em_largura
from algorithms.busca_gulosa import busca_gulosa
from algorithms.a_estrela import a_estrela


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
with open('maps/mapa3.json') as arquivo:
    dados = json.load(arquivo)

##print(dados)

mapa = Criar_grafo_mapa(dados, 8, 9)
Printar_mapa(mapa)

caminho_profunidade = busca_em_profundidade(Encontrar_node_inicial(mapa), Encontrar_node_objetivo(mapa))
caminho_largura = busca_em_largura(mapa, Encontrar_node_inicial(mapa), Encontrar_node_objetivo(mapa))
caminho_gulosa = busca_gulosa(Encontrar_node_inicial(mapa), Encontrar_node_objetivo(mapa))
caminho_estrela = a_estrela(Encontrar_node_inicial(mapa), Encontrar_node_objetivo(mapa))

print()
print("caminho_profunidade")
if caminho_profunidade:
    for node in caminho_profunidade:
        print(node.name)
else:
    print("Nenhum caminho encontrado")
    
print()
print("caminho_largura")
if caminho_largura:
    for node in caminho_largura:
        print(node.name)
else:
    print("Nenhum caminho encontrado")

print()
print("caminho_gulosa")
if caminho_gulosa:
    for node in caminho_gulosa:
        print(node.name)
else:
    print("Nenhum caminho encontrado")

print()
print("Caminho estrela")
if caminho_estrela:
    for node in caminho_estrela:
        print(node.name)
else:
    print("Nenhum caminho encontrado")

