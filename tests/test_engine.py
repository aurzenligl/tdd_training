import mock
import pytest
import pygame
from types import ModuleType
from app.engine import Engine

@pytest.fixture(autouse=True)
def mock_pygame(mocker):
    def mockable(val):
        return callable(val) or isinstance(val, ModuleType)

    for var in [varname for (varname, varval) in vars(pygame).items() if mockable(varval)]:
        mocker.patch('pygame.' + var)

@pytest.fixture
def events():
    class Event():
        def __init__(self, type_):
            self.type = type_

    class EventQueue():
        def __init__(self):
            self.events = []
        def push(self, type_):
            self.events.append(Event(type_))
        def pop(self):
            return [self.events.pop(0)]

    eq = EventQueue()
    pygame.event.get.side_effect = eq.pop
    return eq

@pytest.fixture
def screen():
    scr = mock.Mock()
    screens = [scr]
    pygame.display.set_mode.side_effect = lambda _, __: screens.pop(0)
    return scr

@pytest.fixture
def game():
    class GameFake():
        def size(self):
            return 5, 3
    return GameFake()

def test_engine_init(game, events):
    events.push(pygame.QUIT)
    eng = Engine(game)

    eng.run()

    pygame.init.assert_called_once()
    pygame.display.set_mode.assert_called_once_with(100, 60)

def test_engine_renders(game, events, screen):
    events.push(pygame.QUIT)
    eng = Engine(game)

    eng.run()

    screen.fill.assert_called_once()
    pygame.display.flip.assert_called_once()
