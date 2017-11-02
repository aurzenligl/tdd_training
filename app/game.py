from .level import Tile
from .color import Color

class Direction():
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3

class Move():
    ILLEGAL = 0
    WALK = 1
    PUSH = 2

    def __init__(self, type_, start=None, end=None):
        self.type = type_
        self.start = start
        self.end = end

class Game():
    """Game logic, knows how to move and what to render"""

    def __init__(self, level):
        self.level = level

    def size(self):
        """Returns cols and rows tuple"""
        return self.level.size

    def on_render(self, drawer):
        """Draws all game objects"""
        for pos, type_ in self.level:
            drawer.square(pos, type_)
        drawer.circle(self.level.player, Color.YELLOW)

    def on_move(self, direction):
        """Reacts to movement"""
        return _move(self.level, direction)

def _move(level, dir_):
    start = level.player
    end = _pos_add(start, _to_pos(dir_))
    if level[end] == Tile.WALL:
        return Move(Move.ILLEGAL, start, end)

def _pos_add(lhs, rhs):
    return (lhs[0] + rhs[0], lhs[1] + rhs[1])

def _to_pos(dir_):
    dirtopos = {
        Direction.LEFT: (-1, 0),
        Direction.RIGHT: (1, 0),
        Direction.UP: (0, -1),
        Direction.DOWN: (0, 1),
    }
    return dirtopos[dir_]
