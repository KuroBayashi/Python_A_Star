from gui.cell import Cell
from gui.cell_type import CellType
from history.action_type import ActionType


class HistoryInterpreter:

    ANIM_SPEED = 10

    def __init__(self, history, canvas):
        """
        Constructeur

        :param History history : Historique des actions
        :param Canvas canvas : Zone de dessin
        """
        self.m_current = None
        self.m_history = history
        self.m_canvas = canvas

    def run(self):
        """
        Demarre l'animation du deroulement des actions de l'historique
        """
        for i in range(len(self.m_history)):
            self.m_canvas.after(i * HistoryInterpreter.ANIM_SPEED,
                              lambda index=i: self.render(self.m_history[index]))

    def render(self, action):
        """
        Interprete l'action pour un rendu visuel

        :param Action action : Action a interpreter
        """
        if self.m_current is not None:
            self.m_canvas.delete(self.m_current)

        x, y = action.m_element.m_x, action.m_element.m_y
        current = self.m_canvas.create_rectangle(
            Cell.WIDTH * x,
            Cell.WIDTH * y,
            Cell.WIDTH * (x + 1),
            Cell.WIDTH * (y + 1),
            fill=action.m_type["color"],
            tags="history"
        )

        if action.m_type == ActionType.SET_CURRENT:
            self.m_current = current