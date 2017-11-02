from app.numtup import numtup

def test_numtup_add():
    assert numtup((1, 2)) + 3 == (4, 5)
    assert numtup((1, 2)) + (1, 5) == (2, 7)
    assert numtup((1, 2, 3)) + 1 == (2, 3, 4)
    assert numtup((1, 2, 3)) + (3, 2, 1) == (4, 4, 4)

def test_numtup_mul():
    assert numtup((1, 2)) * 3 == (3, 6)
    assert numtup((1, 2)) * (1, 5) == (1, 10)
    assert numtup((1, 2, 3)) * 2 == (2, 4, 6)
    assert numtup((1, 2, 3)) * (3, 2, 1) == (3, 4, 3)
