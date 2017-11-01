from .level import Level, Tile

S = Tile.SPACE
W = Tile.WALL
B = Tile.BOX
G = Tile.GOAL

hardcoded_level = [
    S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S,
    S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S,
    S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S,
    S, S, S, S, S, S, S, S, S, S, S, W, W, W, W, W, S, S, S, S,
    S, S, S, S, S, W, W, W, W, W, W, W, S, S, S, W, W, S, S, S,
    S, S, S, S, W, W, S, W, S, S, W, W, S, B, B, S, W, S, S, S,
    S, S, S, S, W, S, S, S, S, B, S, S, S, S, S, S, W, S, S, S,
    S, S, S, S, W, S, S, B, S, S, W, W, W, S, S, S, W, S, S, S,
    S, S, S, S, W, W, W, S, W, W, W, W, W, B, W, W, W, S, S, S,
    S, S, S, S, W, S, B, S, S, W, W, W, S, G, G, W, S, S, S, S,
    S, S, S, S, W, S, B, S, B, S, B, S, G, G, G, W, S, S, S, S,
    S, S, S, S, W, S, S, S, S, W, W, W, G, G, G, W, S, S, S, S,
    S, S, S, S, W, S, B, B, S, W, S, W, G, G, G, W, S, S, S, S,
    S, S, S, S, W, S, S, W, W, W, S, W, W, W, W, W, S, S, S, S,
    S, S, S, S, W, W, W, W, S, S, S, S, S, S, S, S, S, S, S, S,
    S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S, S,
]

def get_level():
    return Level(20, 16, hardcoded_level)
