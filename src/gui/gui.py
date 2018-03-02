from tkinter import Tk

import gui.grid as gg
import gui.menu as gm


class Gui(Tk):

    WIDTH = 861 # + 1 pour la bordure droite de la grille
    HEIGHT = 511 # + 1 pour la bordure basse de la grille

    def __init__(self):
        """
        Constructeur
        """
        super().__init__()
        self.init_window()

        self.m_menu = gm.Menu(self)
        self.m_grid = gg.Grid(self)

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

    def show(self):
        """
        Affiche la fenetre
        """
        self.mainloop()
