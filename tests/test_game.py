import mock
import pytest
from app.level import Level, Tile
from app.game import Game, Direction, Move
from app.color import Color

S = Tile.SPACE
W = Tile.WALL
B = Tile.BOX
Y = Color.YELLOW

@pytest.fixture
def level():
    squares = [
        W, W, W, W, W,
        W, S, B, S, W,
        W, S, S, S, W,
        W, W, W, W, W,
    ]
    return Level((5,4), squares, player=(1,1))

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
    drawer.circle.assert_any_call((1,1), Y)

@pytest.mark.parametrize("movement, endpos", [
    (Direction.UP, (1, 0)),
    (Direction.DOWN, (1, 2)),
    (Direction.LEFT, (0, 1)),
    (Direction.RIGHT, (2, 1))
])
def test_game_movement_illegal(level, movement, endpos):
    level = Level((3,3), player=(1,1), tiles=[
        W, W, W,
        W, S, W,
        W, W, W,
    ])
    game = Game(level)

    move = game.on_move(movement)

    assert move.type == Move.ILLEGAL
    assert move.start == (1, 1)
    assert move.end == endpos
    assert level.player == (1, 1)
