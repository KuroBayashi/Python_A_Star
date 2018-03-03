class MenuEventManager:

    def __init__(self, menu):
        """
        Constructeur

        :param Menu menu : Menu sur lequel on va ecouter des evenements
        """
        self.m_menu = menu

        self.m_menu.m_start_button.bind("<Enter>", self.on_mouse_enter)
        self.m_menu.m_start_button.bind("<Leave>", self.on_mouse_leave)

        self.m_menu.m_clear_button.bind("<Enter>", self.on_mouse_enter)
        self.m_menu.m_clear_button.bind("<Leave>", self.on_mouse_leave)

        self.m_menu.m_reset_button.bind("<Enter>", self.on_mouse_enter)
        self.m_menu.m_reset_button.bind("<Leave>", self.on_mouse_leave)

    # On mouse enter
    def on_mouse_enter(self, event):
        event.widget.configure(background=self.m_menu.COLOR["hover"])

    # On mouse leave
    def on_mouse_leave(self, event):
        event.widget.configure(background=self.m_menu.COLOR["foreground"])
