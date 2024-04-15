from config.imports import *

def mostrar_caminho(mapa, caminho):
    
    print()
    
    for node in caminho:
        node.is_agent = True
        time.sleep(0.5)
        os.system('cls')
        Printar_mapa(mapa)
        node.is_agent = False
        node.is_point = False
time.sleep(4)       
