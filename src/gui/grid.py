from tkinter import Canvas

import gui.cell as gcc
import gui.cell_type as gct
from gui.grid_event_manager import GridEventManager


class Grid(Canvas):

    COLS = 25
    ROWS = 25

    WIDTH = gcc.Cell.WIDTH * COLS + 1  # + 1 pour la bordure droite
    HEIGHT = gcc.Cell.WIDTH * ROWS + 1  # + 1 pour la bordure basse

    def __init__(self, root):
        """
        Constructeur

        :param root : Fenetre racine

        :type root: Tk
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
        self.configure(width=Grid.WIDTH, height=Grid.HEIGHT)
        self.configure(background="#7054b7", highlightthickness=0)
        self.pack_propagate(0)

    def draw_lines(self):
        """
        Dessine les lignes de la grille
        """
        for i in range(Grid.ROWS):
            self.create_line(0, i * gcc.Cell.WIDTH, Grid.WIDTH, i * gcc.Cell.WIDTH)
        for j in range(Grid.COLS):
            self.create_line(j * gcc.Cell.WIDTH, 0,  j * gcc.Cell.WIDTH, Grid.HEIGHT)

    def build_cells(self):
        """
        Construction des cellules de la grille et positionnement des cellules de départ et d'arrivee
        """
        self.m_cells = [
            [gcc.Cell(self, x, y, gct.CellType.EMPTY) for x in range(Grid.COLS)]
            for y in range(Grid.ROWS)
        ]
        self.m_cells[0][0].set_type(gct.CellType.START)
        self.m_cells[len(self.m_cells) - 1][len(self.m_cells[0]) - 1].set_type(gct.CellType.END)

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

    def enable_event(self):
        self.m_event_manager.enable_event()

    def disable_event(self):
        self.m_event_manager.disable_event()