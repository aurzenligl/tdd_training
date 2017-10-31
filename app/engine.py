import pygame
from .color import Color

class Engine():
    """Manages game resources"""

    def __init__(self, game):
        self.game = game

    def run(self):
        """Initializes screen and runs game main loop."""
        pygame.init()
        cols, rows = self.game.size()
        self.screen = pygame.display.set_mode(cols * 20, rows * 20)
        self._render()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

    def _render(self):
        """Renders new game frame"""
        self.screen.fill(Color.BLACK)
        pygame.display.flip()

    def _keypress(self, key):
        """Reacts on any key press"""
        pass
