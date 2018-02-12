import gui.cell_type as gct


class Cell:

    WIDTH = 40

    # Setter
    def set_type(self, ctype):
        self.m_type = ctype
        self.canvas.itemconfig(self.m_shape, fill=self.m_type["color"])

    # Constructor
    def __init__(self, canvas, x, y, ctype=gct.CellType.EMPTY):
        self.m_x = x
        self.m_y = y
        self.m_type = ctype
        self.canvas = canvas
        self.m_shape = canvas.create_rectangle(
            Cell.WIDTH * x,
            Cell.WIDTH * y,
            Cell.WIDTH * (x + 1),
            Cell.WIDTH * (y + 1),
            fill=self.m_type["color"]
        )
