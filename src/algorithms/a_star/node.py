class Node:

    def __init__(self, x, y, traversable):
        """
        Constructeur

        :param int x : Position horizontale
        :param int y : Position verticale
        :param bool traversable : Traversabilite
        """
        self.m_x = x
        self.m_y = y
        self.m_cost_f = 0
        self.m_cost_g = 0
        self.m_cost_h = 0
        self.m_traversable = traversable
        self.m_parent = None

    def reset(self):
        """
        Remet le noeud aux valeurs initiales
        """
        self.m_cost_f = 0
        self.m_cost_g = 0
        self.m_cost_h = 0
        self.m_parent = None

    def set_cost_g(self, cost_g):
        """
        Change le `cout G`

        :param int cost_g : Nouveau `cout G`
        """
        self.m_cost_g = cost_g
        self.m_cost_f = self.m_cost_g + self.m_cost_h

    def set_cost_h(self, cost_heuristic):
        """
        Change le `cout H`

        :param int cost_heuristic : Nouveau `cout H`
        """
        self.m_cost_h = cost_heuristic
        self.m_cost_f = self.m_cost_g + self.m_cost_h

    def set_traversable(self, traversable):
        """
        Change la traversabilite

        :param bool traversable : Nouvelle traversabilite
        """
        self.m_traversable = traversable

    def set_parent(self, parent):
        """
        Change le noeud parent

        :param Node parent : Nouveau noeud parent
        """
        self.m_parent = parent

    # Surcharge des methodes de comparaison pour Heapq
    def __lt__(self, other):
        return self.m_cost_f < other.m_cost_f

    def __le__(self, other):
        return self.m_cost_f <= other.m_cost_f

    def __eq__(self, other):
        return self.m_cost_f == other.m_cost_f

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return self.m_cost_f > other.m_cost_f

    def __ge__(self, other):
        return self.m_cost_f >= other.m_cost_f
