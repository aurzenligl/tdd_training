import pytest
import pygame
from types import ModuleType
from app.engine import Engine

@pytest.fixture(autouse=True)
def mock_pygame(mocker):
    def mockable(val):
        return callable(val) or isinstance(val, ModuleType)

    for var in [varname for (varname, varval) in vars(pygame).items() if mockable]:
        mocker.patch('pygame.' + var)

@pytest.fixture
def eventq():
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
def game():
    class GameFake():
        def size(self):
            return 5, 3
    return GameFake()

def test_engine_init(game, eventq):
    eng = Engine(game)
    eventq.push(pygame.QUIT)

    eng.run()

    pygame.init.assert_called_once()
    pygame.display.set_mode.assert_called_once_with(100, 60)
