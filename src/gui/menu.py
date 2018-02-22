from tkinter import Frame, Label, Y, RIGHT, E, W, font, Radiobutton, IntVar, Checkbutton, Button

from gui.menu_event_manager import MenuEventManager


class Menu(Frame):

    WIDTH = 250

    COLOR_BG = "#29323a"
    COLOR_FG = "#f1f1f1"
    COLOR_HV = "#dbd9d9"
    FONT_TITLE = "Lobster"
    FONT_MAIN = "Open Sans"

    def build_title(self):
        title = Label(self, text="Menu")
        title.configure(font=font.Font(family=Menu.FONT_TITLE, size=22))
        title.configure(background="#333E47", foreground=Menu.COLOR_FG)
        title.grid(sticky=W + E, pady=10)

        return title

    def build_algorithms_list(self):
        # Label
        algo_label = Label(self, text="Choix de l'algorithme : ")
        algo_label.configure(font=font.Font(family=Menu.FONT_MAIN, size=12))
        algo_label.configure(background=Menu.COLOR_BG, foreground=Menu.COLOR_FG)
        algo_label.grid(sticky=W, padx=5)

        # Radio buttons
        algo_list = []
        algo_list_def = [("Dijkstra", "1"), ("A*", "2")]
        x = IntVar(value=42)

        for text, value in algo_list_def:
            rdo = Radiobutton(self, text=text, variable=x, value=value, tristatevalue=0)
            rdo.configure(font=font.Font(family=Menu.FONT_MAIN, size=10))
            rdo.configure(background=Menu.COLOR_BG, foreground=Menu.COLOR_FG, selectcolor=Menu.COLOR_BG)
            rdo.configure(activebackground=Menu.COLOR_BG, activeforeground=Menu.COLOR_FG)
            rdo.grid(sticky=W, padx=20)
            algo_list.append(rdo)

        return algo_label, algo_list

    def build_heuristics_list(self):
        # Label
        heuristic_label = Label(self, text="Choix de l'heuristique : ")
        heuristic_label.configure(font=font.Font(family=Menu.FONT_MAIN, size=12))
        heuristic_label.configure(background=Menu.COLOR_BG, foreground=Menu.COLOR_FG)
        heuristic_label.grid(sticky=W, padx=5)

        # Radio buttons
        heuristic_list = []
        heuristic_list_def = [("Manhattan", "1"), ("Chebyshev", "2"), ("Euclidien", "3"), ("Octile", "4")]
        x = IntVar(value=13)

        for text, value in heuristic_list_def:
            rdo = Radiobutton(self, text=text, variable=x, value=value, tristatevalue=0)
            rdo.configure(font=font.Font(family=Menu.FONT_MAIN, size=10))
            rdo.configure(background=Menu.COLOR_BG, foreground=Menu.COLOR_FG, selectcolor=Menu.COLOR_BG)
            rdo.configure(activebackground=Menu.COLOR_BG, activeforeground=Menu.COLOR_FG)
            rdo.grid(sticky=W, padx=20)
            heuristic_list.append(rdo)

        return heuristic_label, heuristic_list

    def build_options_list(self):
        # Options
        opt_label = Label(self, text="Options : ")
        opt_label.configure(font=font.Font(family=Menu.FONT_MAIN, size=12))
        opt_label.configure(background=Menu.COLOR_BG, foreground=Menu.COLOR_FG)
        opt_label.grid(sticky=W, padx=5)

        # Checkbox
        opt_list = []
        opt_list_def = [("Autoriser les diagonales", "1")]
        x = IntVar(value=13)

        for text, value in opt_list_def:
            ckb = Checkbutton(self, text=text, variable=x, tristatevalue=0)
            ckb.configure(font=font.Font(family=Menu.FONT_MAIN, size=10))
            ckb.configure(background=Menu.COLOR_BG, foreground=Menu.COLOR_FG, selectcolor=Menu.COLOR_BG)
            ckb.configure(activebackground=Menu.COLOR_BG, activeforeground=Menu.COLOR_FG)
            ckb.grid(sticky=W, padx=20)
            opt_list.append(ckb)

        return opt_label, opt_list

    def build_start_button(self):
        # Button
        btn = Button(self, text="START")
        btn.configure(font=font.Font(family=Menu.FONT_MAIN, size=12, weight="bold"))
        btn.configure(background=Menu.COLOR_FG, foreground=Menu.COLOR_BG)
        btn.configure(cursor="hand2")
        btn.grid(sticky=W+E, padx=40, pady=30)

        return btn

    def setup_frame(self):
        self.configure(width=Menu.WIDTH)
        self.configure(background=Menu.COLOR_BG)
        self.pack(fill=Y, side=RIGHT)
        self.grid_columnconfigure(0, weight=1)
        self.grid_propagate(0)

    def __init__(self, root):
        super().__init__(root)
        self.setup_frame()

        self.m_title = self.build_title()
        self.m_algorithms_label, self.m_algorithms_list = self.build_algorithms_list()
        self.m_heuristics_label, self.m_heuristics_list = self.build_heuristics_list()
        self.m_options_list = self.build_options_list()
        self.m_start_button = self.build_start_button()

        self.m_event_manager = MenuEventManager(self)

        #self.m_selected_algorithm = self.m_algorithms_list[0]
        #self.m_selected_heuristic = self.m_heuristics_list[0]
        #self.m_selected_diagonal = False
