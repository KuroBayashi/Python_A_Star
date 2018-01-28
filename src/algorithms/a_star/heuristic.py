from math import sqrt


class Heuristic:

    @staticmethod
    def manhattan(node, target):
        dx = abs(node.x - target.x)
        dy = abs(node.y - target.y)

        return dx + dy

    @staticmethod
    def chebyshev(node, target):
        dx = abs(node.x - target.x)
        dy = abs(node.y - target.y)

        return (dx + dy) - min(dx, dy)

    @staticmethod
    def octile(node, target):
        dx = abs(node.x - target.x)
        dy = abs(node.y - target.y)

        return (dx + dy) + (sqrt(2) - 2) * min(dx, dy)

    @staticmethod
    def euclidean(node, target):
        dx = abs(node.x - target.x)
        dy = abs(node.y - target.y)

        return sqrt(dx * dx + dy * dy)
