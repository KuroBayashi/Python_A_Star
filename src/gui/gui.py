from tkinter import Tk, Frame, Y, RIGHT

import gui.grid as gg


class Gui(Tk):

    MIN_WIDTH = 810
    MIN_HEIGHT = 600
    OPTIONS_WIDTH = 250

    # Build options panel
    def draw_options(self):
        self._options.configure(width=Gui.OPTIONS_WIDTH)
        self._options.configure(background="#3f4d59")
        self._options.pack(fill=Y, side=RIGHT)

    # Build main window
    def init_window(self):
        self.title("Python - A* algorithm (Test)")
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

        self._options = Frame(self)
        self.draw_options()

        self._grid = gg.Grid(self)
