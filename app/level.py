class Tile():
    SPACE = 0
    WALL = 1
    BOX = 2

    def __init__(self, tile, goal=False):
        self.tile = tile
        self.goal = goal

class LevelIterator():
    def __init__(self, level):
        self.level = level
        self.n = 0

    def __next__(self):
        n = self.n
        if n >= len(self.level._tiles):
            raise StopIteration()
        self.n += 1
        row, col = divmod(n, self.level.size[0])
        pos = col, row
        return (pos), self.level[pos]

    def next(self):
        return self.__next__()

class Level(object):
    """Represents logical level state"""

    def __init__(self, size, tilecodes):
        """
        :arg size: tuple with number of columns and rows
        :arg tilecodes: string with flat list of tile codes, consecutive
                        elements represent rows from left to right,
                        top to bottom. Chars have following meanings:
                        ' ' - floor
                        '%' - wall
                        'o' - box
                        '@' - player
                        '.' - goal
        """
        nexpect = size[0] * size[1]
        if nexpect != len(tilecodes):
            raise ValueError("expected %s elements, got %s"
                             % (nexpect, len(tilecodes)))

        nplayers = tilecodes.count('@')
        if nplayers == 0:
            raise ValueError("no player: '@' specified")
        if nplayers > 1:
            raise ValueError("multiple players: '@' specified")

        def to_tile(index, code):
            code2tile = {
                ' ': Tile.SPACE,
                '.': Tile.SPACE,
                '@': Tile.SPACE,
                '%': Tile.WALL,
                'o': Tile.BOX,
            }
            tile = code2tile.get(code)
            if tile is None:
                pos = tuple(reversed(divmod(index, size[0])))
                raise ValueError("invalid tilecode '%s' on %s" % (code, pos))
            goal = code == '.'
            return Tile(tile, goal)

        self._size = size
        self._tiles = [to_tile(index, code) for index, code in enumerate(tilecodes)]
        self._player = tuple(reversed(divmod(tilecodes.find('@'), size[0])))

    @property
    def size(self):
        """Returns tuple with column and row counts"""
        return self._size

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, pos):
        tile = self[pos].tile
        if tile != Tile.SPACE:
            raise ValueError("expected player on floor")
        self._player = pos

    def __getitem__(self, pos):
        """
        :arg pos: col and row tuple
        """
        if _out_of_bounds(pos, self.size):
            raise ValueError("index %s out of bounds %s" % (pos, self._size))
        return self._tiles[_index(pos, self.size)]

    def __iter__(self):
        """Returns sequence of tuples of row-col tuples and SquareType.

        Sequence consists of rows output left to right, top to bottom.
        """
        return LevelIterator(self)

def _out_of_bounds(pos, bounds):
    return any(pos[i] >= bounds[i] for i in range(len(bounds)))

def _index(pos, bounds):
    return pos[1] * bounds[0] + pos[0]
