from history.action import Action


class History(list):

    def __init__(self):
        super().__init__()

    def add(self, action_type, element, passed_time):
        """
        Ajoute une action

        :param action_type: Type d'action effectuee
        :param element: Element sur lequel l'action a ete effectue
        :param passed_time: Temps ecoule avant execution de l'action

        :type action_type: ActionType
        :type element: object
        :type passed_time: double
        """
        self.append(Action(action_type, element, passed_time))
