from tkinter import Frame, Label, E, W, font, Radiobutton, IntVar, Checkbutton, Button, DISABLED, ACTIVE

from algorithms.a_star.a_star import AStar
from algorithms.a_star.exception_path_not_found import ExceptionPathNotFound
from algorithms.a_star.heuristic import Heuristic
from gui.cell_type import CellType
from gui.history_interpreter import HistoryInterpreter
from gui.menu_event_manager import MenuEventManager
from history.history import History


class Menu(Frame):

    WIDTH = 250
    MIN_HEIGHT = 500

    COLOR = {"background": "#29323a", "foreground": "#f1f1f1", "hover": "#dbd9d9", "error": "#f24d4d"}
    FONT = {"title": "Lobster", "main": "Open Sans"}
    SIZE = {"label": 12, "list": 10}

    ALGORITHMS = ["A*", "Dijkstra"]
    HEURISTICS = ["Manhattan", "Chebyshev", "Euclidien", "Octile"]
    OPTIONS = ["Autoriser les diagonales"]

    def __init__(self, root):
        """
        Constructeur

        :param Tk root : Fenetre racine
        """
        super().__init__(root)
        self.setup_frame()

        self.m_title = self.build_title()
        self.m_algorithms_list = self.build_algorithms_list()
        self.m_heuristics_list = self.build_heuristics_list()
        self.m_options_list = self.build_options_list()
        self.m_message = self.build_message()
        self.m_start_button = self.build_start_button()
        self.m_reset_button = self.build_reset_button()
        self.m_clear_button = self.build_clear_button()

        self.m_event_manager = MenuEventManager(self)

        self.m_history = History()
        self.m_history_interpreter = HistoryInterpreter(self.m_history, self.master.m_grid)

    def setup_frame(self):
        """
        Initialise la fenetre du menu
        """
        self.configure(width=Menu.WIDTH)
        self.configure(background=Menu.COLOR["background"])
        self.pack_propagate(0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_propagate(0)

    def build_title(self):
        """
        Construit le titre du menu

        :return Label : Identifiant unique du titre
        """
        # Label
        title = Label(self, text="Resolution")
        title.configure(font=font.Font(family=Menu.FONT["title"], size=22))
        title.configure(background="#333E47", foreground=Menu.COLOR["foreground"])
        title.grid(sticky=W+E, pady=10)

        return title

    def build_algorithms_list(self):
        """
        Construit la liste des algorithmes disponibles

        :return (Label, IntVar) : Tuple contenant l'identifiant unique du Label, et de la liste des boutons Radio
        """
        # Label
        algo_label = Label(self, text="Choix de l'algorithme")
        algo_label.configure(font=font.Font(family=Menu.FONT["main"], size=Menu.SIZE["label"]))
        algo_label.configure(background=Menu.COLOR["background"], foreground=Menu.COLOR["foreground"])
        algo_label.grid(sticky=W, padx=5)

        # Radio buttons
        x = IntVar(value=1)

        for index, text in enumerate(Menu.ALGORITHMS):
            rdo = Radiobutton(self, text=text, variable=x, value=index+1, tristatevalue=0)
            rdo.configure(font=font.Font(family=Menu.FONT["main"], size=Menu.SIZE["list"]))
            rdo.configure(background=Menu.COLOR["background"], foreground=Menu.COLOR["foreground"])
            rdo.configure(activebackground=Menu.COLOR["background"], activeforeground=Menu.COLOR["foreground"])
            rdo.configure(selectcolor=Menu.COLOR["background"])
            rdo.grid(sticky=W, padx=20)

        return x

    def build_heuristics_list(self):
        """
        Construit la liste des heuristiques disponibles

        :return (Label, IntVar) : Tuple contenant l'identifiant unique du Label, et de la liste des boutons Radio
        """
        # Label
        heuristic_label = Label(self, text="Choix de l'heuristique")
        heuristic_label.configure(font=font.Font(family=Menu.FONT["main"], size=Menu.SIZE["label"]))
        heuristic_label.configure(background=Menu.COLOR["background"], foreground=Menu.COLOR["foreground"])
        heuristic_label.grid(sticky=W, padx=5)

        # Radio buttons
        x = IntVar(value=1)

        for index, text in enumerate(Menu.HEURISTICS):
            rdo = Radiobutton(self, text=text, variable=x, value=index+1, tristatevalue=0)
            rdo.configure(font=font.Font(family=Menu.FONT["main"], size=Menu.SIZE["list"]))
            rdo.configure(background=Menu.COLOR["background"], foreground=Menu.COLOR["foreground"])
            rdo.configure(activebackground=Menu.COLOR["background"], activeforeground=Menu.COLOR["foreground"])
            rdo.configure(selectcolor=Menu.COLOR["background"])
            rdo.grid(sticky=W, padx=20)

        return x

    def build_options_list(self):
        """
        Construit la liste des options disponibles

        :return (Label, List(IntVar)) : Tuple contenant l'identifiant unique du Label, et une liste de ceux des options
        """
        # Label
        opt_label = Label(self, text="Options")
        opt_label.configure(font=font.Font(family=Menu.FONT["main"], size=Menu.SIZE["label"]))
        opt_label.configure(background=Menu.COLOR["background"], foreground=Menu.COLOR["foreground"])
        opt_label.grid(sticky=W, padx=5)

        # Checkbox
        opt_list = []

        for text in Menu.OPTIONS:
            x = IntVar()
            ckb = Checkbutton(self, text=text, variable=x, tristatevalue=0)
            ckb.configure(font=font.Font(family=Menu.FONT["main"], size=Menu.SIZE["list"]))
            ckb.configure(background=Menu.COLOR["background"], foreground=Menu.COLOR["foreground"])
            ckb.configure(activebackground=Menu.COLOR["background"], activeforeground=Menu.COLOR["foreground"])
            ckb.configure(selectcolor=Menu.COLOR["background"])
            ckb.grid(sticky=W, padx=20)
            opt_list.append(x)

        return opt_list

    def build_message(self):
        """
        Construit le Label pour afficher un message retour a l'utilisateur

        :return Label : Identifiant unique du Label
        """
        message = Label(self, text="")
        message.configure(font=font.Font(family=Menu.FONT["main"], size=Menu.SIZE["label"]))
        message.configure(background=Menu.COLOR["background"], foreground=Menu.COLOR["error"])
        message.grid(sticky=W+E, padx=5, pady=10)

        return message

    def build_start_button(self):
        """
        Construit le bouton pour lancer la resolution

        :return Button : Identifiant unique du bouton
        """
        btn = Button(self, text="START", command=self.on_click_start)
        btn.configure(font=font.Font(family=Menu.FONT["main"], size=Menu.SIZE["label"], weight="bold"))
        btn.configure(background=Menu.COLOR["foreground"], foreground=Menu.COLOR["background"])
        btn.configure(cursor="hand2", width=20)
        btn.place(x=20, y=420)

        return btn

    def build_reset_button(self):
        """
        Construit le bouton pour reinitialiser la grille

        :return Button : Identifiant unique du bouton
        """
        btn = Button(self, text="Clear Wall", command=self.on_click_clear_wall)
        btn.configure(font=font.Font(family=Menu.FONT["main"], size=8))
        btn.configure(background=Menu.COLOR["foreground"], foreground=Menu.COLOR["background"])
        btn.configure(cursor="hand2", width=15)
        btn.place(x=20, y=470)

        return btn

    def build_clear_button(self):
        """
        Construit le bouton pour supprimer la visualisation de la precedente resolution

        :return Button : Identifiant unique du bouton
        """
        btn = Button(self, text="Clear Path", command=self.on_click_clear_path)
        btn.configure(font=font.Font(family=Menu.FONT["main"], size=8))
        btn.configure(background=Menu.COLOR["foreground"], foreground=Menu.COLOR["background"])
        btn.configure(cursor="hand2", width=15)
        btn.place(anchor="ne", x=230, y=470)

        return btn

    def on_click_start(self):
        """
        Lance la resolution et la previsualisation
        """
        # Button state
        self.m_start_button.configure(state=DISABLED)
        self.m_clear_button.configure(state=DISABLED)
        self.m_reset_button.configure(state=DISABLED)
        self.master.m_menu_animation.m_play_button.configure(state=ACTIVE)
        self.master.m_menu_animation.m_stop_button.configure(state=ACTIVE)
        self.master.m_grid.unbind("<ButtonPress-1>")
        self.master.m_grid.unbind("<ButtonRelease-1>")

        # Clear
        self.on_click_clear_path()
        self.m_message.configure(text="")

        # Heuristic
        heuristics = [Heuristic.manhattan, Heuristic.chebyshev, Heuristic.euclidean, Heuristic.octile]
        heuristic = heuristics[self.m_heuristics_list.get() - 1]

        # Options
        options = [bool(opt.get()) for opt in self.m_options_list]

        # History
        self.m_history.clear()

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
        try:
            if self.m_algorithms_list.get() == self.ALGORITHMS.index("A*") + 1:
                a_star = AStar(self.master.m_grid, self.m_history, heuristic, options[0])
            else:
                a_star = AStar(self.master.m_grid, self.m_history, Heuristic.dijkstra, options[0])

            a_star.run(start, end)

            self.m_history_interpreter.set_animation_speed(self.master.m_menu_animation.m_scale.get())
            self.m_history_interpreter.run(True)
        except ExceptionPathNotFound as e:
            self.m_message.configure(text=e.m_message)
            self.m_start_button.configure(state=ACTIVE)
            self.m_clear_button.configure(state=ACTIVE)
            self.m_reset_button.configure(state=ACTIVE)
            self.master.m_menu_animation.m_play_button.configure(state=DISABLED)
            self.master.m_menu_animation.m_stop_button.configure(state=DISABLED)
            self.master.m_grid.bind("<ButtonPress-1>", self.master.m_grid.m_event_manager.on_mouse_down)
            self.master.m_grid.bind("<ButtonRelease-1>", self.master.m_grid.m_event_manager.on_mouse_up)

    def on_click_clear_path(self):
        """
        Supprime le rendu de la precedente resolution,
        """
        self.master.m_grid.clear()

    def on_click_clear_wall(self):
        """
        Supprime le rendu de la precedente resolution, supprime tous les murs, et remet les valeurs des cellules a 0
        """
        self.on_click_clear_path()
        self.master.m_grid.reset()
