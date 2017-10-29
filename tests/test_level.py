from app.level import SquareType, Level

S = SquareType.SPACE
W = SquareType.WALL
P = SquareType.PLAYER

def test_level_empty():
    level = Level(0, 0, [])
    assert level.size() == (0, 0)

def test_level_filled():
    level = Level(3, 2, [S, W, S, S, S, P])
    assert level.size() == (3, 2)
    assert level[0,0] == S
    assert level[1,0] == W
    assert level[2,1] == P
