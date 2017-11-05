import pytest
from app.level import Tile, Level

F = Tile.FLOOR
W = Tile.WALL
B = Tile.BOX

def make_example_level():
    return Level((3, 2), ' %o'
                         '@o.')

def test_tile_repr():
    assert repr(Tile(Tile.FLOOR)) == '<Tile(f)>'
    assert repr(Tile(Tile.WALL)) == '<Tile(w)>'
    assert repr(Tile(Tile.BOX)) == '<Tile(b)>'
    assert repr(Tile(Tile.FLOOR, goal=True)) == '<Tile(F)>'
    assert repr(Tile(Tile.BOX, goal=True)) == '<Tile(B)>'

def test_level_filled():
    level = make_example_level()

    assert level.size == (3, 2)
    assert level[0,0].kind == F
    assert level[0,0].goal is False
    assert level[1,0].kind == W
    assert level[1,0].goal is False
    assert level[2,1].kind == F
    assert level[2,1].goal is True

def test_level_indexing():
    level = make_example_level()

    level[1,0].kind = B

    assert level[1,0].kind == B

def test_level_iteration():
    level = make_example_level()

    assert [_ for _ in level] == [
        ((0,0), level[0,0]),
        ((1,0), level[1,0]),
        ((2,0), level[2,0]),
        ((0,1), level[0,1]),
        ((1,1), level[1,1]),
        ((2,1), level[2,1]),
    ]

def test_level_player_position():
    level = make_example_level()

    assert level.player == (0, 1)

def test_level_player_position_setting():
    level = make_example_level()

    level.player = (0, 0)  # other floor
    assert level.player == (0, 0)

    level.player = (2, 1)  # goal
    assert level.player == (2, 1)

def test_level_str():
    level = make_example_level()

    assert str(level) == (
        'fwb\n'
        'fbF\n'
    )

def test_level_error_too_few_squaretypes():
    with pytest.raises(ValueError) as e:
        Level((2, 2), '@')
    assert str(e.value) == "expected 4 elements, got 1"

def test_level_error_wrong_index_read():
    with pytest.raises(ValueError) as e:
        Level((1, 1), '@')[1,0]
    assert str(e.value) == "index (1, 0) out of bounds (1, 1)"

def test_level_error_no_player():
    with pytest.raises(ValueError) as e:
        Level((3, 3), '.........')
    assert str(e.value) == "no player: '@' specified"

def test_level_error_two_players():
    with pytest.raises(ValueError) as e:
        Level((3, 3), '....@...@')
    assert str(e.value) == "multiple players: '@' specified"

def test_level_error_setting_player_not_on_floor():
    with pytest.raises(ValueError) as e:
        level = Level((2, 1), '@%')
        level.player = (1, 0)
    assert str(e.value) == "expected player on floor"

def test_level_error_invalid_tilecode():
    with pytest.raises(ValueError) as e:
        Level((3, 3), '...%%%.?@')
    assert str(e.value) == "invalid tilecode '?' on (1, 2)"
