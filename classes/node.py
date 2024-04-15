class Node:
    def __init__(self, name: str, heuristic_cost:float=0, type_ground='', cost_ground:float=0, is_agent = False, is_point:bool = False, column:int = 0, row:int = 0):
        self.name = name
        
        self.column: int = column
        self.row: int = row
        
        self.type_ground = type_ground
        self.cost_ground = cost_ground
        
        self.is_agent = is_agent
        self.is_point = is_point
        
        self.heuristic_cost = heuristic_cost
        self.actual_cost = float('inf')
        self.parent = None
     
        self.neighbor_top = None 
        self.neighbor_down = None
        self.neighbor_left = None
        self.neighbor_right = None

    def add_neighbor(self, orientation: str, neighbor):
        if orientation == 'top':
            self.neighbor_top = neighbor
            neighbor.add_neighbor_reverse('down', self)
        elif orientation == 'down':
            self.neighbor_down = neighbor
            neighbor.add_neighbor_reverse('top', self)
        elif orientation == 'right':
            self.neighbor_right = neighbor
            neighbor.add_neighbor_reverse('left', self)
        elif orientation == 'left':
            self.neighbor_left = neighbor
            neighbor.add_neighbor_reverse('right', self)

    def add_neighbor_reverse(self, orientation, neighbor):
        if orientation == 'top':
            self.neighbor_top = neighbor
        elif orientation == 'down':
            self.neighbor_down = neighbor
        elif orientation == 'right':
            self.neighbor_right = neighbor
        elif orientation == 'left':
            self.neighbor_left = neighbor
            
    def get_neighbors_profundidade(self):
        vizinhos = []
        if self.neighbor_left and self.neighbor_left.type_ground != "parede":
            vizinhos.append(self.neighbor_left)
        if self.neighbor_down and self.neighbor_down.type_ground != "parede":
            vizinhos.append(self.neighbor_down)
        if self.neighbor_right and self.neighbor_right.type_ground != "parede":
            vizinhos.append(self.neighbor_right)  
        if self.neighbor_top and self.neighbor_top.type_ground != "parede":
            vizinhos.append(self.neighbor_top)   
        return vizinhos
    
    def get_neighbors_largura(self):
        vizinhos = []
        if self.neighbor_right and self.neighbor_right.type_ground != "parede":
            vizinhos.append(self.neighbor_right) 
        if self.neighbor_left and self.neighbor_left.type_ground != "parede":
            vizinhos.append(self.neighbor_left)
        if self.neighbor_down and self.neighbor_down.type_ground != "parede":
            vizinhos.append(self.neighbor_down)
        if self.neighbor_top and self.neighbor_top.type_ground != "parede":
            vizinhos.append(self.neighbor_top)    
        return vizinhos
