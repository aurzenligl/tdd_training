import pytest
from digraph import Digraph

'''
Previous test:
    - was 56 lines long, it didn't fit on one screen
    - had actions between asserts
It's difficult to reason about testcase like this.
It's very difficult to hunt corner cases in tests like this.
It's extremely difficult to figure out what went wrong when such test fails.
We can do better than this.
'''

class TestDigraph(object):
    '''
    When any part of graph logic is broken, particular test or group of tests
    will fail. When new functionality is added, it can be added without damaging
    previous tests.
    '''

    def test_empty(self):
        g = Digraph()

        assert len(g.nodes) == 0
        assert len(g.edges) == 0

    def test_missing_node(self):
        g = Digraph()

        with pytest.raises(Exception) as e:
            g.node('missing')

    def test_missing_edge(self):
        g = Digraph()

        with pytest.raises(Exception) as e:
            g.edge('missing')

    '''
    This is first test when you clearly see the structure:
        - given: setup part, create things by calling functions we know work correctly
        - when: action, side-effects and results of which we'll assert
        - then: checking part
    '''
    def test_one_node(self):
        g = Digraph()

        n = g.add_node('N')

        assert len(g.nodes) == 1
        assert g.node('N') is n

    def test_removed_node(self):
        g = Digraph()
        n = g.add_node('N')

        g.remove_node(n)

        assert len(g.nodes) == 0

    def test_one_edge(self):
        g = Digraph()
        n1 = g.add_node('N1')
        n2 = g.add_node('N2')

        e = g.add_edge(n1, n2, 'E')

        assert len(g.edges) == 1
        assert g.edge('E') is e
        assert e.nodes == (n1, n2)

        assert n1.head_nodes == []
        assert n1.head_edges == []
        assert n1.tail_nodes == [n2]
        assert n1.tail_edges == [e]
        assert n2.head_nodes == [n1]
        assert n2.head_edges == [e]
        assert n2.tail_nodes == []
        assert n2.tail_edges == []

    def test_removed_edge(self):
        g = Digraph()
        n1 = g.add_node('N1')
        n2 = g.add_node('N2')
        e = g.add_edge(n1, n2, 'E')

        g.remove_edge(e)

        assert len(g.nodes) == 2
        assert len(g.edges) == 0

        assert n1.head_nodes == []
        assert n1.head_edges == []
        assert n1.tail_nodes == []
        assert n1.tail_edges == []
        assert n2.head_nodes == []
        assert n2.head_edges == []
        assert n2.tail_nodes == []
        assert n2.tail_edges == []

'''
Test suite structure: Python's dynamically interpreted nature
and introspection allow to detect testcases and test modules on the fly,
which allows easy organization of test code.

- function:
    Single testcase should test single action in single context.
    It's name should indicate the feature or aspect it tries to test.

- class:
    One can use class as a means to separate groups of testcases.
    Test class can indicate a separate class is tested, or different
    kind of testing is performed.

- module:
    These "fixed" tests occupy a module (a .py file), next to "broken" test.
    Both will run if pytest is executed in this directory.

- directory:
    Next to this directory are other directories with tests, which allows
    to structure test suite deeply and allow for a vast amount of unit tests.
    Enough to reach 90% coverage of the project.
'''

class TestNode(object):
    def test_label(self):
        n = Digraph().add_node('N')

        assert n.label == 'N'

    def test_repr(self):
        n = Digraph().add_node('N')

        assert repr(n) == '<Node N>'

class TestEdge(object):

    '''
    Test setup may become a boilerplate code easily.
    When this happens, use "fixture" as a means for test setup.
    A set of fixtures can be defined and then some of these may be
    used in test functions in any combination. Fixtures may use
    other fixtures, and their scope may vary. Read more here:
    https://docs.pytest.org/en/latest/fixture.html
    '''
    @pytest.fixture
    def edge(self):
        g = Digraph()
        n1 = g.add_node('N1')
        n2 = g.add_node('N2')
        yield g.add_edge(n1, n2, 'E')

    def test_label(self, edge):
        assert edge.label == 'E'

    def test_repr(self, edge):
        assert repr(edge) == '<Edge E>'

'''
Simple cases of one node and one edge may not be enough.
It might be wise to separate those from more involved tests
with more complicated graph structures and scenarios.

If simple tests fail, problem should be easy to find and most
probably is trivial. If only complex tests fail, you know you're
looking for something contrived, because obvious stuff works all right.
'''

class TestComplex(object):
    @pytest.fixture
    def graph(self):
        '''
         --e1-> n2 --e2->
        n1 -----e3-----> n3
         -------e4------>
        '''
        g = Digraph()
        n1 = g.add_node('N1')
        n2 = g.add_node('N2')
        n3 = g.add_node('N3')
        g.add_edge(n1, n2, 'E1')
        g.add_edge(n2, n3, 'E2')
        g.add_edge(n1, n3, 'E3')
        g.add_edge(n1, n3, 'E4')
        yield g

    def test_remove_edge(self, graph):
        n1, n2, n3 = graph.nodes

        graph.remove_edge(graph.edge('E3'))

        assert len(graph.nodes) == 3
        assert len(graph.edges) == 3

        assert n1.head_nodes == []
        assert n1.tail_nodes == [n2, n3]
        assert n3.head_nodes == [n2, n1]
        assert n3.tail_nodes == []

    def test_remove_connected_node(self, graph):
        n1, n2, n3 = graph.nodes

        graph.remove_node(n2)

        assert len(graph.nodes) == 2
        assert len(graph.edges) == 2

        assert n1.head_nodes == []
        assert n1.tail_nodes == [n3, n3]
        assert n3.head_nodes == [n1, n1]
        assert n3.tail_nodes == []
