class SquareType():
    SPACE = 0
    WALL = 1
    BOX = 2
    GOAL = 3
    SETBOX = 4

class LevelIterator():
    def __init__(self, level):
        self.level = level
        self.n = 0

    def __next__(self):
        n = self.n
        if n >= len(self.level._squares):
            raise StopIteration()
        self.n += 1
        row, col = divmod(n, self.level.size[0])
        pos = col, row
        return (pos), self.level[pos]

    def next(self):
        return self.__next__()

class Level():
    """Represents logical level state"""

    def __init__(self, columns, rows, squaretypes, player):
        """
        :arg columns: number of columns
        :arg rows: number of rows
        :arg squaretypes: flat list of SquareType, consecutive
                          elements represent rows from left to right,
                          top to bottom.
        :arg player: player's column and row tuple
        """
        size = columns, rows

        nexpect = columns * rows
        if nexpect != len(squaretypes):
            raise ValueError("expected %s elements, got %s"
                             % (nexpect, len(squaretypes)))

        if _out_of_bounds(player, size):
            raise ValueError("player position %s out of bounds %s"
                             % (player, size))

        if squaretypes[_index(player, size)] != SquareType.SPACE:
            raise ValueError("expected player on empty space")

        self._size = size
        self._squares = squaretypes
        self._player = player

    @property
    def size(self):
        """Returns tuple with column and row counts"""
        return self._size

    @property
    def player(self):
        return self._player

    def __getitem__(self, pos):
        """
        :arg pos: col and row tuple
        """
        if _out_of_bounds(pos, self.size):
            raise ValueError("index %s out of bounds %s" % (pos, self._size))
        return self._squares[_index(pos, self.size)]

    def __setitem__(self, pos, value):
        """
        :arg pos: col and row tuple
        """
        if _out_of_bounds(pos, self.size):
            raise ValueError("index %s out of bounds %s" % (pos, self._size))
        self._squares[_index(pos, self.size)] = value

    def __iter__(self):
        """Returns sequence of tuples of row-col tuples and SquareType.

        Sequence consists of rows output left to right, top to bottom.
        """
        return LevelIterator(self)

def _out_of_bounds(pos, bounds):
    return any(pos[i] >= bounds[i] for i in range(len(bounds)))

def _index(pos, bounds):
    return pos[1] * bounds[0] + pos[0]
