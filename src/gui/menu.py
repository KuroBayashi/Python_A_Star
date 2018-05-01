from tkinter import Frame, Label, font, Radiobutton, IntVar, Checkbutton, Button, DISABLED, ACTIVE

from algorithms.a_star.a_star import AStar
from algorithms.a_star.exception_path_not_found import ExceptionPathNotFound
from algorithms.a_star.heuristic import Heuristic

from gui.cell_type import CellType
from gui.config import Config
from gui.history_interpreter import HistoryInterpreter
from gui.menu_event_manager import MenuEventManager

from history.history import History


class Menu(Frame):

    ALGORITHMS = ["A*", "Dijkstra"]
    HEURISTICS = ["Manhattan", "Chebyshev", "Euclidien", "Octile"]
    OPTIONS = ["Autoriser les diagonales"]

    def __init__(self, root):
        """
        Constructeur

        :param root : Fenetre racine

        :type root: Tk
        """
        super().__init__(root)
        self.setup_frame()

        self.build_title()
        self.m_algorithms_list = self.build_algorithms_list()
        self.m_heuristics_list = self.build_heuristics_list()
        self.m_options_list = self.build_options_list()
        self.m_message = self.build_message()
        self.m_start_button = self.build_start_button()
        self.m_reset_button = self.build_reset_button()

        self.m_event_manager = MenuEventManager(self)

        self.m_history = History()
        self.m_history_interpreter = HistoryInterpreter(self.m_history, self.master.m_grid)

    def setup_frame(self):
        """
        Initialise la fenetre du menu
        """
        self.configure(
            background=Config.COLOR["main-bg"]
        )
        self.grid_propagate(0)
        self.columnconfigure(0, weight=1)

    def build_title(self):
        """
        Construit le titre du menu
        """
        # Label
        title = Label(self, text="Resolution")
        title.configure(
            font=font.Font(
                family=Config.FONT["title"],
                size=22
            ),
            background=Config.COLOR["title-bg"],
            foreground=Config.COLOR["title-fg"]
        )
        title.grid(sticky='we', pady=10)

    def build_algorithms_list(self):
        """
        Construit la liste des algorithmes disponibles

        :return: IntVar - Identifiant unique de la liste des algorithmes
        """
        # Label
        algo_label = Label(self, text="Choix de l'algorithme")
        algo_label.configure(
            font=font.Font(
                family=Config.FONT["main"],
                size=Config.SIZE["large"]
            ),
            background=Config.COLOR["main-bg"],
            foreground=Config.COLOR["main-fg"]
        )
        algo_label.grid(sticky='w', padx=10)

        # Radio buttons
        x = IntVar(value=1)

        for index, text in enumerate(Menu.ALGORITHMS):
            rdo = Radiobutton(self, text=text, variable=x, value=index+1, tristatevalue=0)
            rdo.configure(
                font=font.Font(
                    family=Config.FONT["main"],
                    size=Config.SIZE["medium"]
                ),
                background=Config.COLOR["main-bg"],
                foreground=Config.COLOR["main-fg"],
                activebackground=Config.COLOR["main-bg"],
                activeforeground=Config.COLOR["main-fg"],
                selectcolor=Config.COLOR["main-bg"]
            )
            rdo.grid(sticky='w', padx=20)

        return x

    def build_heuristics_list(self):
        """
        Construit la liste des heuristiques disponibles

        :return: IntVar - Identifiant de la liste des boutons
        """
        # Label
        heuristic_label = Label(self, text="Choix de l'heuristique")
        heuristic_label.configure(
            font=font.Font(
                family=Config.FONT["main"],
                size=Config.SIZE["large"]
            ),
            background=Config.COLOR["main-bg"],
            foreground=Config.COLOR["main-fg"]
        )
        heuristic_label.grid(sticky='w', padx=10)

        # Radio buttons
        x = IntVar(value=1)

        for index, text in enumerate(Menu.HEURISTICS):
            rdo = Radiobutton(self, text=text, variable=x, value=index+1, tristatevalue=0)
            rdo.configure(
                font=font.Font(
                    family=Config.FONT["main"],
                    size=Config.SIZE["medium"]
                ),
                background=Config.COLOR["main-bg"],
                foreground=Config.COLOR["main-fg"],
                activebackground=Config.COLOR["main-bg"],
                activeforeground=Config.COLOR["main-fg"],
                selectcolor=Config.COLOR["main-bg"]
            )
            rdo.grid(sticky='w', padx=20)

        return x

    def build_options_list(self):
        """
        Construit la liste des options disponibles

        :return: list(IntVar) - Liste contenant les identifiants des options
        """
        # Label
        opt_label = Label(self, text="Options")
        opt_label.configure(
            font=font.Font(
                family=Config.FONT["main"],
                size=Config.SIZE["large"]
            ),
            background=Config.COLOR["main-bg"],
            foreground=Config.COLOR["main-fg"]
        )
        opt_label.grid(sticky='w', padx=10)

        # Checkbox
        opt_list = []

        for text in Menu.OPTIONS:
            x = IntVar()
            ckb = Checkbutton(self, text=text, variable=x, tristatevalue=0)
            ckb.configure(
                font=font.Font(
                    family=Config.FONT["main"],
                    size=Config.SIZE["medium"]
                ),
                background=Config.COLOR["main-bg"],
                foreground=Config.COLOR["main-fg"],
                activebackground=Config.COLOR["main-bg"],
                activeforeground=Config.COLOR["main-fg"],
                selectcolor=Config.COLOR["main-bg"]
            )
            ckb.grid(sticky='w', padx=20)
            opt_list.append(x)

        return opt_list

    def build_message(self):
        """
        Construit le Label pour afficher un message retour a l'utilisateur

        :return: Label - Identifiant unique du Label
        """
        message = Label(self, text="")
        message.configure(
            font=font.Font(
                family=Config.FONT["main"],
                size=Config.SIZE["large"]
            ),
            background=Config.COLOR["main-bg"],
            foreground=Config.COLOR["error"]
        )
        message.grid(sticky='we', padx=10, pady=10)

        return message

    def build_start_button(self):
        """
        Construit le bouton pour lancer la resolution

        :return: Button - Identifiant unique du bouton
        """
        btn = Button(self, text="START", command=self.on_click_start)
        btn.configure(
            font=font.Font(
                family=Config.FONT["main"],
                size=Config.SIZE["large"],
                weight="bold"
            ),
            background=Config.COLOR["btn-bg"],
            foreground=Config.COLOR["btn-fg"],
            cursor="hand2"
        )
        btn.grid(sticky='we', padx=10, pady=10)

        return btn

    def build_reset_button(self):
        """
        Construit le bouton pour reinitialiser la grille

        :return: Button - Identifiant unique du bouton
        """
        btn = Button(self, text="Clear Wall", command=self.on_click_clear_wall)
        btn.configure(
            font=font.Font(
                family=Config.FONT["main"],
                size=Config.SIZE["medium"]
            ),
            background=Config.COLOR["btn-bg"],
            foreground=Config.COLOR["btn-fg"],
            cursor="hand2"
        )
        btn.grid(sticky='we', padx=10)

        return btn

    def on_click_start(self):
        """
        Lance la resolution et la previsualisation
        """
        # Buttons state
        self.set_buttons_state(DISABLED)
        self.master.m_menu_animation.set_buttons_state(ACTIVE)
        self.master.m_grid.disable_event()

        # Animation speed
        if self.master.m_menu_animation.m_scale.get() <= 0:
            self.master.m_menu_animation.m_scale.set(1)

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
            self.set_buttons_state(ACTIVE)
            self.master.m_menu_animation.set_buttons_state(DISABLED)
            self.master.m_grid.enable_event()

    def on_click_clear_path(self):
        """
        Supprime le rendu de la precedente resolution
        """
        self.master.m_grid.clear()

    def on_click_clear_wall(self):
        """
        Supprime le rendu de la precedente resolution, supprime tous les murs, et remet les valeurs des cellules a 0
        """
        self.on_click_clear_path()
        self.master.m_grid.reset()

    def set_buttons_state(self, state):
        """
        Change l'etat des boutons

        :param state: Etat des boutons

        :type state: ACTIVE, DISABLED
        """
        self.m_start_button.configure(state=state)
        self.m_reset_button.configure(state=state)

    def stop(self):
        self.m_history_interpreter.stop()
