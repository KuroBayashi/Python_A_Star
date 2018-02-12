class Node:

    # Setters / Getters
    def set_parent(self, parent):
        self.parent = parent
        self.cost_g += parent.cost_g
        self.cost_f = self.cost_g + self.cost_h

    def set_cost_h(self, cost_heuristic):
        self.cost_h = cost_heuristic
        self.cost_f = self.cost_g + self.cost_h

    # Compare to another node
    def __lt__(self, other):
        return 0 if self.cost_f == other.cost_f else -1 if self.cost_f < other.cost_f else 1

    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cost_f = 0
        self.cost_g = 1
        self.cost_h = 0
        self.parent = None
