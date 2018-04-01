from tkinter import Frame, Label, font, W, E


class InformationsDisplayer(Frame):

    WIDTH = 250
    HEIGHT = 150

    COLOR = {"background": "#29323a", "foreground": "#f1f1f1", "hover": "#dbd9d9", "error": "#f24d4d"}
    FONT = {"title": "Lobster", "main": "Open Sans"}
    SIZE = {"large": 12, "medium": 10, "small": 8}

    def __init__(self, root):
        """
        Constructeur

        :param root: Racine pour l'integration a l'interface

        :type root: Frame
        """
        super().__init__(root)
        self.setup_frame()

        self.build_title()
        self.m_operations = self.build_operations_count_label()
        self.m_time = self.build_time_label()

    def setup_frame(self):
        """
        Initialise la fenetre du menu
        """
        self.configure(
            width=InformationsDisplayer.WIDTH,
            height=InformationsDisplayer.HEIGHT,
            background=InformationsDisplayer.COLOR["background"]
        )
        self.pack_propagate(0)
        self.grid_propagate(0)
        self.grid_columnconfigure(1, weight=1)

    def build_title(self):
        """
        Construit le titre du menu
        """
        title = Label(self, text="Informations")
        title.configure(
            font=font.Font(
                family=InformationsDisplayer.FONT["title"],
                size=22
            ),
            background="#333E47",
            foreground=InformationsDisplayer.COLOR["foreground"]
        )
        title.grid(columnspan=2, sticky=W+E, pady=10)

    def build_operations_count_label(self):
        """
        Construit le Label pour afficher le nombre d'operation effectue

        :return: Label
        """
        label = Label(self, text="Nombre d'operation :")
        label.configure(
            font=font.Font(
                family=InformationsDisplayer.FONT["main"],
                size=InformationsDisplayer.SIZE["small"]
            ),
            background=InformationsDisplayer.COLOR["background"],
            foreground=InformationsDisplayer.COLOR["foreground"]
        )
        label.grid(sticky=W, padx=5)

        text = Label(self, text="0")
        text.configure(
            font=font.Font(
                family=InformationsDisplayer.FONT["main"],
                size=InformationsDisplayer.SIZE["small"]
            ),
            background=InformationsDisplayer.COLOR["background"],
            foreground=InformationsDisplayer.COLOR["foreground"]
        )
        text.grid(row=1, column=1, sticky=E, padx=5)

        return text

    def build_time_label(self):
        """
        Construit le Label pour afficher le temps d'execution

        :return: Label
        """
        label = Label(self, text="Temps (ms) :")
        label.configure(
            font=font.Font(
                family=InformationsDisplayer.FONT["main"],
                size=InformationsDisplayer.SIZE["small"]
            ),
            background=InformationsDisplayer.COLOR["background"],
            foreground=InformationsDisplayer.COLOR["foreground"]
        )
        label.grid(sticky=W, padx=5)

        text = Label(self, text="0")
        text.configure(
            font=font.Font(
                family=InformationsDisplayer.FONT["main"],
                size=InformationsDisplayer.SIZE["small"]
            ),
            background=InformationsDisplayer.COLOR["background"],
            foreground=InformationsDisplayer.COLOR["foreground"]
        )
        text.grid(row=2, column=1, sticky=E, padx=5)

        return text

    def set_time(self, temps):
        """
        Change le texte du temps d'execution

        :param temps: Nouveau temps d'execution

        :type temps: double
        """
        self.m_time.configure(text="{:f}".format(temps * 1000))

    def set_operations(self, operations):
        """
        Change le texte du nombre d'operation

        :param operations: Nouveau nombre d'operations

        :type operations: double
        """
        self.m_operations.configure(text=operations)