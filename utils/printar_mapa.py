from config.imports import *

def Printar_mapa(mapa):
    # Função para mapear o tipo de terreno para um símbolo
    def mapear_terreno(type_ground, is_agent, is_point):
        
        # se for o agente ou o objetivo
        if is_agent:
            return "☺"
        if is_point:
            return "$"
            
        if type_ground == "parede":
            return "▓"
        elif type_ground == "solido_e_plano":
            return "s"  # Substitua "@" pelo símbolo correspondente ao segundo tipo de terreno
        elif type_ground == "rochoso":
            return "r"  # Símbolo para tipos de terreno desconhecidos
        elif type_ground == "pantano":
            return "p"  # Símbolo para tipos de terreno desconhecidos
        elif type_ground == "arenoso":
            return "a"
        
        ##se tiver nada 
        return "𖠃"
        
    # self.is_agent = is_agent
    #    self.is_point = is_point
    for linha in mapa:
        for elemento in linha:
            print(mapear_terreno(elemento.type_ground, elemento.is_agent, elemento.is_point), end='')
        print()  # Adiciona uma quebra de linha após cada linha
        