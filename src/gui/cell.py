import gui.cell_type as gct


class Cell:

    WIDTH = 40

    # Event : on click
    def toggle_wall(self, e):
        if self.m_type["id"] == gct.CellType.WALL["id"]:
            self.m_type = gct.CellType.EMPTY
        elif self.m_type["id"] != gct.CellType.START["id"] \
                and self.m_type != gct.CellType.END["id"]:
            self.m_type = gct.CellType.WALL

        self.canvas.itemconfig(self.m_shape, fill=self.m_type["color"])

    # Bind events
    def bind_events(self):
        self.canvas.tag_bind(self.m_shape, "<Button-1>", self.toggle_wall)

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

        self.bind_events()