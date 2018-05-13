from tkinter import Canvas

import gui.cell as gcc
import gui.cell_type as gct

from gui.config import Config
from gui.grid_event_manager import GridEventManager


class Grid(Canvas):

    def __init__(self, root):
        """
        Constructeur

        :param root: Fenetre racine

        :type root: Tk
        """
        super().__init__(root)
        self.setup_canvas()

        self.m_cells = []
        self.m_event_manager = GridEventManager(self)

        self.m_cell_size = Config.CELL_SIZE
        self.m_rows = 1
        self.m_cols = 1
        self.bind('<Configure>', self.draw_grid)

    def setup_canvas(self):
        """
        Initialise le canvas
        """
        self.configure(
            highlightthickness=0
        )

    def draw_grid(self, event):
        """
        Calcul le nombre de colonne et de ligne, puis dessine la grille

        :param event: Evenement genere

        :type event: Event
        """
        self.m_rows = (event.height - 1) // self.m_cell_size
        self.m_cols = (event.width - 1) // self.m_cell_size

        self.draw_lines()
        self.build_cells()

        self.configure(
            width=self.m_cell_size*self.m_cols+1,
            height=self.m_cell_size*self.m_rows+1,
        )
        self.grid_configure(sticky='')

    def draw_lines(self):
        """
        Dessine les lignes de la grille
        """
        for i in range(self.m_rows+1):
            self.create_line(0, i * self.m_cell_size, self.m_cols * self.m_cell_size, i * self.m_cell_size)
        for j in range(self.m_cols+1):
            self.create_line(j * self.m_cell_size, 0,  j * self.m_cell_size, self.m_rows * self.m_cell_size)

    def build_cells(self):
        """
        Construction des cellules de la grille et positionnement des cellules de départ et d'arrivee
        """
        self.m_cells = [
            [gcc.Cell(self, x, y, gct.CellType.EMPTY, self.m_cell_size) for x in range(self.m_cols)]
            for y in range(self.m_rows)
        ]
        self.m_cells[0][0].set_type(gct.CellType.START)
        self.m_cells[len(self.m_cells) - 1][len(self.m_cells[0]) - 1].set_type(gct.CellType.END)

    def clear(self):
        """
        Supprime le rendu de la resolution et remise a zero des parametres
        """
        for y in range(len(self.master.m_grid.m_cells)):
            for x in range(len(self.master.m_grid.m_cells[0])):
                self.m_cells[y][x].reset()

        history = self.find_withtag("history")

        for item in history:
            self.delete(item)

    def reset(self):
        """
        Reinitialise les cellules (suppression des murs et remise a zero des parametres)
        """
        for y in range(len(self.master.m_grid.m_cells)):
            for x in range(len(self.master.m_grid.m_cells[0])):
                self.m_cells[y][x].reset()
                if self.m_cells[y][x].m_type == gct.CellType.WALL:
                    self.m_cells[y][x].set_type(gct.CellType.EMPTY)

    def enable_event(self):
        self.m_event_manager.enable_event()

    def disable_event(self):
        self.m_event_manager.disable_event()
