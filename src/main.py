import gui.gui as gg


class Main:

    def __init__(self):
        self.m_gui = gg.Gui()

    def run(self):
        self.m_gui.show()


if __name__ == "__main__":
    main = Main()
    main.run()
