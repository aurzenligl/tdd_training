import pygame

class Engine():
    """Manages game resources"""

    def __init__(self, game):
        self.game = game

    def run(self):
        """Initializes screen and runs game main loop."""
        pygame.init()
        cols, rows = self.game.size()
        pygame.display.set_mode(cols * 20, rows * 20)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

    def _render(self):
        """Renders new game frame"""
        pass

    def _keypress(self, key):
        """Reacts on any key press"""
        pass
