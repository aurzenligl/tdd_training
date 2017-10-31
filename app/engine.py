import pygame

class Engine():
    """Manages game resources"""

    def __init__(self, game):
        pygame.init()
        cols, rows = game.size()
        pygame.display.set_mode(cols * 20, rows * 20)

    def run(self, game):
        """Initializes screen and runs game main loop."""
        pass

    def _render(self):
        """Renders new game frame"""
        pass

    def _keypress(self, key):
        """Reacts on any key press"""
        pass
