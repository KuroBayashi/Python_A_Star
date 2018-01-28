from tkinter import Canvas, BOTH

import gui.cell as gc


class Grid(Canvas):

    # Draw grid
    def draw_grid(self, e):
        self.update()
        count_cols = self.winfo_width() // gc.Cell.WIDTH + 1
        count_lines = self.winfo_height() // gc.Cell.WIDTH + 1

        for i in range(count_lines):
            self.create_line(0, gc.Cell.WIDTH * i, self.winfo_width(), gc.Cell.WIDTH * i)
        for j in range(count_cols):
            self.create_line(gc.Cell.WIDTH * j, 0, gc.Cell.WIDTH * j, self.winfo_height())

    # Bind events
    def bind_events(self):
        self.bind("<Configure>", self.draw_grid)

    # Init grid
    def init_grid(self):
        self.configure(background="#f1f1f1", highlightthickness=0)
        self.pack(expand=True, fill=BOTH)
        self.update()

    # Constructor
    def __init__(self, root):
        super().__init__(root)
        self.init_grid()

        self.m_cells = [[gc.Cell(self, x, y) for x in range(self.winfo_width() // gc.Cell.WIDTH)] for y in range(self.winfo_height() // gc.Cell.WIDTH)]

        self.bind_events()
