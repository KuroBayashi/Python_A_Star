from heapq import heappop, heappush

from algorithms.a_star.exception_path_not_found import ExceptionPathNotFound
from algorithms.a_star.heuristic import Heuristic


class AStar:

    # Get list of nodes to build path
    @staticmethod
    def get_path(node):
        path = []

        while node.parent is not None:
            node = node.parent
            path.append(node)

        return path

    # Get list of neighbors of the node
    # def get_neighbors(self, node):
    #     x, y = node.x, node.y
    #
    #     coords = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    #     if self.m_diagonal_allowed:
    #         coords += [(x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1)]
    #
    #     return [
    #         self.m_grid[t[0]][t[1]] for t in coords
    #         if 0 <= t[0] < len(self.m_grid[0]) and 0 <= t[1] < len(self.m_grid)
    #     ]

    # Run the solver
    def run(self, start, end):
        closed_set = []
        open_set = []

        current = start
        heappush(open_set, current)

        try:
            while open_set:
                current = heappop(open_set)

                if current == end:
                    return self.get_path(current)

                closed_set.append(current)

                for node in current.m_neighbors:
                    if node in closed_set:
                        continue

                    if node not in open_set:
                        cost_g = current.m_cost_g + node.m_cost_g       # TEST

                        if node.m_cost_g > cost_g:
                            node.set_parent(current)
                    else:
                        node.set_parent(current)
                        node.set_cost_h(self.m_heuristic(node, end))
                        heappush(open_set, node)

            raise ExceptionPathNotFound()
        except ExceptionPathNotFound as e:
            print("Exception : ", e.m_message)

    # Constructor
    def __init__(self, grid, heuristic=Heuristic.manhattan, diagonal_allowed=False):
        self.m_grid = grid
        self.m_heuristic = heuristic
        self.m_diagonal_allowed = diagonal_allowed
