from tkinter import Tk

import gui.grid as gg
import gui.menu as gm


class Gui(Tk):

    WIDTH = 861
    HEIGHT = 511

    # Constructor
    def __init__(self):
        super().__init__()
        self.init_window()

        self.m_menu = gm.Menu(self)
        self.m_grid = gg.Grid(self)

    # Build main window
    def init_window(self):
        self.title("Python - Pathfinding algorithms")
        self.geometry("%dx%d+%d+%d" % (
            Gui.WIDTH,
            Gui.HEIGHT,
            (self.winfo_screenwidth() - Gui.WIDTH) // 2,
            (self.winfo_screenheight() - Gui.HEIGHT) // 2)
        )
        self.update()
        self.minsize(self.winfo_width(), self.winfo_height())
        self.resizable(False, False)

    # Show GUI
    def show(self):
        self.mainloop()
