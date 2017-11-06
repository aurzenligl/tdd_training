import time
import pygame
from .level import Tile
from .color import Color
from .numtup import numtup

class Game():
    """Game logic, knows how to move and what to render"""

    def __init__(self, engine, level):
        self.screen = engine.screen(geometry=level.size)
        self.level = level

        engine.connect_keydown(pygame.K_DOWN, lambda: self.on_move((0, 1)))
        engine.connect_keydown(pygame.K_UP, lambda: self.on_move((0, 1)))
        engine.connect_keydown(pygame.K_RIGHT, lambda: self.on_move((1, 0)))
        engine.connect_keydown(pygame.K_LEFT, lambda: self.on_move((-1, 0)))
        engine.connect_keydown(pygame.K_ESCAPE, self.on_escape)
        self._render()

    def on_move(self, shift):
        """Attempts to make a move"""
        move(self.level, shift)
        self._render()
        if check_win(self.level):
            animate_goals(self._render)
            return False

    def on_escape(self):
        """Notifies engine to stop"""
        return False

    def _render(self, invert=False):
        """Draws all game objects"""
        with self.screen.draw() as drawer:
            render(drawer, self.level, invert)

def render(drawer, level, invert):
    tile_to_color = {
        Tile.FLOOR: Color.LBLUE,
        Tile.WALL: Color.RED,
        Tile.BOX: Color.BROWN,
    }
    for pos, tile in level:
        color_ = tile_to_color[tile.kind]
        if invert and tile.goal:
            color_ = color_[1], color_[0], color_[2]
        drawer.square(pos, color_)
        if tile.goal:
            drawer.diamond(pos, color_)
    drawer.circle(level.player, Color.YELLOW)

def animate_goals(renderer):
    for i in range(10):
        renderer(i)
        time.sleep(0.050)

def move(level, shift):
    start = numtup(level.player)
    end = start + shift
    pastend = end + shift
    if level[end].kind == Tile.FLOOR:
        level.player = end
    elif level[end].kind == Tile.BOX and level[pastend].kind == Tile.FLOOR:
        level[end].kind = Tile.FLOOR
        level[pastend].kind = Tile.BOX
        level.player = end

def check_win(level):
    for pos, tile in level:
        isbox = tile.kind == Tile.BOX
        isgoal = tile.goal
        if isbox != isgoal:
            return False
    return True
