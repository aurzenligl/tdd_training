import pygame
from .color import Color
from .game import Direction
from .numtup import numtup

class Engine():
    """Manages game resources"""

    def __init__(self, game):
        self.game = game

    def run(self):
        """Initializes screen and runs game main loop."""
        pygame.init()
        size = numtup(self.game.size())
        self.screen = pygame.display.set_mode(size * Drawer.GRID)
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
    GRID = 20

    def __init__(self, screen):
        self.screen = screen

    def square(self, pos, color):
        topleft = tuple(numtup(pos) * self.GRID)
        pygame.draw.rect(self.screen, color, topleft + (self.GRID, self.GRID))

    def circle(self, pos, color):
        center = tuple(numtup(pos) * self.GRID + int(self.GRID * 0.5))
        pygame.draw.circle(self.screen, color, center, int(self.GRID * 0.4))

    def diamond(self, pos, color):
        center = numtup(pos) * self.GRID + int(self.GRID * 0.5)
        edgepos = int(self.GRID * 0.45)
        pygame.draw.aalines(self.screen, numtup(color) * 0.5, True, [
            center + (edgepos, 0),
            center + (0, edgepos),
            center + (-edgepos, 0),
            center + (0, -edgepos),
        ])
