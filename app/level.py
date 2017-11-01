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
        if n >= len(self.level.squares):
            raise StopIteration()
        self.n += 1
        row, col = divmod(n, self.level.size()[0])
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
        self.cols = columns
        self.rows = rows
        self.squares = squaretypes
        self._player = player

        nexpect = columns * rows
        nactual = len(squaretypes)
        if nexpect != nactual:
            raise ValueError("expected %s elements, got %s"
                             % (nexpect, nactual))

        if player[0] > columns or player[1] > rows:
            raise ValueError("player position %s out of bounds %s"
                             % (player, (columns, rows)))

        if self[player] != SquareType.SPACE:
            raise ValueError("expected player on empty space")

    def size(self):
        """Returns tuple with column and row counts"""
        return self.cols, self.rows

    @property
    def player(self):
        return self._player

    def __getitem__(self, pos):
        """
        :arg pos: col and row tuple
        """
        col, row = pos
        if col >= self.cols or row >= self.rows:
            raise ValueError("index (%s,%s) out of bounds (%s,%s)"
                             % (col, row, self.cols, self.rows))
        return self.squares[row * self.cols + col]

    def __setitem__(self, pos, value):
        """
        :arg pos: col and row tuple
        """
        col, row = pos
        if col >= self.cols or row >= self.rows:
            raise ValueError("index (%s,%s) out of bounds (%s,%s)"
                             % (col, row, self.cols, self.rows))
        self.squares[row * self.cols + col] = value

    def __iter__(self):
        """Returns sequence of tuples of row-col tuples and SquareType.

        Sequence consists of rows output left to right, top to bottom.
        """
        return LevelIterator(self)
