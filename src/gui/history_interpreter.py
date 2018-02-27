from gui.cell import Cell
from gui.cell_type import CellType
from history.action_type import ActionType


class HistoryInterpreter:

    ANIM_SPEED = 20

    # Constructor
    def __init__(self, history, grid):
        self.m_history = history
        self.m_grid = grid

    # Run
    def run(self):
        for i in range(len(self.m_history.m_actions)):
            self.m_grid.after(i * HistoryInterpreter.ANIM_SPEED,
                              lambda index=i: self.interprete(self.m_history.m_actions[index]))

    # Interprete
    def interprete(self, action):
        if action.m_type == ActionType.ADD_TO_CLOSED_SET:
            color = CellType.TESTED["color"]
        elif action.m_type == ActionType.ADD_TO_OPEN_SET:
            color = CellType.ON_QUEUE["color"]
        else:
            color = CellType.VALIDATE["color"]

        x, y = action.m_element.m_x, action.m_element.m_y
        self.m_grid.create_rectangle(
            Cell.WIDTH * x,
            Cell.WIDTH * y,
            Cell.WIDTH * (x + 1),
            Cell.WIDTH * (y + 1),
            fill=color,
            tags="history"
        )