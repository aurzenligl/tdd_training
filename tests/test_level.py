from app.level import SquareType, Level

S = SquareType.SPACE
W = SquareType.WALL

def test_level_empty():
    level = Level(0, 0, [])
    assert level.size() == (0, 0)

def test_level_filled():
    level = Level(2, 3, [S, W, S, W, W, S])
    assert level.size() == (2, 3)
