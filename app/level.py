class SquareType():
    SPACE = 0
    WALL = 1
    BOX = 2
    PLAYER = 3
    GOAL = 4
    SETBOX = 5

class Level():
    """Represents logical level state"""

    def __init__(self, rows, columns, squaretypes):
        """
        :arg squaretypes: flat list of SquareType, consecutive
                          elements represent rows from left to right,
                          top to bottom.
        """
        pass

    def size(self):
        """Returns tuple with column and row counts"""
        pass

    def __call__(self, col, row):
        """Indexing operator"""
        pass

    def __iter__(self):
        """Returns sequence of tuples of row-col tuples and SquareType.

        Sequence consists of rows output left to right, top to bottom.
        """
        pass
