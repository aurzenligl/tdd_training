import pygame
from .color import Color
from .level import Tile
from .game import Direction

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
                if event.type == pygame.KEYDOWN:
                    self._keypress(event.key)

    def _render(self):
        """Renders new game frame"""
        self.screen.fill(Color.BLACK)
        self.game.on_render(Drawer(self.screen))
        pygame.display.flip()

    def _keypress(self, key):
        """Reacts on any key press"""
        directions = {
            pygame.K_UP: Direction.UP,
            pygame.K_DOWN: Direction.DOWN,
            pygame.K_RIGHT: Direction.RIGHT,
            pygame.K_LEFT: Direction.LEFT
        }
        direction = directions.get(key)
        if direction is not None:
            self.game.on_move(direction)
            self._render()

class Drawer():
    type_to_col = {
        Tile.SPACE: Color.LBLUE,
        Tile.WALL: Color.RED,
        Tile.BOX: Color.BROWN,
    }

    def __init__(self, screen):
        self.screen = screen

    def square(self, pos, type_):
        surf = pygame.Surface((20, 20))
        surf.fill(self.type_to_col[type_])
        col, row = pos
        self.screen.blit(surf, (col * 20, row * 20))

    def circle(self, pos, color):
        col, row = pos
        pygame.draw.circle(self.screen, color, (col * 20 + 10, row * 20 + 10), 8)
