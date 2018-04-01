from tkinter import Frame, Label, E, W, font, Scale, Button, DISABLED, ACTIVE

from gui.informations_displayer import InformationsDisplayer


class MenuAnimation(Frame):
    WIDTH = 250
    MIN_HEIGHT = 500

    COLOR = {"background": "#29323a", "foreground": "#f1f1f1", "hover": "#dbd9d9", "error": "#f24d4d"}
    FONT = {"title": "Lobster", "main": "Open Sans"}
    SIZE = {"large": 12, "medium": 10, "small": 8}

    def __init__(self, root):
        """
        Constructeur

        :param root : Fenetre racine

        :type root: Tk
        """
        super().__init__(root)
        self.setup_frame()

        self.build_title()
        self.m_scale = self.build_speed_scale()
        self.m_play_button = self.build_play_pause_button()
        self.m_stop_button = self.build_stop_button()

        self.m_informations_displayer = InformationsDisplayer(self)
        self.config_template()

    def setup_frame(self):
        """
        Initialise la fenetre du menu
        """
        self.configure(width=MenuAnimation.WIDTH)
        self.configure(background=MenuAnimation.COLOR["background"])
        self.pack_propagate(0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_propagate(0)

    def config_template(self):
        self.m_informations_displayer.grid()

    def build_title(self):
        """
        Construit le titre du menu
        """
        title = Label(self, text="Animation")
        title.configure(
            font=font.Font(
                family=MenuAnimation.FONT["title"],
                size=22
            ),
            background="#333E47",
            foreground=MenuAnimation.COLOR["foreground"]
        )
        title.grid(sticky=W + E, pady=10)

    def build_speed_scale(self):
        """
        Construit la barre de reglage de la vitesse d'animation

        :return: Scale
        """
        speed_label = Label(self, text="Vitesse")
        speed_label.configure(
            font=font.Font(
                family=MenuAnimation.FONT["main"],
                size=MenuAnimation.SIZE["large"]
            ),
            background=MenuAnimation.COLOR["background"],
            foreground=MenuAnimation.COLOR["foreground"]
        )
        speed_label.grid(sticky=W, padx=5)

        scale = Scale(self, from_=-1, to=1, resolution=0.1, tickinterval=0.5, command=self.on_move_scale)
        scale.configure(
            length=MenuAnimation.WIDTH - 10,
            orient='horizontal',
            font=font.Font(
                family=MenuAnimation.FONT["main"],
                size=MenuAnimation.SIZE["medium"]
            ),
            background=MenuAnimation.COLOR["background"],
            foreground=MenuAnimation.COLOR["foreground"],
            activebackground=MenuAnimation.COLOR["background"],
            troughcolor="#f1f1f1",
            highlightthickness=0,
        )
        scale.set(1)
        scale.grid()

        return scale

    def build_play_pause_button(self):
        """
        Construit le bouton mettre l'animation en play/pause

        :return: Button
        """
        btn = Button(self, text="Pause", command=self.on_click_play_pause)
        btn.configure(
            font=font.Font(
                family=MenuAnimation.FONT["main"],
                size=MenuAnimation.SIZE["medium"]
            ),
            background=MenuAnimation.COLOR["foreground"],
            foreground=MenuAnimation.COLOR["background"],
            cursor="hand2",
            state=DISABLED
        )
        btn.grid(sticky=W + E, padx=20, pady=20)

        return btn

    def build_stop_button(self):
        """
        Construit le bouton arreter l'animation en cours

        :return: Button
        """
        btn = Button(self, text="Stop", command=self.on_click_stop)
        btn.configure(
            font=font.Font(
                family=MenuAnimation.FONT["main"],
                size=MenuAnimation.SIZE["medium"]
            ),
            background=MenuAnimation.COLOR["foreground"],
            foreground=MenuAnimation.COLOR["background"],
            cursor="hand2",
            state=DISABLED
        )
        btn.grid(sticky=W + E, padx=20, pady=0)

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

        if self.m_play_button.cget("text") == "Play":
            self.m_play_button.configure(text="Pause")
        else:
            self.m_play_button.configure(text="Play")

    def on_click_stop(self):
        self.master.m_menu.m_history_interpreter.stop()
        self.m_play_button.configure(text="Pause")
        self.set_buttons_state(DISABLED)
        self.master.m_menu.set_buttons_state(ACTIVE)
        self.master.m_grid.enable_event()

    def set_buttons_state(self, state):
        self.m_play_button.configure(state=state)
        self.m_stop_button.configure(state=state)
