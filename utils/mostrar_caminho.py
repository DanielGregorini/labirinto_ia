from config.imports import *

def mostrar_caminho(mapa, caminho, texto: str):
    
    print()
    
    for node in caminho:
        node.is_agent = True
        time.sleep(0.3)
        os.system('cls')
        
        print(texto)
        Printar_mapa(mapa)
        
        node.is_agent = False
        node.is_point = False
time.sleep(1)       