from tkinter import Tk

import gui.grid as gg
import gui.menu as gms
import gui.menu_animation as gma

from gui.config import Config
from gui.informations_displayer import InformationsDisplayer


class Gui(Tk):

    def __init__(self):
        """
        Constructeur
        """
        super().__init__()
        self.config_tk()

        self.m_menu_animation = gma.MenuAnimation(self)
        self.m_informations_displayer = InformationsDisplayer(self)
        self.m_grid = gg.Grid(self)
        self.m_menu = gms.Menu(self)

        self.config_template()

    def config_tk(self):
        """
        Initialise la fenetre principale
        """
        self.title("Python - Pathfinding algorithms")
        self.geometry("%dx%d+%d+%d" % (
            Config.WIDTH,
            Config.HEIGHT,
            (self.winfo_screenwidth() - Config.WIDTH) // 2,
            (self.winfo_screenheight() - Config.HEIGHT) // 2)
        )
        self.resizable(False, False)

    def config_template(self):
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(1, minsize=Config.LEFT_MENU_WIDTH)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, minsize=Config.RIGHT_MENU_WIDTH)

        self.m_menu_animation.grid(column=1, row=1, rowspan=2, sticky='nwse')
        self.m_informations_displayer.grid(column=1, row=3, sticky='nwse')
        self.m_menu.grid(column=3, row=1, rowspan=3, sticky='nwse')
        self.m_grid.grid(column=2, row=1, rowspan=3, sticky='nwse', padx=10, pady=10)

    def show(self):
        """
        Affiche la fenetre
        """
        self.mainloop()
