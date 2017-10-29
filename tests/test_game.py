import pytest
from app.level import Level, SquareType
from app.game import Game

@pytest.fixture
def level():
    S = SquareType.SPACE
    W = SquareType.WALL
    B = SquareType.BOX
    squares = [
        W, W, W, W, W,
        W, S, B, S, W,
        W, S, S, S, W,
        W, W, W, W, W,
    ]
    return Level(5, 4, squares)

def test_game_size(level):
    game = Game(level)

    assert game.size() == (5, 4)
