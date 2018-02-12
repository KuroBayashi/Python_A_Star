import gui.gui as gg


class Main:

    # Convert Gui grid to A* nodes list
    def convert_grid_to_nodes(self):
        pass

    # Start program
    def run(self):
        self.m_gui.show()

    # Constructor
    def __init__(self):
        self.m_gui = gg.Gui()


if __name__ == "__main__":
    main = Main()
    main.run()
