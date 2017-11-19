from digraph import Digraph

'''
How about like this?
'''

def test_digraph():
    g = Digraph()
    n1 = g.add_node('N1')
    n2 = g.add_node('N2')
    n3 = g.add_node('N3')
    e1 = g.add_edge(n1, n2, 'E1')
    e2 = g.add_edge(n2, n3, 'E2')
    e3 = g.add_edge(n1, n3, 'E3')
    e4 = g.add_edge(n1, n3, 'E4')

    assert len(g.nodes) == 3
    assert len(g.edges) == 4
    assert g.edge('E1').nodes == (n1, n2)
    assert g.edge('E2').nodes == (n2, n3)
    assert g.edge('E3').nodes == (n1, n3)
    assert g.edge('E4').nodes == (n1, n3)
    assert g.node('N1').head_nodes == []
    assert g.node('N1').head_edges == []
    assert g.node('N1').tail_nodes == [n2, n3, n3]
    assert g.node('N1').tail_edges == [e1, e3, e4]
    assert g.node('N2').head_nodes == [n1]
    assert g.node('N2').head_edges == [e1]
    assert g.node('N2').tail_nodes == [n3]
    assert g.node('N2').tail_edges == [e2]
    assert g.node('N3').head_nodes == [n2, n1, n1]
    assert g.node('N3').head_edges == [e2, e3, e4]
    assert g.node('N3').tail_nodes == []
    assert g.node('N3').tail_edges == []

    g.remove_node(n2)

    assert len(g.nodes) == 2
    assert len(g.edges) == 2
    assert g.edge('E3').nodes == (n1, n3)
    assert g.edge('E4').nodes == (n1, n3)
    assert g.node('N1').head_nodes == []
    assert g.node('N1').head_edges == []
    assert g.node('N1').tail_nodes == [n3, n3]
    assert g.node('N1').tail_edges == [e3, e4]
    assert g.node('N3').head_nodes == [n1, n1]
    assert g.node('N3').head_edges == [e3, e4]
    assert g.node('N3').tail_nodes == []
    assert g.node('N3').tail_edges == []

    g.remove_edge(e3)

    assert len(g.nodes) == 2
    assert len(g.edges) == 1
    assert g.edge('E4').nodes == (n1, n3)
    assert g.node('N1').head_nodes == []
    assert g.node('N1').head_edges == []
    assert g.node('N1').tail_nodes == [n3]
    assert g.node('N1').tail_edges == [e4]
    assert g.node('N3').head_nodes == [n1]
    assert g.node('N3').head_edges == [e4]
    assert g.node('N3').tail_nodes == []
    assert g.node('N3').tail_edges == []
