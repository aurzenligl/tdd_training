import mock
import pytest
from app.level import Level, Tile
from app.game import Game, Direction, Move

@pytest.fixture
def level():
    return Level((5,4), '%%%%%'
                        '%@o %'
                        '% ..%'
                        '%%%%%')

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
        for m in range(4):
            drawer.square.assert_any_call((n,m), mock.ANY)
    drawer.circle.assert_any_call((1,1), mock.ANY)
    drawer.diamond.assert_any_call((2,2), mock.ANY)
    drawer.diamond.assert_any_call((3,2), mock.ANY)

@pytest.mark.parametrize("movement, endpos", [
    (Direction.UP, (1, 0)),
    (Direction.DOWN, (1, 2)),
    (Direction.LEFT, (0, 1)),
    (Direction.RIGHT, (2, 1))
])
def test_game_movement_illegal(level, movement, endpos):
    level = Level((3,3), '%%%'
                         '%@%'
                         '%%%')
    game = Game(level)

    move = game.on_move(movement)

    assert move.type == Move.ILLEGAL
    assert move.start == (1, 1)
    assert move.end == endpos
    assert level.player == (1, 1)

@pytest.mark.parametrize("movement, endpos", [
    (Direction.UP, (1, 0)),
    (Direction.DOWN, (1, 2)),
    (Direction.LEFT, (0, 1)),
    (Direction.RIGHT, (2, 1))
])
def test_game_movement_walk(level, movement, endpos):
    level = Level((3,3), '% %'
                         '.@.'
                         '% %')
    game = Game(level)

    move = game.on_move(movement)

    assert move.type == Move.WALK
    assert move.start == (1, 1)
    assert move.end == endpos
    assert level.player == endpos

@pytest.mark.parametrize("movement, endpos, endboxpos", [
    (Direction.UP, (2, 1), (2, 0)),
    (Direction.DOWN, (2, 3), (2, 4)),
    (Direction.LEFT, (1, 2), (0, 2)),
    (Direction.RIGHT, (3, 2), (4, 2))
])
def test_game_movement_push(level, movement, endpos, endboxpos):
    level = Level((5,5), '%%.%%'
                         '%%o%%'
                         ' o@o '
                         '%%o%%'
                         '%%.%%')
    game = Game(level)

    move = game.on_move(movement)

    assert move.type == Move.PUSH
    assert move.start == (2, 2)
    assert move.end == endpos
    assert level.player == endpos
    assert level[endpos].tile == Tile.FLOOR
    assert level[endboxpos].tile == Tile.BOX

@pytest.mark.parametrize("movement, endpos, pastendpos, pastendtile", [
    (Direction.UP, (2, 1), (2, 0), Tile.WALL),
    (Direction.DOWN, (2, 3), (2, 4), Tile.WALL),
    (Direction.LEFT, (1, 2), (0, 2), Tile.BOX),
    (Direction.RIGHT, (3, 2), (4, 2), Tile.BOX)
])
def test_game_movement_illegal_push(level, movement, endpos, pastendpos, pastendtile):
    level = Level((5,5), '%%%%%'
                         '%%o%%'
                         'oo@oo'
                         '%%o%%'
                         '%%%%%')
    game = Game(level)

    move = game.on_move(movement)

    assert move.type == Move.ILLEGAL
    assert move.start == (2, 2)
    assert move.end == endpos
    assert level.player == (2, 2)
    assert level[endpos].tile == Tile.BOX
    assert level[pastendpos].tile == pastendtile
