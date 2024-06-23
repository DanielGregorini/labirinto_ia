from config.imports import *

#valor de cada ponto secundario
value_secondary: float = 1

while True:
    print("Selecione o mapa 1 a 4: ")
    mapa_escolha = input()

    # Valida a escolha do mapa
    if mapa_escolha in ['1', '2', '3', '4']:
        break  # Sai do loop se a escolha for válida
    else:
        print("Escolha inválida. Por favor, selecione o mapa 1 a 4.")

#carrega  
#mapa = carregar_mapa(mapa_escolha)  
mapa = carregar_mapa(mapa_escolha)  
Printar_mapa(mapa)  
#todos os objetivos4
all_point:list[Node] = encontrar_node_objetivo_lista(mapa)
#todos os objetivos secundarios
all_secundary:list[Node] = encontrar_node_objetivo_secundario_lista(mapa)
#o local de inicio de agente
inicio:Node = encontrar_node_inicial(mapa)

#variaveis de controle de custo, tempo e pontos
tempo_total_largura: float = 0
custo_total_largura: float = 0
pontos_total_largura: int = 0

tempo_total_profundidade: float = 0
custo_total_profundidade: float = 0
pontos_total_profundidade: int = 0

tempo_total_gulosa: float = 0
custo_total_gulosa: float = 0
pontos_total_gulosa: int = 0

tempo_total_a_estrela: float = 0
custo_total_a_estrela: float = 0
pontos_total_a_estrela: int = 0

while all_point:
    if(all_point and inicio):
            
        start_time = time.time()
        caminho = busca_em_largura(inicio, all_point, all_secundary)
        end_time = time.time()
            
        tempo_total_largura += end_time - start_time 
            
    print("Caminho achado entre os nós", caminho[-1].name,"-",caminho[0].name,"\n")    
        
    if caminho:
        pontos_total_largura += 1
        for node in caminho:
            if(node.is_secondary):
                pontos_total_largura += value_secondary
            print(node.name)
    else:
        print("Nenhum caminho encontrado")
        time.sleep(2)  
            
    #pausa para mostrar o caminho
    time.sleep(1)    
        
    #mudando o incio do agente para o local do ponto achado
    inicio = caminho[-1]
    #removendo o ponto achado
    all_point.remove(caminho[-1])

    custo_total_largura += custo_caminho(caminho)
    mostrar_caminho(mapa, caminho)
    limpar_node_parente(mapa)


mapa = carregar_mapa(mapa_escolha)    
#todos os objetivos
all_point:Node = encontrar_node_objetivo_lista(mapa)
#todos os objetivos secundarios
all_secundary = encontrar_node_objetivo_secundario_lista(mapa)
#o local de inicio de agente
inicio:Node = encontrar_node_inicial(mapa)

while all_point:
    
    if(all_point and inicio):
        start_time = time.time()
            
        caminho = busca_em_profundidade(inicio, all_point, all_secundary)
            
        end_time = time.time()
        tempo_total_profundidade += end_time - start_time 
             
    print("Caminho achado entre os nós", caminho[-1].name,"-",caminho[0].name,"\n")    
        
    if caminho:
        pontos_total_profundidade += 1
        for node in caminho:
            if(node.is_secondary):
                pontos_total_profundidade += value_secondary
            print(node.name)
    else:
        print("Nenhum caminho encontrado")
        time.sleep(2) 
            
    #pausa para mostrar o caminho
    time.sleep(1)    
        
    #mudando o incio do agente para o local do ponto achado
    inicio = caminho[-1]
    #removendo o ponto achado
    all_point.remove(caminho[-1])

    custo_total_profundidade += custo_caminho(caminho)
    mostrar_caminho(mapa, caminho)
    limpar_node_parente(mapa)

mapa = carregar_mapa(mapa_escolha)    
#todos os objetivos
all_point:Node = encontrar_node_objetivo_lista(mapa)
#todos os objetivos secundarios
all_secundary = encontrar_node_objetivo_secundario_lista(mapa)
#o local de inicio de agente
inicio:Node = encontrar_node_inicial(mapa)

while all_point:

    if(all_point and inicio):
        start_time = time.time()
            
        caminho = busca_gulosa(inicio, all_point, all_secundary)
            
        end_time = time.time()
        tempo_total_gulosa += end_time - start_time 
            
    print("Caminho achado entre os nós", caminho[-1].name,"-",caminho[0].name,"\n")    
        
    if caminho:
        pontos_total_gulosa += 1
        for node in caminho:
            if(node.is_secondary):
                pontos_total_gulosa += value_secondary
            print(node.name)
    else:
        print("Nenhum caminho encontrado")
            
    #pausa para mostrar o caminho
    time.sleep(1)    
        
    #mudando o incio do agente para o local do ponto achado
    inicio = caminho[-1]
    #removendo o ponto achado
    all_point.remove(caminho[-1])

    custo_total_gulosa += custo_caminho(caminho)
    mostrar_caminho(mapa, caminho)
        
    limpar_node_parente(mapa)
  
mapa = carregar_mapa(mapa_escolha)    
#todos os objetivos
all_point:Node = encontrar_node_objetivo_lista(mapa)
#todos os objetivos secundarios
all_secundary = encontrar_node_objetivo_secundario_lista(mapa)
#o local de inicio de agente
inicio:Node = encontrar_node_inicial(mapa)

while all_point:
        
    if(all_point and inicio):
        start_time = time.time()
            
        caminho = a_estrela(inicio, all_point, all_secundary)
            
        end_time = time.time()
        tempo_total_a_estrela += end_time - start_time 
            
    print("Caminho achado entre os nós", caminho[-1].name,"-",caminho[0].name,"\n")    
        
    if caminho:
            pontos_total_a_estrela += 1
            for node in caminho:
                if(node.is_secondary):
                    pontos_total_a_estrela += value_secondary
                print(node.name)
    else:
        print("Nenhum caminho encontrado")
            
    #pausa para mostrar o caminho
    time.sleep(1)    
        
    #mudando o incio do agente para o local do ponto achado
    inicio = caminho[-1]
    #removendo o ponto achado
    all_point.remove(caminho[-1])

    custo_total_a_estrela += custo_caminho(caminho)
    mostrar_caminho(mapa, caminho)
    limpar_node_parente(mapa)
        
print("CUSTO TOTAL do algortimo busca em largura: ", custo_total_largura)
print(f"Tempo de execução: {tempo_total_largura:.5} segundos")
print(f"Quantidade pontos: {pontos_total_largura}\n")

print("CUSTO TOTAL do algortimo busca em profundidade: ", custo_total_profundidade)
print(f"Tempo de execução: {tempo_total_profundidade:.5} segundos")
print(f"Quantidade pontos: {pontos_total_profundidade}\n")

print("CUSTO TOTAL do algortimo busca gulosa: ", custo_total_gulosa)
print(f"Tempo de execução: {tempo_total_gulosa:.5} segundos")  
print(f"Quantidade pontos: {pontos_total_gulosa}\n")

print("CUSTO TOTAL do algortimo busca A*: ",custo_total_a_estrela)
print(f"Tempo de execução: {tempo_total_a_estrela:.5}  segundos")  
print(f"Quantidade pontos: {pontos_total_a_estrela}\n") 