from functools import partial
from tkinter import *

# Config
ROOT_W = 800
ROOT_H = 600
OPTS_W = 250
CELL_W = 50


def on_click(cell_id, event):
    canvas = event.widget

    if canvas.itemcget(cell_id, "fill") == "#f1f1f1":
        canvas.itemconfig(cell_id, fill="#bbd88f")
    else:
        canvas.itemconfig(cell_id, fill="#f1f1f1")


def draw_grid(event):
    canvas = event.widget
    canvas.update()
    columns_count = canvas.winfo_width() // CELL_W + 1
    lines_count = canvas.winfo_height() // CELL_W + 1

    for i in range(lines_count):
        canvas.create_line(0, CELL_W * i, canvas.winfo_width(), CELL_W * i)
    for j in range(columns_count):
        canvas.create_line(CELL_W * j, 0, CELL_W * j, canvas.winfo_height())


if __name__ == "__main__":
    # WINDOW #
    root = Tk()
    root.title = "Python - A* algorithm (Test)"
    root.geometry("%dx%d+%d+%d" % (ROOT_W, ROOT_H, (root.winfo_screenwidth() - ROOT_W) // 2, (root.winfo_screenheight() - ROOT_H) // 2))
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())

    # OPTION PANEL #
    frame = Frame(root)
    frame.configure(width=OPTS_W)
    frame.configure(background="#3f4d59")
    frame.pack(fill=Y, side=RIGHT)

    # CANVAS #
    canvas = Canvas(root)
    canvas.configure(background="#f1f1f1", highlightthickness=0)
    canvas.bind("<Configure>", draw_grid)
    canvas.pack(expand=True, fill=BOTH)

    root.mainloop()
