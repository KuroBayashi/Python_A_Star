from algorithms.a_star.node import Node


class Cell(Node):

    WIDTH = 20

    def __init__(self, canvas, x, y, cell_type):
        """
        Constructeur

        :param Canvas canvas : Zone de dessin
        :param int x : Position horizontale du noeud
        :param int y : Position verticale du noeud
        :param dict cell_type : Type de cellule
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

        :param dict cell_type : Type de cellule
        """
        self.m_type = cell_type
        self.set_traversable(cell_type["traversable"])
        self.m_canvas.itemconfig(self.m_shape, fill=cell_type["color"])
