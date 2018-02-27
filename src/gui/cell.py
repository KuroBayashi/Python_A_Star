import gui.cell_type as gct
from algorithms.a_star.node import Node


class Cell(Node):

    WIDTH = 40

    # Setter
    def set_type(self, cell_type):
        self.m_type = cell_type
        self.m_traversable = cell_type["traversable"]
        self.m_canvas.itemconfig(self.m_shape, fill=cell_type["color"])

    # Constructor
    def __init__(self, canvas, x, y, cell_type=gct.CellType.EMPTY):
        super().__init__(x, y)
        self.m_canvas = canvas
        self.m_type = cell_type
        self.m_shape = canvas.create_rectangle(
            Cell.WIDTH * x,
            Cell.WIDTH * y,
            Cell.WIDTH * (x + 1),
            Cell.WIDTH * (y + 1),
            fill=self.m_type["color"]
        )
