import pytest
from occurences import count_occurences

'''
Let's try to solve the problem of many testcases or assert identical
with exception of test input and output.

Test parametrization may help here. If testcase follows a common
template and only a couple of variables change around
'''

@pytest.mark.parametrize("input, expected", [
    ([], {}),
    ([1, 1], {1: 2}),
    ([1, 2], {1: 1, 2: 1}),
], ids = [
    'empty',
    'two-same',
    'two-different'
])
def test_occurences(input, expected):
    assert count_occurences(input) == expected

@pytest.mark.parametrize("input, expected", [
    ((x for x in range(2)), {0: 1, 1: 1}),
    ((0, 1), {0: 1, 1: 1}),
    ([0, 1], {0: 1, 1: 1}),
    ({0: None, 1: None}, {0: 1, 1: 1}),
    ('foo', {'f': 1, 'o': 2})
], ids = [
    'generator',
    'tuple',
    'list',
    'dict',
    'string'
])
def test_occurences_iterable_input(input, expected):
    assert count_occurences(input) == expected

def test_occurences_heterogenous():
    x = 'abc'
    y = (7,8,9)
    z = complex(1.3, 0.2)
    assert count_occurences([z, y, y, z, x, z]) == {x: 1, y: 2, z: 3}

def test_occurences_nans():
    nan = float('nan')
    assert count_occurences([nan, nan, nan]) == {nan: 3}

def test_occurences_disallows_mutable():
    with pytest.raises(Exception) as e:
        count_occurences([[]])
