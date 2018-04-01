class CellType:

    EMPTY = {"id": 0, "traversable": True, "color": "#f0f0f0"}        # White
    WALL = {"id": 1, "traversable": False, "color": "#7d7d7d"}        # Grey
    START = {"id": 2, "traversable": True, "color": "#64f460"}        # Green
    END = {"id": 3, "traversable": True, "color": "#ff2429"}          # Red
