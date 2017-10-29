class Game():
    """Game logic, knows how to move and what to render"""

    def __init__(self, level):
        self.level = level

    def size(self):
        """Returns cols and rows tuple"""
        return self.level.size()

    def on_render(self, drawer):
        """Draws all game objects"""
        pass

    def on_move(self, direction):
        """Reacts to movement"""
        pass
