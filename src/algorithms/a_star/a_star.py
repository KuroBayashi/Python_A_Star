from algorithms.a_star.exception_path_not_found import ExceptionPathNotFound
from algorithms.a_star.heuristic import Heuristic


class AStar:

    # Get list of nodes to build path
    def get_path(self, node):
        path = []

        while node.parent is not None:
            node = node.parent
            path.append(node)

        return path

    # Get list of neighbors of the node
    def get_neightbors(self, node):
        x, y = node.x, node.y

        coords = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        if self.m_diagonal_allowed:
            coords += [(x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1)]

        return [
            self.m_grid[t[0]][t[1]] for t in coords
            if 0 <= t[0] < len(self.m_grid[0]) and 0 <= t[1] < len(self.m_grid)
        ]

    # Run the solver
    def run(self, start, end):
        open_set = []
        closed_set = []

        current = start
        open_set.append(current)

        try:
            while len(open_set):
                current = open_set.pop(0)

                if current == end:
                    return self.get_path(current)

                open_set.remove(current)
                closed_set.append(current)

                for node in self.get_neightbors(current):
                    if node in closed_set:
                        continue

                    if node not in open_set:
                        cost_g = current.m_cost_g + node.m_cost_g       # TEST

                        if node.m_cost_g > cost_g:
                            node.set_parent(current)
                    else:
                        node.set_parent(current)
                        node.set_cost_h(self.heuristic(node, end))
                        open_set.append(node)

            raise ExceptionPathNotFound()
        except ExceptionPathNotFound as e:
            print("Exception : ", e.m_message)

    # Constructor
    def __init__(self, grid, heuristic=Heuristic.manhattan, diagonal_allowed=True):
        self.m_grid = grid
        self.heuristic = heuristic
        self.m_diagonal_allowed = diagonal_allowed
