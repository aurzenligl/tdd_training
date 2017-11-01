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
        pass
