class Action:

    def __init__(self, action_type, element, passed_time):
        """
        Constructeur

        :param ActionType action_type : Type d'action effectuee
        :param object element : Element sur lequel l'action a ete effectue
        """
        self.m_type = action_type
        self.m_element = element
        self.m_passed_time = passed_time