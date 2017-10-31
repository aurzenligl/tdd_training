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
def game():
    class GameFake():
        def size(self):
            return 5, 3
    return GameFake()

def test_engine_init(game):
    eng = Engine(game)

    eng.run()

    pygame.init.assert_called_once()
    pygame.display.set_mode.assert_called_once_with(100, 60)
