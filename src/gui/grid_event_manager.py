import gui.cell as gcc
import gui.cell_type as gct


class GridEventManager:
    MOVE_START = 1
    MOVE_END = 2
    WALL_ADD = 3
    WALL_RMV = 4

    def __init__(self, grid):
        """
        Constructeur

        :param Grid grid : Grille sur lequel on va ecouter les evenements
        """
        self.m_grid = grid
        self.m_editor_type = None
        self.m_preview_id = None

        self.enable_event()

    def enable_event(self):
        self.m_grid.bind("<ButtonPress-1>", self.on_mouse_down)
        self.m_grid.bind("<ButtonRelease-1>", self.on_mouse_up)

    def disable_event(self):
        self.m_grid.unbind("<ButtonPress-1>")
        self.m_grid.unbind("<ButtonRelease-1>")

    def draw_preview(self, x, y, color):
        """
        Affiche la previsualisation

        :param int x : Position horizontale
        :param int y : Position verticale
        :param string color : Couleur de la previsualisation
        """
        self.m_preview_id = self.m_grid.create_rectangle(
            gcc.Cell.WIDTH * x,
            gcc.Cell.WIDTH * y,
            gcc.Cell.WIDTH * (x + 1),
            gcc.Cell.WIDTH * (y + 1),
            fill=color
        )

    def delete_preview(self):
        """
        Supprime la previsualisation
        """
        self.m_grid.delete(self.m_preview_id)
        self.m_preview_id = None

    def is_out_of_bound(self, event):
        """
        Verifie si le curseur est bien dans le canvas

        :param Event event: Evenement sur lequel la position du curseur doit etre verifie

        :return bool : Position valide
        """
        return not (0 < event.x < event.widget.winfo_width() - 1 and
                    0 < event.y < event.widget.winfo_height() - 1)

    def on_mouse_down(self, event):
        """
        Change le type d'edition

        :param Event event: Evenement en cours
        """
        if self.is_out_of_bound(event):
            return

        x, y = event.x // gcc.Cell.WIDTH, event.y // gcc.Cell.WIDTH

        self.m_editor_type = {
            gct.CellType.START["id"]: GridEventManager.MOVE_START,
            gct.CellType.END["id"]: GridEventManager.MOVE_END,
            gct.CellType.EMPTY["id"]: GridEventManager.WALL_ADD,
            gct.CellType.WALL["id"]: GridEventManager.WALL_RMV
        }[self.m_grid.m_cells[y][x].m_type["id"]]

        if self.m_editor_type in [GridEventManager.MOVE_START, GridEventManager.MOVE_END]:
            self.m_grid.m_cells[y][x].set_type(gct.CellType.EMPTY)

            self.draw_preview(x, y, {
                GridEventManager.MOVE_START : gct.CellType.START["color"],
                GridEventManager.MOVE_END : gct.CellType.END["color"]
            }[self.m_editor_type])

        self.m_grid.bind("<B1-Motion>", self.on_mouse_move)

    def on_mouse_move(self, event):
        """
        Ajoute/Supprime des murs ou Deplace les cases de depart/arrivee en fonction du mode d'edition en cours

        :param Event event : Evenement en cours
        """
        if self.is_out_of_bound(event):
            return

        x, y = event.x // gcc.Cell.WIDTH, event.y // gcc.Cell.WIDTH
        cell_type = self.m_grid.m_cells[y][x].m_type

        if self.m_editor_type == GridEventManager.MOVE_START:
            if cell_type == gct.CellType.END:
                self.on_mouse_up(event)
            else:
                self.delete_preview()
                self.draw_preview(x, y, gct.CellType.START["color"])
        elif self.m_editor_type == GridEventManager.MOVE_END:
            if cell_type == gct.CellType.START:
                self.on_mouse_up(event)
            else:
                self.delete_preview()
                self.draw_preview(x, y, gct.CellType.END["color"])
        elif self.m_editor_type == GridEventManager.WALL_ADD:
            if cell_type == gct.CellType.EMPTY:
                self.m_grid.m_cells[y][x].set_type(gct.CellType.WALL)
        elif self.m_editor_type == GridEventManager.WALL_RMV:
            if cell_type == gct.CellType.WALL:
                self.m_grid.m_cells[y][x].set_type(gct.CellType.EMPTY)

    def on_mouse_up(self, event):
        """
        Change la derniere cellule active lorsque l'on relache le clic

        :param Event event : Evenement en cours
        """
        if self.m_editor_type is None:
            return

        event.x = sorted((0, event.x, event.widget.winfo_width() - 2))[1]
        event.y = sorted((0, event.y, event.widget.winfo_height() - 2))[1]

        x, y = event.x // gcc.Cell.WIDTH, event.y // gcc.Cell.WIDTH
        cell_type_id = self.m_grid.m_cells[y][x].m_type["id"]

        if self.m_editor_type in [GridEventManager.MOVE_START, GridEventManager.MOVE_END]:
            if self.m_preview_id is not None:
                preview_bbox = self.m_grid.coords(self.m_preview_id)
                x, y = int(preview_bbox[0] // gcc.Cell.WIDTH), int(preview_bbox[1] // gcc.Cell.WIDTH)

            self.m_grid.m_cells[y][x].set_type({
               GridEventManager.MOVE_START: gct.CellType.START,
               GridEventManager.MOVE_END: gct.CellType.END
           }[self.m_editor_type])

            self.delete_preview()
        elif cell_type_id not in [gct.CellType.START["id"], gct.CellType.END["id"]]:
            self.m_grid.m_cells[y][x].set_type({
               GridEventManager.WALL_ADD: gct.CellType.WALL,
               GridEventManager.WALL_RMV: gct.CellType.EMPTY
            }[self.m_editor_type])

        self.m_editor_type = None

        self.m_grid.unbind("<B1-Motion>")
