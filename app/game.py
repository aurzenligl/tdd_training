from .level import Tile

class Direction():
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3

class MoveError(Exception):
    pass

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

    def on_move(self, direction):
        """Reacts to movement"""
        _move(self.level, direction)

def _move(level, dir_):
    if level[_pos_add(level.player, _to_pos(dir_))] == Tile.WALL:
        raise MoveError("moving into a wall")

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
