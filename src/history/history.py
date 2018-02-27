from history.action import Action


class History:

    def add(self, type, element):
        self.m_actions.append(Action(type, element))

    def __init__(self):
        self.m_actions = []
