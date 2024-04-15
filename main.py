from config.imports import *

def carregar_mapa(mapa_escolha):
    arquivo_mapa = {
        '1': ('maps/mapa1.json', 4, 2),
        '2': ('maps/mapa2.json', 5, 5),
        '3': ('maps/mapa3.json', 9, 8)
    }

    if mapa_escolha in arquivo_mapa:
        arquivo, largura, altura = arquivo_mapa[mapa_escolha]
        with open(arquivo) as arquivo:
            dados = json.load(arquivo)
        return criar_grafo_mapa(dados, largura, altura)
    
    return None

while True:
    print("Selecione o mapa 1 a 4: ")
    mapa_escolha = input()

    # Valida a escolha do mapa
    if mapa_escolha in ['1', '2', '3']:
        break  # Sai do loop se a escolha for válida
    else:
        print("Escolha inválida. Por favor, selecione o mapa 1 a 4.")

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
        print("Escolha inválida. Por favor, selecione uma das opções de algoritmo disponíveis.")
  
 
#carrega  
mapa = carregar_mapa(mapa_escolha)    
#todos os objetivos
all_point:Node = encontrar_node_objetivo_lista(mapa)
#o local de inicio de agente
inicio:Node = encontrar_node_inicial(mapa)

tempo_total_largura: float = 0
custo_total_largura: float = 0

tempo_total_profundidade: float = 0
custo_total_profundidade: float = 0

tempo_total_gulosa: float = 0
custo_total_gulosa: float = 0

tempo_total_a_estrela: float = 0
custo_total_a_estrela: float = 0

if algoritmo_escolha == '1':
    while all_point:
        
        if(all_point and inicio):
            start_time = time.time()
            
            caminho = busca_em_largura(inicio, all_point)
            
            end_time = time.time()
            tempo_total_largura += end_time - start_time 
            
        
        print("Caminho achado entre os nós", caminho[-1].name,"-",caminho[0].name,"\n")    
        
        if caminho:
            for node in caminho:
                print(node.name)
        else:
            print("Nenhum caminho encontrado")
            
        #pausa para mostrar o caminho
        time.sleep(4)    
        
        #mudando o incio do agente para o local do ponto achado
        inicio = caminho[-1]
        #removendo o ponto achado
        all_point.remove(caminho[-1])

        custo_total_largura += custo_caminho(caminho)
        mostrar_caminho(mapa, caminho)
        limpar_node_parente(mapa)
    print("CUSTO TOTAL do algortimo busca em largura: ", custo_total_largura)
    print(f"Tempo de execução: {tempo_total_largura} segundos")

if algoritmo_escolha == '2':
    while all_point:
        
        if(all_point and inicio):
            start_time = time.time()
            
            caminho = busca_em_profundidade(inicio, all_point)
            
            end_time = time.time()
            tempo_total_profundidade += end_time - start_time 
            
        
        print("Caminho achado entre os nós", caminho[-1].name,"-",caminho[0].name,"\n")    
        
        if caminho:
            for node in caminho:
                print(node.name)
        else:
            print("Nenhum caminho encontrado")
            
        #pausa para mostrar o caminho
        time.sleep(4)    
        
        #mudando o incio do agente para o local do ponto achado
        inicio = caminho[-1]
        #removendo o ponto achado
        all_point.remove(caminho[-1])

        custo_total_profundidade += custo_caminho(caminho)
        mostrar_caminho(mapa, caminho)
        limpar_node_parente(mapa)
    print("CUSTO TOTAL do algortimo busca em profundidade: ", custo_total_profundidade)
    print(f"Tempo de execução: {tempo_total_profundidade:.5} segundos")
    
    
if algoritmo_escolha == '3':
    while all_point:
        
        if(all_point and inicio):
            start_time = time.time()
            
            caminho = busca_gulosa(inicio, all_point)
            
            end_time = time.time()
            tempo_total_gulosa += end_time - start_time 
            
        
        print("Caminho achado entre os nós", caminho[-1].name,"-",caminho[0].name,"\n")    
        
        if caminho:
            for node in caminho:
                print(node.name)
        else:
            print("Nenhum caminho encontrado")
            
        #pausa para mostrar o caminho
        time.sleep(4)    
        
        #mudando o incio do agente para o local do ponto achado
        inicio = caminho[-1]
        #removendo o ponto achado
        all_point.remove(caminho[-1])

        custo_total_gulosa += custo_caminho(caminho)
        mostrar_caminho(mapa, caminho)
        limpar_node_parente(mapa)
    print("CUSTO TOTAL do algortimo busca gulosa: ", custo_total_gulosa)
    print(f"Tempo de execução: {tempo_total_gulosa:.5} segundos")    
    
if algoritmo_escolha == '4':
    while all_point:
        
        if(all_point and inicio):
            start_time = time.time()
            
            caminho = a_estrela(inicio, all_point)
            
            end_time = time.time()
            tempo_total_a_estrela += end_time - start_time 
            
        
        print("Caminho achado entre os nós", caminho[-1].name,"-",caminho[0].name,"\n")    
        
        if caminho:
            for node in caminho:
                print(node.name)
        else:
            print("Nenhum caminho encontrado")
            
        #pausa para mostrar o caminho
        time.sleep(4)    
        
        #mudando o incio do agente para o local do ponto achado
        inicio = caminho[-1]
        #removendo o ponto achado
        all_point.remove(caminho[-1])

        custo_total_a_estrela += custo_caminho(caminho)
        mostrar_caminho(mapa, caminho)
        limpar_node_parente(mapa)
    print("CUSTO TOTAL do algortimo busca A*: ", custo_total_a_estrela)
    print(f"Tempo de execução: {tempo_total_a_estrela:.5} segundos")    