import mock
import inspect
import pytest
import pygame
from types import ModuleType
from app.engine import Engine
from app.game import Direction
from app.color import Color

@pytest.fixture(autouse=True)
def mock_pygame(mocker):
    def mockable(name, val):
        if getattr(val, '_NOT_IMPLEMENTED_', None):  # to silence pygame.MissingModule access warning
            return False
        if name.startswith('_'):
            return False
        return callable(val) or isinstance(val, ModuleType)

    for name in [name for (name, val) in vars(pygame).items() if mockable(name, val)]:
        mocker.patch('pygame.' + name)

@pytest.fixture
def events():
    class Event():
        def __init__(self, type_, key):
            self.type = type_
            self.key = key

    class EventQueue():
        def __init__(self):
            self.events = []
        def push(self, type_, key=None):
            self.events.append(Event(type_, key=key))
        def pop(self):
            return [self.events.pop(0)]

    eq = EventQueue()
    pygame.event.get.side_effect = eq.pop
    return eq

@pytest.fixture
def screen():
    scr = mock.Mock()
    screens = [scr]
    pygame.display.set_mode.side_effect = lambda _: screens.pop(0)
    return scr

@pytest.fixture
def game():
    class GameFake():
        def __init__(self):
            self.on_move = mock.Mock()
        def size(self):
            return 5, 3
        def on_render(self, drawer):
            drawer.square((0,0), Color.RED)
            drawer.square((4,2), Color.RED)
            drawer.circle((1,1), Color.YELLOW)
            drawer.diamond((2,2), Color.BLUE)

    return GameFake()

def test_engine_init(game, events):
    events.push(pygame.QUIT)
    eng = Engine(game)

    eng.run()

    pygame.init.assert_called_once()
    pygame.display.set_mode.assert_called_once_with((100, 60))

def test_engine_renders(game, events, screen):
    events.push(pygame.QUIT)
    eng = Engine(game)

    eng.run()

    screen.fill.assert_called_once()
    pygame.draw.rect.assert_any_call(screen, mock.ANY, (0, 0, 20, 20))
    pygame.draw.rect.assert_any_call(screen, mock.ANY, (80, 40, 20, 20))
    pygame.draw.circle.assert_any_call(screen, mock.ANY, mock.ANY, mock.ANY)
    pygame.draw.aalines.assert_any_call(screen, mock.ANY, mock.ANY, mock.ANY)
    pygame.display.flip.assert_called_once()

def test_engine_relays_move_keypresses(game, events):
    events.push(pygame.KEYDOWN, key=pygame.K_LEFT)
    events.push(pygame.KEYDOWN, key=pygame.K_k)
    events.push(pygame.KEYDOWN, key=pygame.K_UP)
    events.push(pygame.QUIT)
    eng = Engine(game)

    eng.run()

    assert game.on_move.call_count == 2
    game.on_move.assert_any_call(Direction.LEFT)
    game.on_move.assert_any_call(Direction.UP)
