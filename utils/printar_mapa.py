def Printar_mapa(mapa):
    # Função para mapear o tipo de terreno para um símbolo com cor
    def mapear_terreno(type_ground, is_agent, is_point):
        # Definindo cores com códigos ANSI
        cor_parede = "\033[90m"  # Cinza escuro
        cor_solido_plano = "\033[97m"  # Branco
        cor_rochoso = "\033[37m"  # Cinza claro
        cor_pantano = "\033[32m"  # Verde
        cor_arenoso = "\033[33m"  # Amarelo
        cor_agente = "\033[34m"  # Azul
        cor_objetivo = "\033[31m"  # Vermelho
        reset_cor = "\033[0m"  # Reseta para a cor padrão
        
        if is_agent:
            return f"{cor_agente}☺{reset_cor}"
        if is_point:
            return f"{cor_objetivo}${reset_cor}"
        
        if type_ground == "parede":
            return f"{cor_parede}▓{reset_cor}"
        elif type_ground == "solido_e_plano":
            return f"{cor_solido_plano}s{reset_cor}"
        elif type_ground == "rochoso":
            return f"{cor_rochoso}r{reset_cor}"
        elif type_ground == "pantano":
            return f"{cor_pantano}p{reset_cor}"
        elif type_ground == "arenoso":
            return f"{cor_arenoso}a{reset_cor}"
        
        return " "  # Espaço para terreno desconhecido
    
    for linha in mapa:
        for elemento in linha:
            print(mapear_terreno(elemento.type_ground, elemento.is_agent, elemento.is_point), end='')
        print()  # Adiciona uma quebra de linha após cada linha
