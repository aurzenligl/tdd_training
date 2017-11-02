import pygame
from .color import Color
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
    def __init__(self, screen):
        self.screen = screen

    def square(self, pos, color):
        col, row = pos
        pygame.draw.rect(self.screen, color, (col * 20, row * 20, 20, 20))

    def circle(self, pos, color):
        col, row = pos
        pygame.draw.circle(self.screen, color, (col * 20 + 10, row * 20 + 10), 8)

    def diamond(self, pos, color):
        # TODO: prepare a tuple-derived type with + and * operators
        def mul2(tpl, scale):
            return tpl[0]*scale, tpl[1]*scale

        def mul3(tpl, scale):
            return tpl[0]*scale, tpl[1]*scale, tpl[2]*scale

        def add(tpl1, tpl2):
            return tpl1[0]+tpl2[0], tpl1[1]+tpl2[1]

        center = add(mul2(pos, 20), (10, 10))

        pygame.draw.aalines(self.screen, mul3(color, 0.5), True, [
            add(center, (9, 0)),
            add(center, (0, 9)),
            add(center, (-9, 0)),
            add(center, (0, -9)),
        ])
