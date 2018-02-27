from heapq import heappop, heappush

from algorithms.a_star.exception_path_not_found import ExceptionPathNotFound
from algorithms.a_star.heuristic import Heuristic
from history.action_type import ActionType


class AStar:

    # Constructor
    def __init__(self, grid, history, heuristic=Heuristic.manhattan, diagonal_allowed=False):
        self.m_grid = grid
        self.m_heuristic = heuristic
        self.m_diagonal_allowed = diagonal_allowed
        self.m_history = history

    # Run the solver
    def run(self, start, end):
        closed_set = []
        open_set = []

        current = start
        current.set_cost_h(self.m_heuristic(start, end))
        heappush(open_set, current)
        self.m_history.add(ActionType.ADD_TO_OPEN_SET, current)

        while open_set:
            current = heappop(open_set)

            if id(current) == id(end):
                return self.path(start, current)

            closed_set.append(current)
            self.m_history.add(ActionType.ADD_TO_CLOSED_SET, current)

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
                    self.m_history.add(ActionType.ADD_TO_OPEN_SET, node)

        raise ExceptionPathNotFound()

    # Get list of neighbors of the node
    def neighbors(self, node):
        x, y = node.m_x, node.m_y

        coords = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        if self.m_diagonal_allowed:
            coords += [(x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x + 1, y + 1)]

        print(coords)
        return [
            self.m_grid.m_cells[t[1]][t[0]] for t in coords
            if 0 <= t[0] < len(self.m_grid.m_cells[0])
                and 0 <= t[1] < len(self.m_grid.m_cells)
                and self.m_grid.m_cells[t[1]][t[0]].m_traversable
        ]

    # Get list of nodes to build path
    def path(self, start, end):
        path = []

        while end.m_parent is not None:
            path.append(end)
            end = end.m_parent

        self.m_history.add(ActionType.ADD_TO_PATH, start)
        for node in reversed(path):
            self.m_history.add(ActionType.ADD_TO_PATH, node)

        return path

    # Get "distance" (cost g) between 2 nodes
    @staticmethod
    def distance(a, b):
        return 1
