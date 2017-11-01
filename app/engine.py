import pygame
from .color import Color
from .level import Tile

class Engine():
    """Manages game resources"""

    def __init__(self, game):
        self.game = game

    def run(self):
        """Initializes screen and runs game main loop."""
        pygame.init()
        cols, rows = self.game.size()
        self.screen = pygame.display.set_mode((cols * 20, rows * 20))
        self._render()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

    def _render(self):
        """Renders new game frame"""
        class Drawer():
            type_to_col = {
                Tile.SPACE: Color.LBLUE,
                Tile.WALL: Color.RED,
                Tile.BOX: Color.BROWN,
                Tile.GOAL: Color.BLUE,
                Tile.SETBOX: Color.GBLUE
            }
            def __init__(self, screen):
                self.screen = screen
            def square(self, pos, type_):
                surf = pygame.Surface((20, 20))
                surf.fill(self.type_to_col[type_])
                col, row = pos
                self.screen.blit(surf, (col * 20, row * 20))

        self.screen.fill(Color.BLACK)
        self.game.on_render(Drawer(self.screen))
        pygame.display.flip()

    def _keypress(self, key):
        """Reacts on any key press"""
        pass
