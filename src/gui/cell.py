import gui.cell_type as gct
from algorithms.a_star.node import Node


class Cell(Node):

    WIDTH = 40

    # Setter
    def set_type(self, ctype):
        self.m_type = ctype
        self.m_canvas.itemconfig(self.m_shape, fill=self.m_type["color"])

    # Constructor
    def __init__(self, canvas, x, y, ctype=gct.CellType.EMPTY):
        super().__init__(x, y)
        self.m_type = ctype
        self.m_canvas = canvas
        self.m_shape = canvas.create_rectangle(
            Cell.WIDTH * x,
            Cell.WIDTH * y,
            Cell.WIDTH * (x + 1),
            Cell.WIDTH * (y + 1),
            fill=self.m_type["color"]
        )
