import pytest
from app.level import SquareType, Level

S = SquareType.SPACE
W = SquareType.WALL
B = SquareType.BOX

def make_example_level():
    tiles = [S, W, B,
             S, B, W]
    return Level((3, 2), tiles, (0, 1))

def test_level_filled():
    level = make_example_level()

    assert level.size == (3, 2)
    assert level[0,0] == S
    assert level[1,0] == W
    assert level[1,1] == B

def test_level_indexing():
    level = make_example_level()

    level[1,0] = B

    assert level[1,0] == B

def test_level_iteration():
    level = make_example_level()

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

    assert level.player == (0, 1)

def test_level_error_too_few_squaretypes():
    with pytest.raises(ValueError) as e:
        Level((2, 2), [S], (0,0))
    assert str(e.value) == "expected 4 elements, got 1"

def test_level_error_wrong_index_read():
    with pytest.raises(ValueError) as e:
        Level((1, 1), [S], (0,0))[1,0]
    assert str(e.value) == "index (1, 0) out of bounds (1, 1)"

def test_level_error_wrong_index_write():
    with pytest.raises(ValueError) as e:
        Level((1, 1), [S], (0,0))[1,0] = S
    assert str(e.value) == "index (1, 0) out of bounds (1, 1)"

def test_level_error_nonexistent_player_position():
    with pytest.raises(ValueError) as e:
        Level((1, 1), [S], (3,4))
    assert str(e.value) == "player position (3, 4) out of bounds (1, 1)"

def test_level_error_player_not_on_space():
    with pytest.raises(ValueError) as e:
        Level((1, 1), [W], (0,0))
    assert str(e.value) == "expected player on empty space"
