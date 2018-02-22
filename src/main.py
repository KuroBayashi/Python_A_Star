import gui.gui as gg


class Main:
    # Convert Gui grid to A* nodes list
    # def convert_grid_to_nodes(self):
    #     neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    #     if self.m_gui.m_menu.m_selected_diagonal:
    #         neighbors += [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    #
    #     for i in range(len(self.nodes)):
    #         node = self.nodes[i]
    #
    #         for j in range(len(self.nodes)):
    #             dx = node.m_x - self.nodes[j].m_x
    #             dy = node.m_y - self.nodes[j].m_y
    #
    #             if (dx, dy) in neighbors:
    #                 node.m_neighbors.append(node[j])

    # Start program
    def run(self):
        self.m_gui.show()

    # Constructor
    def __init__(self):
        self.m_gui = gg.Gui()


if __name__ == "__main__":
    main = Main()
    main.run()
