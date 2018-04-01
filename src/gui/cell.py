from algorithms.a_star.node import Node


class Cell(Node):

    WIDTH = 20

    def __init__(self, canvas, x, y, cell_type):
        """
        Constructeur

        :param canvas: Zone de dessin
        :param x: Position horizontale du noeud
        :param y: Position verticale du noeud
        :param cell_type: Type de cellule

        :type canvas: Canvas
        :type x: int
        :type y: int
        :type cell_type: CellType
        """
        super().__init__(x, y, cell_type["traversable"])
        self.m_canvas = canvas
        self.m_type = cell_type
        self.m_shape = canvas.create_rectangle(
            Cell.WIDTH * x,
            Cell.WIDTH * y,
            Cell.WIDTH * (x + 1),
            Cell.WIDTH * (y + 1),
            fill=cell_type["color"]
        )

    def set_type(self, cell_type):
        """
        Change le type de cellule

        :param cell_type: Type de cellule

        :type cell_type: CellType
        """
        self.m_type = cell_type
        self.set_traversable(cell_type["traversable"])
        self.m_canvas.itemconfig(self.m_shape, fill=cell_type["color"])
