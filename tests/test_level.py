from app.level import SquareType, Level

def test_level_empty():
    level = Level(0, 0, [])
    assert level.size() == (0, 0)
