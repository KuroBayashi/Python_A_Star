from tkinter import Tk, Y, RIGHT, LEFT

import gui.grid as gg
import gui.menu as gms
import gui.menu_animation as gma


class Gui(Tk):

    GRID_MARGIN = 5

    WIDTH = gg.Grid.WIDTH + gms.Menu.WIDTH + 2 * GRID_MARGIN + gma.MenuAnimation.WIDTH
    HEIGHT = max(gg.Grid.HEIGHT, gms.Menu.MIN_HEIGHT, gma.MenuAnimation.MIN_HEIGHT) + 2 * GRID_MARGIN

    def __init__(self):
        """
        Constructeur
        """
        super().__init__()
        self.init_window()

        self.m_grid = gg.Grid(self)
        self.m_menu = gms.Menu(self)
        self.m_menu_animation = gma.MenuAnimation(self)

        self.config_template()

    def init_window(self):
        """
        Initialise la fenetre principale
        """
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

    def config_template(self):
        self.m_menu_animation.pack(fill=Y, side=LEFT)
        self.m_menu.pack(fill=Y, side=RIGHT)
        self.m_grid.pack(expand=True)

    def show(self):
        """
        Affiche la fenetre
        """
        self.mainloop()
