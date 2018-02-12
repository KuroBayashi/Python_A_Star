from tkinter import Canvas, BOTH

import gui.cell as gc
import gui.cell_type as gct
from gui.grid_event_manager import GridEventManager


class Grid(Canvas):

    # Draw lines
    def draw_lines(self):
        self.update()

        for i in range(0, self.winfo_width(), gc.Cell.WIDTH):
            self.create_line(0, i, self.winfo_width(), i)
        for j in range(0, self.winfo_height(), gc.Cell.WIDTH):
            self.create_line(j, 0,  j, self.winfo_height())

    # Build cells
    def build_cells(self):
        self.m_cells = [
            [gc.Cell(self, x, y) for x in range(self.winfo_width() // gc.Cell.WIDTH)]
            for y in range(self.winfo_height() // gc.Cell.WIDTH)
        ]
        self.m_cells[1][1].set_type(gct.CellType.START)
        self.m_cells[len(self.m_cells) - 2][len(self.m_cells[0]) - 2].set_type(gct.CellType.END)

    # Setup canvas
    def setup_canvas(self):
        self.configure(background="#f1f1f1", highlightthickness=0)
        self.pack(expand=True, fill=BOTH)
        self.update()

    # Constructor
    def __init__(self, root):
        super().__init__(root)
        self.setup_canvas()

        self.m_cells = []
        self.m_event_manager = GridEventManager(self)

        self.build_cells()
        self.draw_lines()
