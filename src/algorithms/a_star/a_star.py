from heapq import heappop, heappush
from math import sqrt
from timeit import default_timer

from history.action_type import ActionType
from algorithms.a_star.exception_path_not_found import ExceptionPathNotFound


class AStar:

    def __init__(self, grid, history, heuristic, diagonal_allowed=False):
        """
        Constructeur

        :param grid: Grille contenant les noeuds
        :param history: Historique des actions effectues pour l'animation finale
        :param heuristic: Fonction pour le calcul de l'heuristique entre 2 noeuds
        :param diagonal_allowed: Deplacement en diagonal autorise ou non

        :type grid: Grid
        :type history: History
        :type heuristic: callable
        :type diagonal_allowed: bool
        """
        self.m_grid = grid
        self.m_heuristic = heuristic
        self.m_diagonal_allowed = diagonal_allowed
        self.m_history = history
        self.m_start_time = 0

    def run(self, start, end):
        """
        Recherche du chemin le plus court

        :param start: Noeud de depart
        :param end: Noeud d'arrivee

        :type start: Node
        :type end: Node

        :return: list(Node)

        :except ExceptionPathNotFound: Erreur levee en cas de chemin impossible
        """
        self.m_start_time = default_timer()

        closed_set = []
        open_set = []

        current = start
        current.set_cost_h(self.m_heuristic(start, end))
        heappush(open_set, current)

        while open_set:
            current = heappop(open_set)
            self.m_history.add(ActionType.SET_CURRENT, current, default_timer()-self.m_start_time)

            if id(current) == id(end):
                return self.path(current)

            closed_set.append(current)
            if id(current) != id(start):
                self.m_history.add(ActionType.ADD_TO_CLOSED_SET, current, default_timer()-self.m_start_time)

            for node in self.neighbors(current):
                if node in closed_set:
                    continue

                tmp_cost_g = current.m_cost_g + self.distance(current, node)

                if node in open_set:
                    if node.m_cost_g > tmp_cost_g:
                        node.set_cost_g(tmp_cost_g)
                        node.set_parent(current)
                else:
                    node.set_cost_g(tmp_cost_g)
                    node.set_cost_h(self.m_heuristic(node, end))
                    node.set_parent(current)
                    heappush(open_set, node)
                    self.m_history.add(ActionType.ADD_TO_OPEN_SET, node, default_timer()-self.m_start_time)

        raise ExceptionPathNotFound()

    def neighbors(self, node):
        """
        Recupere les noeuds atteignables

        :param node: Noeud actuel

        :type node: None

        :return: list(Node)
        """
        x, y = node.m_x, node.m_y

        coords = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        if self.m_diagonal_allowed:
            coords += [(x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x + 1, y + 1)]

        neighbors = []
        for cx, cy in coords:
            if 0 <= cx < len(self.m_grid.m_cells[0]) and \
                    0 <= cy < len(self.m_grid.m_cells) and \
                    self.m_grid.m_cells[cy][cx].m_traversable:
                neighbors.append(self.m_grid.m_cells[cy][cx])

        return neighbors

    def path(self, node):
        """
        Construction du chemin le plus court sous forme de liste ordonee des noeuds qui le compose
        (depart vers arrivee)

        :param node: Noeud d'arrivee

        :type node: Node

        :return: list(Node)
        """
        path = []

        while node is not None:
            path.insert(0, node)
            node = node.m_parent

        for node in path:
            self.m_history.add(ActionType.ADD_TO_PATH, node, default_timer()-self.m_start_time)

        return path

    @staticmethod
    def distance(a, b):
        """
        Calcul du `cout G` entre deux points

        :param a: Noeud 1
        :param b: Noeud 2

        :type a: Node
        :type b: Node

        :return: int
        """
        if a.m_x == b.m_x or a.m_y == b.m_y:
            return 1
        else:
            return sqrt(2)
