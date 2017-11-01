import mock
import pytest
from app.level import Level, SquareType
from app.game import Game

S = SquareType.SPACE
W = SquareType.WALL
B = SquareType.BOX

@pytest.fixture
def level():
    squares = [
        W, W, W, W, W,
        W, S, B, S, W,
        W, S, S, S, W,
        W, W, W, W, W,
    ]
    return Level(5, 4, squares, player=(1,1))

def call_args(mock):
    return [x[:] for x in mock.call_args_list]

def test_game_size(level):
    game = Game(level)

    assert game.size() == (5, 4)

def test_game_rendering(level):
    game = Game(level)
    drawer = mock.Mock()

    game.on_render(drawer)

    for n in range(5):
        drawer.square.assert_any_call((n,0), W)
        drawer.square.assert_any_call((n,3), W)
    drawer.square.assert_any_call((1,1), S)
    drawer.square.assert_any_call((3,1), S)
    drawer.square.assert_any_call((1,2), S)
    drawer.square.assert_any_call((2,2), S)
    drawer.square.assert_any_call((1,2), S)
    drawer.square.assert_any_call((2,1), B)
