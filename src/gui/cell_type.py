class CellType:
    EMPTY = {"id": 0, "color": "#f0f0f0"}        # White
    WALL = {"id": 1, "color": "#7d7d7d"}         # Grey
    START = {"id": 2, "color": "#64f460"}        # Green
    END = {"id": 3, "color": "#ff2429"}          # Red
    TESTED = {"id": 4, "color": "#92decf"}       # Light blue
    ON_QUEUE = {"id": 5, "color": "#a4dd93"}     # Light green
