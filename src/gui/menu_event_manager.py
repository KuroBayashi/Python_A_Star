class MenuEventManager:

    # Constructor
    def __init__(self, menu):
        self.m_menu = menu

        self.m_menu.m_start_button.bind("<Enter>", self.on_mouse_enter)
        self.m_menu.m_start_button.bind("<Leave>", self.on_mouse_leave)

    # On mouse enter
    def on_mouse_enter(self, event):
        event.widget.configure(background=self.m_menu.COLOR_HV)

    # On mouse leave
    def on_mouse_leave(self, event):
        event.widget.configure(background=self.m_menu.COLOR_FG)
