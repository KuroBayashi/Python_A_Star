from history.action import Action


class History(list):

    def __init__(self):
        super().__init__()

    def add(self, action_type, element):
        """
        Ajoute une action

        :param dict action_type : Type d'action
        :param object : Object sur lequel l'action a eu lieu
        """
        self.append(Action(action_type, element))
