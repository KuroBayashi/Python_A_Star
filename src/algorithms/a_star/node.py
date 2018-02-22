class Node:

    # Setters / Getters
    def set_parent(self, parent):
        self.m_parent = parent

    def set_cost_h(self, cost_heuristic):
        self.m_cost_h = cost_heuristic
        self.m_cost_f = self.m_cost_g + self.m_cost_h

    # Compare to another node
    def __lt__(self, other):
        return self.m_cost_f < other.cost_f

    def __le__(self, other):
        return self.m_cost_f <= other.cost_f

    def __eq__(self, other):
        return self.m_cost_f == other.cost_f

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return self.m_cost_f > other.cost_f

    def __ge__(self, other):
        return self.m_cost_f >= other.cost_f

    # Constructor
    def __init__(self, x, y):
        self.m_x = x
        self.m_y = y
        self.m_cost_f = 0
        self.m_cost_g = 0
        self.m_cost_h = 0
        self.m_parent = None
        self.m_neighbors = []
