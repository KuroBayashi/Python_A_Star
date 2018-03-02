from tkinter import Canvas, BOTH

import gui.cell as gcc
import gui.cell_type as gct
from gui.grid_event_manager import GridEventManager


class Grid(Canvas):

    def __init__(self, root):
        """
        Constructeur

        :param Tk root : Fenetre racine
        """
        super().__init__(root)
        self.setup_canvas()

        self.m_cells = []
        self.m_event_manager = GridEventManager(self)

        self.build_cells()
        self.draw_lines()

    def setup_canvas(self):
        """
        Initialise le canvas
        """
        self.configure(background="#f1f1f1", highlightthickness=0)
        self.pack(expand=True, fill=BOTH, padx=5, pady=5)
        self.update()

    def draw_lines(self):
        """
        Dessine les lignes de la grille
        """
        self.update()

        for i in range(0, self.winfo_width(), gcc.Cell.WIDTH):
            self.create_line(0, i, self.winfo_width(), i)
        for j in range(0, self.winfo_height(), gcc.Cell.WIDTH):
            self.create_line(j, 0,  j, self.winfo_height())

    def build_cells(self):
        """
        Construction des cellules de la grille et positionnement des cellules de départ et d'arrivee
        """
        self.m_cells = [
            [gcc.Cell(self, x, y, gct.CellType.EMPTY) for x in range(self.winfo_width() // gcc.Cell.WIDTH)]
            for y in range(self.winfo_height() // gcc.Cell.WIDTH)
        ]
        self.m_cells[1][1].set_type(gct.CellType.START)
        self.m_cells[len(self.m_cells) - 2][len(self.m_cells[0]) - 2].set_type(gct.CellType.END)

    def clear(self):
        """
        Supprime le rendu de la resolution
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
