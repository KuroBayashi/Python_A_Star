from history.action import Action


class History:

    def add(self, atype, element):
        self.m_actions.append(Action(atype, element))

    def __init__(self):
        self.m_actions = []
