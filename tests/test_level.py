import pytest
from app.level import SquareType, Level

S = SquareType.SPACE
W = SquareType.WALL
B = SquareType.BOX

def make_example_level():
    level = Level(3, 2, [S, W, B, S, B, W], player=(3, 0))

def test_level_empty():
    level = Level(0, 0, [])

    assert level.size() == (0, 0)

def test_level_filled():
    level = Level(3, 2, [S, W, S, S, S, B])

    assert level.size() == (3, 2)
    assert level[0,0] == S
    assert level[1,0] == W
    assert level[2,1] == B

def test_level_indexing():
    level = Level(2, 2, [S, S, S, S])

    level[1,0] = W

    assert level[1,0] == W

def test_level_iteration():
    level = Level(3, 2, [S, W, B, S, B, W])

    assert [_ for _ in level] == [
        ((0,0), S),
        ((1,0), W),
        ((2,0), B),
        ((0,1), S),
        ((1,1), B),
        ((2,1), W),
    ]

def test_level_player_position():
    level = make_example_level()

    assert level.player() == (3, 0)

def test_level_errors():
    with pytest.raises(ValueError) as e:
        Level(1, 1, [])
    assert str(e.value) == "expected 1 elements, got 0"

    with pytest.raises(ValueError) as e:
        Level(1, 1, [W])[1,0]
    assert str(e.value) == "index (1,0) out of bounds (1,1)"

    with pytest.raises(ValueError) as e:
        Level(1, 1, [W])[1,0] = S
    assert str(e.value) == "index (1,0) out of bounds (1,1)"
