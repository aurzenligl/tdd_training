from tsort import tsort

a = 'a'
b = 'b'
c = 'c'
d = 'd'
e = 'e'
f = 'f'

class TestTsort(object):
    def test_empty(self):
        input = []
        expected = []
        assert tsort(input) == expected

    def test_one(self):
        input = [
            [a],
        ]
        expected = [
            [a],
        ]
        assert tsort(input) == expected

    def test_one_dependency(self):
        input = [
            [a],
            [b, a],
        ]
        expected = [
            [a],
            [b, a],
        ]
        assert tsort(input) == expected

    def test_one_replace(self):
        input = [
            [b, a],
            [a],
        ]
        expected = [
            [a],
            [b, a],
        ]
        assert tsort(input) == expected

    def test_two_replaces(self):
        input = [
            [b, a],
            [a],
            [c, b],
        ]
        expected = [
            [a],
            [b, a],
            [c, b],
        ]
        assert tsort(input) == expected

    def test_nested_replaces(self):
        input = [
            [c, b],
            [b, a],
            [a],
        ]
        expected = [
            [a],
            [b, a],
            [c, b],
        ]
        assert tsort(input) == expected

    def test_multiple_dependencies_replaces(self):
        input = [
            [c, a, b],
            [b],
            [a],
        ]
        expected = [
            [a],
            [b],
            [c, a, b],
        ]
        assert tsort(input) == expected

    def test_multiple_dependencies_nested_replaces(self):
        input = [
            [c, b, a],
            [b, a],
            [a],
        ]
        expected = [
            [a],
            [b, a],
            [c, b, a],
        ]
        assert tsort(input) == expected

    def test_complex_case(self):
        input = [
            [f, d, b, a, c, d],
            [a],
            [d, b, c, a],
            [e, b, a, c],
            [b],
            [c],
        ]
        expected = [
            [b],
            [c],
            [a],
            [d, b, c, a],
            [f, d, b, a, c, d],
            [e, b, a, c],
        ]
        assert tsort(input) == expected
