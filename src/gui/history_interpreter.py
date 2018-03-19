from gui.cell import Cell
from history.action_type import ActionType


class HistoryInterpreter:

    def __init__(self, history, canvas):
        """
        Constructeur

        :param History history : Historique des actions
        :param Canvas canvas : Zone de dessin
        """
        self.m_current = None
        self.m_history = history
        self.m_canvas = canvas
        self.m_current_index = 0
        self.m_history_shapes = []

        self.m_animation_speed = 1
        self.m_pause = False
        self.m_scl_pause = False
        self.m_stop = False

    def calculate_animation_speed(self, speed):
        speed = float(speed)

        self.m_scl_pause = True if speed == 0 else False

        calc_speed = int(-1715 * pow(abs(speed), 3) + 4121 * pow(abs(speed), 2) - 3735 * abs(speed) + 1332)

        return calc_speed if speed >= 0 else -calc_speed

    def set_animation_speed(self, speed):
        """
        Change la vitesse d'animation

        :param int speed : Nouvelle vitesse
        """
        self.m_animation_speed = self.calculate_animation_speed(speed)

    def toggle_pause(self):
        self.m_pause = not self.m_pause

    def stop(self):
        self.m_stop = True
        self.m_canvas.clear()

    def run(self, reset=False):
        """
        Demarre l'animation du deroulement des actions de l'historique
        """
        if reset:
            self.m_pause = False
            self.m_current_index = 0
            self.m_history_shapes.clear()

        if self.m_stop:
            self.m_stop = False
            return

        if not self.m_pause and not self.m_scl_pause:
            if 0 <= self.m_current_index < len(self.m_history) and self.m_animation_speed > 0:
                self.render()
                self.m_current_index += 1
            elif 0 < self.m_current_index <= len(self.m_history) and self.m_animation_speed < 0:
                self.m_canvas.delete(self.m_history_shapes.pop())
                self.m_current_index -= 1

        self.m_canvas.after(abs(self.m_animation_speed), self.run)

    def render(self):
        """
        Interprete l'action pour un rendu visuel
        """
        x, y = self.m_history[self.m_current_index].m_element.m_x, self.m_history[self.m_current_index].m_element.m_y
        current = self.m_canvas.create_rectangle(
            Cell.WIDTH * x,
            Cell.WIDTH * y,
            Cell.WIDTH * (x + 1),
            Cell.WIDTH * (y + 1),
            fill=self.m_history[self.m_current_index].m_type["color"],
            tags="history"
        )
        self.m_history_shapes.append(current)

        self.m_canvas.master.m_menu_animation.m_informations_displayer.m_operations_count.configure(
            text="{:d}".format(self.m_current_index))

        self.m_canvas.master.m_menu_animation.m_informations_displayer.m_time.configure(
            text="{:f}".format(self.m_history[self.m_current_index].m_passed_time * 1000))

        if self.m_history[self.m_current_index].m_type == ActionType.SET_CURRENT:
            self.m_canvas.delete(self.m_current)
            self.m_current = current
