from tkinter import Frame, Label, Y, RIGHT, N, E, S, W


class Options(Frame):

    WIDTH = 250

    def draw_content(self):
        title = Label(self, text="Options")
        title.grid(sticky=N+E+S+W, row=0, column=1)

    def setup_frame(self):
        self.configure(width=Options.WIDTH)
        self.configure(background="#3f4d59")
        self.grid_propagate(0)
        self.pack(fill=Y, side=RIGHT)

    def __init__(self, root):
        super().__init__(root)
        self.setup_frame()

        self.draw_content()
