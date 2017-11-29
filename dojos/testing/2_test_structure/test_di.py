from digraph import Digraph
from digraph import Node


def test_add_nodes():
	graph = Digraph()

	a = graph.add_node('A')
	
	assert graph.node('A') == a


def test_add_edges():
	graph = Digraph()

	a = graph.add_node('A')
	b = graph.add_node('B')
	e1 = graph.add_edge(a,b,'e1')

	assert graph.edge('e1') == e1

def test_query_head_node():
	graph = Digraph()

	a = graph.add_node('A')
	b = graph.add_node('B')
	c = graph.add_node('C')

	e1 = graph.add_edge(a,b,'e1')
	e2 = graph.add_edge(b,c,'e2')

	assert a in b.head_nodes	