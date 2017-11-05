import mock
import inspect
import pytest
import pygame
from types import ModuleType
from app.engine import Engine, Screen, Drawer
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
def pygscr():
    scr = mock.Mock()
    screens = [scr]
    pygame.display.set_mode.side_effect = lambda _: screens.pop(0)
    return scr

def test_engine_init(events):
    eng = Engine()

    pygame.init.assert_called_once()

def test_engine_screen_init():
    eng = Engine()

    scr = eng.screen((5, 3))

    pygame.display.set_mode.assert_called_once_with((100, 60))

def test_engine_redraw(pygscr):
    screen = Screen(geometry=(10, 10))
    
    with screen.draw() as drawer:
        drawer.square((0,0), Color.RED)

    pygscr.fill.assert_called_once()
    pygame.display.flip.assert_called_once()

def test_screen_renders_square(pygscr):
    drawer = Drawer(pygscr)

    drawer.square((4,2), Color.RED)

    pygame.draw.rect.assert_called_once_with(pygscr, mock.ANY, (80, 40, 20, 20))

def test_screen_renders_circle(pygscr):
    drawer = Drawer(pygscr)

    drawer.circle((1,1), Color.YELLOW)

    pygame.draw.circle.assert_called_once_with(pygscr, mock.ANY, (30, 30), mock.ANY)

def test_screen_renders_diamond(pygscr):
    drawer = Drawer(pygscr)

    drawer.diamond((2,2), Color.BLUE)

    pygame.draw.aalines.assert_called_once_with(pygscr, mock.ANY, mock.ANY, mock.ANY)

def test_engine_stops_on_quit(events):
    eng = Engine()

    events.push(pygame.QUIT)
    eng.run()

def test_engine_ignores_unconnected_keydown(events):
    eng = Engine()

    events.push(pygame.KEYDOWN, key=pygame.K_RIGHT)
    events.push(pygame.QUIT)
    eng.run()

def test_engine_calls_keydown_actions(events):
    action = mock.MagicMock()
    eng = Engine()
    eng.connect_keydown(pygame.K_LEFT, action)

    events.push(pygame.KEYDOWN, key=pygame.K_LEFT)
    events.push(pygame.QUIT)
    eng.run()

    action.assert_called_once_with()

def test_engine_stops_on_action_returning_false(events):
    def action():
        return False
    eng = Engine()
    eng.connect_keydown(pygame.K_ESCAPE, action)

    events.push(pygame.KEYDOWN, key=pygame.K_ESCAPE)
    eng.run()
