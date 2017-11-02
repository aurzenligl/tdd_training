import pytest
from app.level import Tile, Level

S = Tile.SPACE
W = Tile.WALL
B = Tile.BOX
G = Tile.GOAL


def make_example_level():
    return Level((3, 2), ' %o'
                         '@o.')

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
        ((2,1), G),
    ]

def test_level_player_position():
    level = make_example_level()

    assert level.player == (0, 1)

def test_level_player_position_setting():
    level = make_example_level()

    level.player = (0, 0)  # other space
    assert level.player == (0, 0)

    level.player = (2, 1)  # goal
    assert level.player == (2, 1)

def test_level_error_too_few_squaretypes():
    with pytest.raises(ValueError) as e:
        Level((2, 2), '@')
    assert str(e.value) == "expected 4 elements, got 1"

def test_level_error_wrong_index_read():
    with pytest.raises(ValueError) as e:
        Level((1, 1), '@')[1,0]
    assert str(e.value) == "index (1, 0) out of bounds (1, 1)"

def test_level_error_wrong_index_write():
    with pytest.raises(ValueError) as e:
        Level((1, 1), '@')[1,0] = S
    assert str(e.value) == "index (1, 0) out of bounds (1, 1)"

def test_level_error_no_player():
    with pytest.raises(ValueError) as e:
        Level((3, 3), '.........')
    assert str(e.value) == "no player: '@' specified"

def test_level_error_two_players():
    with pytest.raises(ValueError) as e:
        Level((3, 3), '....@...@')
    assert str(e.value) == "multiple players: '@' specified"

def test_level_error_setting_player_not_on_space():
    with pytest.raises(ValueError) as e:
        level = Level((2, 1), '@%')
        level.player = (1, 0)
    assert str(e.value) == "expected player on empty space or goal"

def test_level_error_invalid_tilecode():
    with pytest.raises(ValueError) as e:
        Level((3, 3), '...%%%.?@')
    assert str(e.value) == "invalid tilecode '?' on (1, 2)"
