from tkinter import Tk

import gui.grid as gg
import gui.menu as gm


class Gui(Tk):

    MIN_WIDTH = 810
    MIN_HEIGHT = 600

    # Build main window
    def init_window(self):
        self.title("Python - Pathfinding algorithms")
        self.geometry("%dx%d+%d+%d" % (
            Gui.MIN_WIDTH,
            Gui.MIN_HEIGHT,
            (self.winfo_screenwidth() - Gui.MIN_WIDTH) // 2,
            (self.winfo_screenheight() - Gui.MIN_HEIGHT) // 2)
        )
        self.update()
        self.minsize(self.winfo_width(), self.winfo_height())
        self.resizable(False, False)

    # Show GUI
    def show(self):
        self.mainloop()

    # Constructor
    def __init__(self):
        super().__init__()
        self.init_window()

        self.m_menu = gm.Menu(self)
        self.m_grid = gg.Grid(self)
