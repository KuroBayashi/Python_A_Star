from history.action import Action


class History(list):

    def __init__(self):
        super().__init__()

    def add(self, action_type, element, passed_time):
        """
        Ajoute une action

        :param dict action_type : Type d'action
        :param object element : Object sur lequel l'action a eu lieu
        """
        self.append(Action(action_type, element, passed_time))
