from tkinter import Frame, Label, font

from gui.config import Config


class InformationsDisplayer(Frame):

    WIDTH = 250

    def __init__(self, root):
        """
        Constructeur

        :param root: Racine pour l'integration a l'interface

        :type root: Tk
        """
        super().__init__(root)
        self.config_frame()

        self.build_title()
        self.m_operations = self.build_operations_label()
        self.m_time = self.build_time_label()

    def config_frame(self):
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
        title = Label(self, text="Informations")
        title.configure(
            font=font.Font(
                family=Config.FONT["title"],
                size=Config.SIZE["x-large"]
            ),
            background=Config.COLOR["title-bg"],
            foreground=Config.COLOR["title-fg"]
        )
        title.grid(columnspan=2, sticky='we', pady=10)

    def build_operations_label(self):
        """
        Construit le Label pour afficher le nombre d'operation effectue

        :return: Label
        """
        label = Label(self, text="Nombre d'operation :")
        label.configure(
            font=font.Font(
                family=Config.FONT["main"],
                size=Config.SIZE["medium"]
            ),
            background=Config.COLOR["main-bg"],
            foreground=Config.COLOR["main-fg"]
        )
        label.grid(sticky='w', padx=10)

        text = Label(self, text="0")
        text.configure(
            font=font.Font(
                family=Config.FONT["main"],
                size=Config.SIZE["medium"]
            ),
            background=Config.COLOR["main-bg"],
            foreground=Config.COLOR["main-fg"]
        )
        text.grid(row=1, column=1, sticky='e', padx=10)

        return text

    def build_time_label(self):
        """
        Construit le Label pour afficher le temps d'execution

        :return: Label
        """
        label = Label(self, text="Temps (ms) :")
        label.configure(
            font=font.Font(
                family=Config.FONT["main"],
                size=Config.SIZE["medium"]
            ),
            background=Config.COLOR["main-bg"],
            foreground=Config.COLOR["main-fg"]
        )
        label.grid(sticky='w', padx=10)

        text = Label(self, text="0")
        text.configure(
            font=font.Font(
                family=Config.FONT["main"],
                size=Config.SIZE["medium"]
            ),
            background=Config.COLOR["main-bg"],
            foreground=Config.COLOR["main-fg"]
        )
        text.grid(row=2, column=1, sticky='e', padx=10)

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