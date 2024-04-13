class Node:
    def __init__(self, name, heuristic_cost=0, type_ground='', cost_ground=0, is_agent=False, is_point=False, column = 0, row= 0):
        self.name = name
        
        self.column = column
        self.row = row
        
        self.type_ground = type_ground
        self.cost_ground = cost_ground
        
        self.is_agent = is_agent
        self.is_point = is_point
        
        self.heuristic_cost = heuristic_cost
        self.actual_cost = float('inf')
        self.parent = None
        self.neighbor_north = None  # Inicialize os vizinhos como None
        self.neighbor_south = None
        self.neighbor_left = None
        self.neighbor_right = None

    def add_neighbor(self, orientation: str, neighbor):
        if orientation == 'north':
            self.neighbor_north = neighbor
            neighbor.add_neighbor_reverse('south', self)
        elif orientation == 'south':
            self.neighbor_south = neighbor
            neighbor.add_neighbor_reverse('north', self)
        elif orientation == 'right':
            self.neighbor_right = neighbor
            neighbor.add_neighbor_reverse('left', self)
        elif orientation == 'left':
            self.neighbor_left = neighbor
            neighbor.add_neighbor_reverse('right', self)

    def add_neighbor_reverse(self, orientation, neighbor):
        if orientation == 'north':
            self.neighbor_north = neighbor
        elif orientation == 'south':
            self.neighbor_south = neighbor
        elif orientation == 'right':
            self.neighbor_right = neighbor
        elif orientation == 'left':
            self.neighbor_left = neighbor
