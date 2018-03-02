from tkinter import Frame, Label, Y, RIGHT, E, W, font, Radiobutton, IntVar, Checkbutton, Button

from algorithms.a_star.a_star import AStar
from algorithms.a_star.exception_path_not_found import ExceptionPathNotFound
from algorithms.a_star.heuristic import Heuristic
from gui.cell_type import CellType
from gui.history_interpreter import HistoryInterpreter
from gui.menu_event_manager import MenuEventManager
from history.history import History


class Menu(Frame):

    WIDTH = 250

    COLOR_BG = "#29323a"
    COLOR_FG = "#f1f1f1"
    COLOR_HV = "#dbd9d9"
    FONT_TITLE = "Lobster"
    FONT_MAIN = "Open Sans"

    def __init__(self, root):
        """
        Constructeur

        :param Tk root : Fenetre racine
        """
        super().__init__(root)
        self.setup_frame()

        self.m_title = self.build_title()
        self.m_algorithms_label, self.m_algorithms_list = self.build_algorithms_list()
        self.m_heuristics_label, self.m_heuristics_list = self.build_heuristics_list()
        self.m_options_label, self.m_options_list = self.build_options_list()
        self.m_start_button = self.build_start_button()
        self.m_reset_button = self.build_reset_button()
        self.m_clear_button = self.build_clear_button()

        self.m_event_manager = MenuEventManager(self)

    def setup_frame(self):
        """
        Initialise la fenetre du menu
        """
        self.configure(width=Menu.WIDTH)
        self.configure(background=Menu.COLOR_BG)
        self.pack(fill=Y, side=RIGHT)
        self.grid_columnconfigure(0, weight=1)
        self.grid_propagate(0)

    def build_title(self):
        """
        Construit le titre du menu

        :return Label : Identifiant unique du titre
        """
        # Label
        title = Label(self, text="Menu")
        title.configure(font=font.Font(family=Menu.FONT_TITLE, size=22))
        title.configure(background="#333E47", foreground=Menu.COLOR_FG)
        title.grid(sticky=W + E, pady=10)

        return title

    def build_algorithms_list(self):
        """
        Construit la liste des algorithmes disponibles

        :return (Label, IntVar) : Tuple contenant l'identifiant unique du Label, et de la liste des boutons Radio
        """
        # Label
        algo_label = Label(self, text="Choix de l'algorithme")
        algo_label.configure(font=font.Font(family=Menu.FONT_MAIN, size=12))
        algo_label.configure(background=Menu.COLOR_BG, foreground=Menu.COLOR_FG)
        algo_label.grid(sticky=W, padx=5)

        # Radio buttons
        algo_list_def = [("A*", 1), ("Dijkstra", 2)]
        x = IntVar(value=1)

        for text, value in algo_list_def:
            rdo = Radiobutton(self, text=text, variable=x, value=value, tristatevalue=0)
            rdo.configure(font=font.Font(family=Menu.FONT_MAIN, size=10))
            rdo.configure(background=Menu.COLOR_BG, foreground=Menu.COLOR_FG, selectcolor=Menu.COLOR_BG)
            rdo.configure(activebackground=Menu.COLOR_BG, activeforeground=Menu.COLOR_FG)
            rdo.grid(sticky=W, padx=20)

        return algo_label, x

    def build_heuristics_list(self):
        """
        Construit la liste des heuristiques disponibles

        :return (Label, IntVar) : Tuple contenant l'identifiant unique du Label, et de la liste des boutons Radio
        """
        # Label
        heuristic_label = Label(self, text="Choix de l'heuristique")
        heuristic_label.configure(font=font.Font(family=Menu.FONT_MAIN, size=12))
        heuristic_label.configure(background=Menu.COLOR_BG, foreground=Menu.COLOR_FG)
        heuristic_label.grid(sticky=W, padx=5)

        # Radio buttons
        heuristic_list_def = [("Manhattan", 1), ("Chebyshev", 2), ("Euclidien", 3), ("Octile", 4)]
        x = IntVar(value=1)

        for text, value in heuristic_list_def:
            rdo = Radiobutton(self, text=text, variable=x, value=value, tristatevalue=0)
            rdo.configure(font=font.Font(family=Menu.FONT_MAIN, size=10))
            rdo.configure(background=Menu.COLOR_BG, foreground=Menu.COLOR_FG, selectcolor=Menu.COLOR_BG)
            rdo.configure(activebackground=Menu.COLOR_BG, activeforeground=Menu.COLOR_FG)
            rdo.grid(sticky=W, padx=20)

        return heuristic_label, x

    def build_options_list(self):
        """
        Construit la liste des options disponibles

        :return (Label, List(IntVar)) : Tuple contenant l'identifiant unique du Label, et une liste de ceux des options
        """
        # Label
        opt_label = Label(self, text="Options")
        opt_label.configure(font=font.Font(family=Menu.FONT_MAIN, size=12))
        opt_label.configure(background=Menu.COLOR_BG, foreground=Menu.COLOR_FG)
        opt_label.grid(sticky=W, padx=5)

        # Checkbox
        opt_list = []
        opt_list_def = ["Autoriser les diagonales"]

        for text in opt_list_def:
            x = IntVar()
            ckb = Checkbutton(self, text=text, variable=x, tristatevalue=0)
            ckb.configure(font=font.Font(family=Menu.FONT_MAIN, size=10))
            ckb.configure(background=Menu.COLOR_BG, foreground=Menu.COLOR_FG, selectcolor=Menu.COLOR_BG)
            ckb.configure(activebackground=Menu.COLOR_BG, activeforeground=Menu.COLOR_FG)
            ckb.grid(sticky=W, padx=20)
            opt_list.append(x)

        return opt_label, opt_list

    def build_start_button(self):
        """
        Construit le bouton pour lancer la resolution

        :return Button : Identifiant unique du bouton
        """
        btn = Button(self, text="START", command=self.on_click_start)
        btn.configure(font=font.Font(family=Menu.FONT_MAIN, size=12, weight="bold"))
        btn.configure(background=Menu.COLOR_FG, foreground=Menu.COLOR_BG)
        btn.configure(cursor="hand2", width=20)
        btn.place(x=20, y=410)

        return btn

    def build_reset_button(self):
        """
        Construit le bouton pour reinitialiser la grille

        :return Button : Identifiant unique du bouton
        """
        btn = Button(self, text="Reset", command=self.on_click_reset)
        btn.configure(font=font.Font(family=Menu.FONT_MAIN, size=8))
        btn.configure(background=Menu.COLOR_FG, foreground=Menu.COLOR_BG)
        btn.configure(cursor="hand2", width=15)
        btn.place(x=20, y=470)

        return btn

    def build_clear_button(self):
        """
        Construit le bouton pour supprimer la visualisation de la precedente resolution

        :return Button : Identifiant unique du bouton
        """
        btn = Button(self, text="Clear Path", command=self.on_click_clear)
        btn.configure(font=font.Font(family=Menu.FONT_MAIN, size=8))
        btn.configure(background=Menu.COLOR_FG, foreground=Menu.COLOR_BG)
        btn.configure(cursor="hand2", width=15)
        btn.place(anchor="ne", x=230, y=470)

        return btn

    def on_click_start(self):
        """
        Lance la resolution et la previsualisation
        """
        # Clear
        self.on_click_clear()

        # Heuristic
        heuristics = [Heuristic.manhattan, Heuristic.chebyshev, Heuristic.euclidean, Heuristic.octile]
        heuristic = heuristics[self.m_heuristics_list.get() - 1]

        # Options
        options = [bool(opt.get()) for opt in self.m_options_list]

        # History
        history = History()
        history_interpreter = HistoryInterpreter(history, self.master.m_grid)

        # Start / End nodes
        start = None
        end = None

        for y in range(len(self.master.m_grid.m_cells)):
            for x in range(len(self.master.m_grid.m_cells[0])):
                if self.master.m_grid.m_cells[y][x].m_type == CellType.START:
                    start = self.master.m_grid.m_cells[y][x]
                elif self.master.m_grid.m_cells[y][x].m_type == CellType.END:
                    end = self.master.m_grid.m_cells[y][x]

        # Algorithm
        if self.m_algorithms_list.get() == 1:
            try:
                a_star = AStar(self.master.m_grid, history, heuristic, options[0])
                a_star.run(start, end)
            except ExceptionPathNotFound as e:
                print("A* : ", e.m_message)

            history_interpreter.run()
        else:
            try:
                a_star = AStar(self.master.m_grid, history, Heuristic.dijkstra, options[0])
                a_star.run(start, end)
            except ExceptionPathNotFound as e:
                print("A* : ", e.m_message)

            history_interpreter.run()

    def on_click_clear(self):
        """
        Supprime le rendu de la precedente resolution
        """
        self.master.m_grid.clear()

    def on_click_reset(self):
        """
        Supprime le rendu de la precedente resolution, supprime tous les murs, et remet les valeurs des cellules a 0
        """
        self.on_click_clear()
        self.master.m_grid.reset()
