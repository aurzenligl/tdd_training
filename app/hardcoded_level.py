from .level import Level, SquareType

S = SquareType.SPACE
W = SquareType.WALL
B = SquareType.BOX
G = SquareType.GOAL

hardcoded_level = [
    W, W, W, W, W,
    W, S, B, S, W,
    W, W, W, W, W,
]

def get_level():
    return Level(5, 3, hardcoded_level)
