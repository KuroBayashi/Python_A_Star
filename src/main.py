import gui.gui as gg


class Main:

    # Start program
    def run(self):
        self.m_gui.show()

    # Constructor
    def __init__(self):
        self.m_gui = gg.Gui()


if __name__ == "__main__":
    main = Main()
    main.run()
