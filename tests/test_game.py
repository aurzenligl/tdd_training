import mock
import pytest
import pygame
import time
from app.level import Level, Tile
from app.game import Game
from app import game

@pytest.fixture(autouse=True)
def mock_time(mocker):
    mocker.patch('time.sleep')

@pytest.fixture
def engine():
    eng = mock.Mock()
    eng.screen_mock = scr = mock.Mock()
    eng.drawer_mock = drawctx = mock.MagicMock()
    drawctx.__enter__.return_value = drawctx
    scr.draw.return_value = drawctx
    eng.screen.return_value = scr
    return eng

@pytest.fixture
def level():
    return Level((5,4), '%%%%%'
                        '%@o %'
                        '% ..%'
                        '%%%%%')

def call_args(mock):
    return [x[:] for x in mock.call_args_list]

def test_game_screen_setup(engine, level):
    game = Game(engine, level)

    engine.screen.assert_called_once_with(geometry=(5,4))
    engine.screen_mock.draw.assert_called_once_with()

def test_game_keydown_actions_setup(engine, level):
    game = Game(engine, level)

    engine.connect_keydown.assert_any_call(pygame.K_DOWN, mock.ANY)
    engine.connect_keydown.assert_any_call(pygame.K_UP, mock.ANY)
    engine.connect_keydown.assert_any_call(pygame.K_RIGHT, mock.ANY)
    engine.connect_keydown.assert_any_call(pygame.K_LEFT, mock.ANY)
    engine.connect_keydown.assert_any_call(pygame.K_ESCAPE, mock.ANY)

def test_game_move_on_action(engine, level):
    actions = {}
    engine.connect_keydown.side_effect = lambda key, action: actions.__setitem__(key, action)
    game = Game(engine, level)

    assert level.player == (1,1) 

    actions[pygame.K_UP]()
    assert level.player == (1,1)

    actions[pygame.K_LEFT]()
    assert level.player == (1,1)

    actions[pygame.K_DOWN]()
    assert level.player == (1,2)

    actions[pygame.K_RIGHT]()
    assert level.player == (2,2)

def test_game_move_ends_game(engine, level):
    level = Level((3,1), '@o.')
    game = Game(engine, level)

    assert game.on_move((1,0)) is False

def test_game_escape_action_stops(engine, level):
    actions = {}
    engine.connect_keydown.side_effect = lambda key, action: actions.__setitem__(key, action)
    game = Game(engine, level)

    assert actions[pygame.K_ESCAPE]() is False

def test_game_rendering(level):
    drawer = mock.Mock()

    game.render(drawer, level, invert=False)

    for n in range(5):
        for m in range(4):
            drawer.square.assert_any_call((n,m), mock.ANY)
    drawer.circle.assert_any_call((1,1), mock.ANY)
    drawer.diamond.assert_any_call((2,2), mock.ANY)
    drawer.diamond.assert_any_call((3,2), mock.ANY)

def test_game_rendering_inverted(level):
    squares = {}
    def add_square(pos, color_):
        squares.setdefault(pos, []).append(color_)
    drawer = mock.Mock()
    drawer.square.side_effect = add_square

    game.render(drawer, level, invert=False)
    game.render(drawer, level, invert=True)

    wall = squares[0, 0]
    floor = squares[1, 2]
    goal = squares[2, 2]
    assert wall[0] == wall[1]
    assert floor[0] == floor[1]
    assert goal[0] != goal[1]

@pytest.mark.parametrize("shift", [
    ((0, -1)),
    ((0, 1)),
    ((-1, 0)),
    ((1, 0))
])
def test_game_movement_illegal(shift):
    level = Level((3,3), '%%%'
                         '%@%'
                         '%%%')

    move = game.move(level, shift)

    assert level.player == (1, 1)

@pytest.mark.parametrize("shift, endpos", [
    ((0, -1), (1, 0)),
    ((0, 1), (1, 2)),
    ((-1, 0), (0, 1)),
    ((1, 0), (2,1))
])
def test_game_movement_walk(shift, endpos):
    level = Level((3,3), '% %'
                         ' @ '
                         '% %')

    move = game.move(level, shift)

    assert level.player == endpos

@pytest.mark.parametrize("shift, endpos, endboxpos", [
    ((0, -1), (2, 1), (2, 0)),
    ((0, 1), (2, 3), (2, 4)),
    ((-1, 0), (1, 2), (0, 2)),
    ((1, 0), (3, 2), (4, 2))
])
def test_game_movement_push(shift, endpos, endboxpos):
    level = Level((5,5), '%%.%%'
                         '%%o%%'
                         ' o@o '
                         '%%o%%'
                         '%%.%%')

    move = game.move(level, shift)

    assert level.player == endpos
    assert level[endpos].kind == Tile.FLOOR
    assert level[endboxpos].kind == Tile.BOX

@pytest.mark.parametrize("shift, endpos, pastendpos, pastendtile", [
    ((0, -1), (2, 1), (2, 0), Tile.WALL),
    ((0, 1), (2, 3), (2, 4), Tile.WALL),
    ((-1, 0), (1, 2), (0, 2), Tile.BOX),
    ((1, 0), (3, 2), (4, 2), Tile.BOX)
])
def test_game_movement_illegal_push(shift, endpos, pastendpos, pastendtile):
    level = Level((5,5), '%%%%%'
                         '%%o%%'
                         'oo@oo'
                         '%%o%%'
                         '%%%%%')

    move = game.move(level, shift)

    assert level.player == (2, 2)
    assert level[endpos].kind == Tile.BOX
    assert level[pastendpos].kind == pastendtile

def test_game_checking_winning_condition():
    level = Level((3,1), 'OO@')

    assert game.check_win(level) is True

@pytest.mark.parametrize("codes", [
    ('Oo@'),
    ('O.@'),
    ('o.@'),
])
def test_game_checking_win_when_goal_is_unsatisfied(codes):
    level = Level((3,1), codes)

    assert game.check_win(level) is False
