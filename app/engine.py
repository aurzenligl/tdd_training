from contextlib import contextmanager
import pygame
from .color import Color
from .numtup import numtup

class Engine():
    """Provides game platform: graphics and user input"""

    def __init__(self):
        self.keydown_actions = {}
        pygame.init()

    def screen(self, geometry):
        return Screen(geometry)

    def connect_keydown(self, key, action):
        self.keydown_actions[key] = action

    def run(self):
        """Runs game main loop."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    action = self.keydown_actions.get(event.key)
                    if action is not None:
                        if action() is False:
                            return

class Screen():
    GRID = 20

    def __init__(self, geometry):
        self.surf = pygame.display.set_mode(numtup(geometry) * self.GRID)

    @contextmanager
    def draw(self):
        self.surf.fill(Color.BLACK)
        yield Drawer(self.surf)
        pygame.display.flip()

class Drawer():
    def __init__(self, surf):
        self.surf = surf

    def square(self, pos, color):
        topleft = tuple(numtup(pos) * Screen.GRID)
        pygame.draw.rect(self.surf, color, topleft + (Screen.GRID, Screen.GRID))

    def circle(self, pos, color):
        center = tuple(numtup(pos) * Screen.GRID + int(Screen.GRID * 0.5))
        pygame.draw.circle(self.surf, color, center, int(Screen.GRID * 0.4))

    def diamond(self, pos, color):
        center = numtup(pos) * Screen.GRID + int(Screen.GRID * 0.5)
        edgepos = int(Screen.GRID * 0.45)
        pygame.draw.aalines(self.surf, numtup(color) * 0.5, True, [
            center + (edgepos, 0),
            center + (0, edgepos),
            center + (-edgepos, 0),
            center + (0, -edgepos),
        ])
