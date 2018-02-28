import gui.cell as gcc
import gui.cell_type as gct


class GridEventManager:

    MOVE_START = 1
    MOVE_END = 2
    WALL_ADD = 3
    WALL_RMV = 4

    # Delete preview
    def delete_preview(self):
        self.m_grid.delete(self.m_preview_id)
        self.m_preview_id = None

    # On mouse down
    def on_mouse_down(self, event):
        if event.x >= event.widget.winfo_width()-1 or event.y >= event.widget.winfo_height()-1:
            return

        x, y = event.x // gcc.Cell.WIDTH, event.y // gcc.Cell.WIDTH
        type_id = self.m_grid.m_cells[y][x].m_type["id"]

        # voir dico pour remplacer switch
        if type_id == gct.CellType.START["id"]:
            self.m_editor_type = GridEventManager.MOVE_START
            self.m_grid.m_cells[y][x].set_type(gct.CellType.EMPTY)
        elif type_id == gct.CellType.END["id"]:
            self.m_editor_type = GridEventManager.MOVE_END
            self.m_grid.m_cells[y][x].set_type(gct.CellType.EMPTY)
        elif type_id == gct.CellType.EMPTY["id"]:
            self.m_editor_type = GridEventManager.WALL_ADD
        elif type_id == gct.CellType.WALL["id"]:
            self.m_editor_type = GridEventManager.WALL_RMV

        self.m_grid.bind("<B1-Motion>", self.on_mouse_move)
        self.m_grid.bind("<Leave>", self.on_mouse_out)

    # On mouse move
    def on_mouse_move(self, event):
        if event.x <= 0 or event.x >= event.widget.winfo_width()-1 \
                or event.y <= 0 or event.y >= event.widget.winfo_height()-1:
            return

        x, y = event.x // gcc.Cell.WIDTH, event.y // gcc.Cell.WIDTH
        type_id = self.m_grid.m_cells[y][x].m_type["id"]

        if self.m_editor_type == GridEventManager.MOVE_START:
            if type_id == gct.CellType.END["id"]:
                self.on_mouse_up(event)
            else:
                self.delete_preview()
                self.m_preview_id = self.m_grid.create_rectangle(
                    gcc.Cell.WIDTH * x,
                    gcc.Cell.WIDTH * y,
                    gcc.Cell.WIDTH * (x + 1),
                    gcc.Cell.WIDTH * (y + 1),
                    fill=gct.CellType.START["color"]
                )
        elif self.m_editor_type == GridEventManager.MOVE_END:
            if type_id == gct.CellType.START["id"]:
                self.on_mouse_up(event)
            else:
                self.delete_preview()
                self.m_preview_id = self.m_grid.create_rectangle(
                    gcc.Cell.WIDTH * x,
                    gcc.Cell.WIDTH * y,
                    gcc.Cell.WIDTH * (x + 1),
                    gcc.Cell.WIDTH * (y + 1),
                    fill=gct.CellType.END["color"]
                )
        elif self.m_editor_type == GridEventManager.WALL_ADD:
            if type_id == gct.CellType.EMPTY["id"]:
                self.m_grid.m_cells[y][x].set_type(gct.CellType.WALL)
        elif self.m_editor_type == GridEventManager.WALL_RMV:
            if type_id == gct.CellType.WALL["id"]:
                self.m_grid.m_cells[y][x].set_type(gct.CellType.EMPTY)

    # On mouse up
    def on_mouse_up(self, event):
        if self.m_editor_type is None \
                or event.x <= 0 or event.x >= event.widget.winfo_width()-1 \
                or event.y <= 0 or event.y >= event.widget.winfo_height()-1:
            return

        x, y = event.x // gcc.Cell.WIDTH, event.y // gcc.Cell.WIDTH
        type_id = self.m_grid.m_cells[y][x].m_type["id"]

        if self.m_editor_type in [GridEventManager.MOVE_START, GridEventManager.MOVE_END]:
            if self.m_preview_id is not None:
                preview_bbox = self.m_grid.coords(self.m_preview_id)
                x, y = int(preview_bbox[0] // gcc.Cell.WIDTH), int(preview_bbox[1] // gcc.Cell.WIDTH)

            if self.m_editor_type == GridEventManager.MOVE_START:
                self.m_grid.m_cells[y][x].set_type(gct.CellType.START)
            else:
                self.m_grid.m_cells[y][x].set_type(gct.CellType.END)

            self.delete_preview()
        elif type_id not in [gct.CellType.START["id"], gct.CellType.END["id"]]:
            if self.m_editor_type == GridEventManager.WALL_ADD:
                self.m_grid.m_cells[y][x].set_type(gct.CellType.WALL)
            elif self.m_editor_type == GridEventManager.WALL_RMV:
                self.m_grid.m_cells[y][x].set_type(gct.CellType.EMPTY)

        self.m_editor_type = None

        self.m_grid.unbind("<B1-Motion>")
        self.m_grid.unbind("<Leave>")

    # On mouse out
    def on_mouse_out(self, event):
        event.x = 0 if event.x <= 0 \
            else event.widget.winfo_width() - 1 if event.x >= event.widget.winfo_width() \
            else event.x
        event.y = 0 if event.y <= 0 \
            else event.widget.winfo_height() - 1 if event.y >= event.widget.winfo_height() \
            else event.y

        self.on_mouse_up(event)

    # Constructor
    def __init__(self, grid):
        self.m_grid = grid
        self.m_editor_type = None
        self.m_preview_id = None

        self.m_grid.bind("<ButtonPress-1>", self.on_mouse_down)
        self.m_grid.bind("<ButtonRelease-1>", self.on_mouse_up)
