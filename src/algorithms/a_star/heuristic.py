from math import sqrt
import sys


class Heuristic:

    @staticmethod
    def manhattan(node, target):
        dx = abs(node.m_x - target.m_x)
        dy = abs(node.m_y - target.m_y)

        return dx + dy

    @staticmethod
    def chebyshev(node, target):
        dx = abs(node.m_x - target.m_x)
        dy = abs(node.m_y - target.m_y)

        return (dx + dy) - min(dx, dy)

    @staticmethod
    def octile(node, target):
        dx = abs(node.m_x - target.m_x)
        dy = abs(node.m_y - target.m_y)

        return (dx + dy) + (sqrt(2) - 2) * min(dx, dy)

    @staticmethod
    def euclidean(node, target):
        dx = abs(node.m_x - target.m_x)
        dy = abs(node.m_y - target.m_y)

        return sqrt(dx * dx + dy * dy)

    @staticmethod
    def dijkstra(node, target):
        return sys.maxsize
