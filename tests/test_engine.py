import mock
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
    return mock.Mock()

def test_engine_init(game):
    eng = Engine(game)

    pygame.init.assert_called_once()
