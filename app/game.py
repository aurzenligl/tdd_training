from .level import Tile
from .color import Color
from .numtup import numtup

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
        tile_to_color = {
            Tile.FLOOR: Color.LBLUE,
            Tile.WALL: Color.RED,
            Tile.BOX: Color.BROWN,
        }

        for pos, tile in self.level:
            color_ = tile_to_color[tile.tile]
            drawer.square(pos, color_)
            if tile.goal:
                drawer.diamond(pos, color_)
        drawer.circle(self.level.player, Color.YELLOW)

    def on_move(self, direction):
        """Reacts to movement"""
        return _move(self.level, direction)

def _move(level, dir_):
    shift = _to_pos(dir_)
    start = numtup(level.player)
    end = start + shift
    if level[end].tile == Tile.WALL:
        return Move(Move.ILLEGAL, start, end)
    elif level[end].tile == Tile.FLOOR:
        level.player = end
        return Move(Move.WALK, start, end)
    elif level[end].tile == Tile.BOX:
        pastend = end + shift
        level[end].tile = Tile.FLOOR
        level[pastend].tile = Tile.BOX
        level.player = end
        return Move(Move.PUSH, start, end)

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
