from gui.config import Config


class MenuEventManager:

    def __init__(self, menu):
        """
        Constructeur

        :param menu: Menu sur lequel on va ecouter des evenements

        :type menu: Menu
        """
        menu.m_start_button.bind("<Enter>", self.on_mouse_enter)
        menu.m_start_button.bind("<Leave>", self.on_mouse_leave)

        menu.m_reset_button.bind("<Enter>", self.on_mouse_enter)
        menu.m_reset_button.bind("<Leave>", self.on_mouse_leave)

    def on_mouse_enter(self, event):
        """
        Change la couleur du bouton quand la souris le survole

        :param event: Evenement

        :type event: event
        """
        event.widget.configure(background=Config.COLOR["btn-hv"])

    def on_mouse_leave(self, event):
        """
        Remet la couleur du bouton original quand la souris cesse de le survoler

        :param event: Evenement

        :type event: event
        """
        event.widget.configure(background=Config.COLOR["btn-bg"])
