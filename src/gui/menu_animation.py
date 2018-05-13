from tkinter import Frame, Label, font, Scale, Button, DISABLED, ACTIVE

from gui.config import Config


class MenuAnimation(Frame):

    def __init__(self, root):
        """
        Constructeur

        :param root: Fenetre racine

        :type root: Tk
        """
        super().__init__(root)
        self.config_frame()

        self.build_title()
        self.m_scale = self.build_speed_scale()
        self.m_play_button = self.build_play_pause_button()
        self.m_stop_button = self.build_stop_button()

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
        title = Label(self, text="Animation")
        title.configure(
            font=font.Font(
                family=Config.FONT["title"],
                size=Config.SIZE["x-large"]
            ),
            background=Config.COLOR["title-bg"],
            foreground=Config.COLOR["title-fg"]
        )
        title.grid(sticky='we', pady=10)

    def build_speed_scale(self):
        """
        Construit la barre de reglage de la vitesse d'animation

        :return: Scale
        """
        speed_label = Label(self, text="Vitesse")
        speed_label.configure(
            font=font.Font(
                family=Config.FONT["main"],
                size=Config.SIZE["large"]
            ),
            background=Config.COLOR["main-bg"],
            foreground=Config.COLOR["main-fg"]
        )
        speed_label.grid(sticky='w', padx=10)

        scale = Scale(self, from_=-1, to=1, resolution=0.1, tickinterval=0.5, command=self.on_move_scale)
        scale.configure(
            length=Config.LEFT_MENU_WIDTH - 10,
            orient='horizontal',
            font=font.Font(
                family=Config.FONT["main"],
                size=Config.SIZE["small"]
            ),
            background=Config.COLOR["main-bg"],
            foreground=Config.COLOR["main-fg"],
            activebackground=Config.COLOR["main-bg"],
            troughcolor=Config.COLOR["main-fg"],
            highlightthickness=0
        )
        scale.set(1)
        scale.grid(padx=10)

        return scale

    def build_play_pause_button(self):
        """
        Construit le bouton mettre l'animation en play/pause

        :return: Button
        """
        btn = Button(self, text="Pause", command=self.on_click_play_pause)
        btn.configure(
            font=font.Font(
                family=Config.FONT["main"],
                size=Config.SIZE["medium"]
            ),
            background=Config.COLOR["btn-bg"],
            foreground=Config.COLOR["btn-fg"],
            cursor="hand2",
            state=DISABLED
        )
        btn.grid(sticky='we', padx=10, pady=(20, 10))

        return btn

    def build_stop_button(self):
        """
        Construit le bouton arreter l'animation en cours

        :return: Button
        """
        btn = Button(self, text="Stop", command=self.on_click_stop)
        btn.configure(
            font=font.Font(
                family=Config.FONT["main"],
                size=Config.SIZE["medium"]
            ),
            background=Config.COLOR["btn-bg"],
            foreground=Config.COLOR["btn-fg"],
            cursor="hand2",
            state=DISABLED
        )
        btn.grid(sticky='we', padx=10)

        return btn

    def on_move_scale(self, speed):
        """
        Change la vitesse d'animation

        :param speed: Vitesse d'animation

        :type speed: double
        """
        self.master.m_menu.m_history_interpreter.set_animation_speed(speed)

    def on_click_play_pause(self):
        """
        Met l'animation en play/pause et change le texte du bouton
        """
        self.master.m_menu.m_history_interpreter.toggle_pause()

        self.m_play_button.configure(text={
            "Play": "Pause",
            "Pause": "Play"
        }[self.m_play_button.cget("text")])

    def on_click_stop(self):
        """
        Arrete l'animation en cours
        """
        self.m_play_button.configure(text="Pause")
        self.set_buttons_state(DISABLED)

        self.master.m_menu.m_history_interpreter.stop()
        self.master.m_menu.set_buttons_state(ACTIVE)
        self.master.m_grid.enable_event()

    def set_buttons_state(self, state):
        """
        Change l'etat des boutons

        :param state: Etat des boutons

        :type state: ACTIVE, DISABLED
        """
        self.m_play_button.configure(state=state)
        self.m_stop_button.configure(state=state)
