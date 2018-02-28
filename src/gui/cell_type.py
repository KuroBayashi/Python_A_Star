class CellType:
    EMPTY = {"id": 0, "traversable": True, "color": "#f0f0f0"}        # White
    WALL = {"id": 1, "traversable": False, "color": "#7d7d7d"}        # Grey
    START = {"id": 2, "traversable": True, "color": "#64f460"}        # Green
    END = {"id": 3, "traversable": True, "color": "#ff2429"}          # Red

    ON_QUEUE = {"id": 4, "traversable": True, "color": "#a4dd93"}     # Light green
    TESTED = {"id": 5, "traversable": True, "color": "#92decf"}       # Light blue
    CURRENT = {"id": 6, "traversable": True, "color": "#f49842"}       # Orange
    VALIDATE = {"id": 7, "traversable": True, "color": "#e29ce1"}     # Light purple