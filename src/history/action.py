class Action:

    def __init__(self, action_type, element, passed_time):
        """
        Constructeur

        :param action_type: Type d'action effectuee
        :param element: Element sur lequel l'action a ete effectue
        :param passed_time: Temps ecoule avant execution de l'action

        :type action_type: ActionType
        :type element: object
        :type passed_time: double
        """
        self.m_type = action_type
        self.m_element = element
        self.m_passed_time = passed_time
