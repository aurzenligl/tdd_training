import pytest
from app.numtup import numtup

@pytest.mark.parametrize('expr,res', [
    (numtup((1, 2)) + 3, (4, 5)),
    (numtup((1, 2)) + (1, 5), (2, 7)),
    (numtup((1, 2, 3)) + 1, (2, 3, 4)),
    (numtup((1, 2, 3)) + (3, 2, 1), (4, 4, 4)),
])
def test_numtup_add(expr, res):
    assert expr == res
    assert isinstance(expr, numtup)

@pytest.mark.parametrize('expr,res', [
    (numtup((1, 2)) * 3, (3, 6)),
    (numtup((1, 2)) * (1, 5), (1, 10)),
    (numtup((1, 2, 3)) * 2, (2, 4, 6)),
    (numtup((1, 2, 3)) * (3, 2, 1), (3, 4, 3)),
])
def test_numtup_mul(expr, res):
    assert expr == res
    assert isinstance(expr, numtup)
