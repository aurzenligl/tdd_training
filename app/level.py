class SquareType():
    SPACE = 0
    WALL = 1
    BOX = 2
    PLAYER = 3
    GOAL = 4
    SETBOX = 5

class Level():
    """Represents logical level state"""

    def __init__(self, columns, rows, squaretypes):
        """
        :arg squaretypes: flat list of SquareType, consecutive
                          elements represent rows from left to right,
                          top to bottom.
        """
        self.cols = columns
        self.rows = rows
        self.squares = squaretypes

    def size(self):
        """Returns tuple with column and row counts"""
        return self.cols, self.rows

    def __getitem__(self, pos):
        """
        :arg pos: col and row tuple
        """
        col, row = pos
        return self.squares[row * self.cols + col]

    def __setitem__(self, pos, value):
        """
        :arg pos: col and row tuple
        """
        col, row = pos
        self.squares[row * self.cols + col] = value

    def __iter__(self):
        """Returns sequence of tuples of row-col tuples and SquareType.

        Sequence consists of rows output left to right, top to bottom.
        """
        pass
