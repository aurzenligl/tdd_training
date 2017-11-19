'''
Let's handle a bigger chunk of code.
How would you test a set of tightly connected classes?
'''

class Digraph(object):
    '''Directed graph with labeled nodes and edges.'''

    def __init__(self):
        self.nodes = []
        self.edges = []
        self._heads = {}
        self._tails = {}

    def add_node(self, label):
        node = Node(self, label)
        self.nodes.append(node)
        return node

    def add_edge(self, head, tail, label):
        edge = Edge(head, tail, label)
        self.edges.append(edge)
        def append(mapping, key, value):
            values = mapping.setdefault(key, [])
            values.append(value)
        append(self._heads, head, edge)
        append(self._tails, tail, edge)
        return edge

    def remove_node(self, node):
        edges = self._heads.get(node, []) + self._tails.get(node, [])
        map(self.remove_edge, edges)
        self.nodes.remove(node)

    def remove_edge(self, edge):
        self.edges.remove(edge)
        self._heads[edge.head].remove(edge)
        self._tails[edge.tail].remove(edge)

    def node(self, label):
        return next(n for n in self.nodes if n.label == label)

    def edge(self, label):
        return next(e for e in self.edges if e.label == label)

class Node(object):
    def __init__(self, graph, label):
        self._graph = graph
        self.label = label

    @property
    def head_nodes(self):
        return [e.head for e in self.head_edges]

    @property
    def head_edges(self):
        return self._graph._tails.get(self, [])

    @property
    def tail_nodes(self):
        return [e.tail for e in self.tail_edges]

    @property
    def tail_edges(self):
        return self._graph._heads.get(self, [])

    def __repr__(self):
        return '<Node %s>' % self.label

class Edge(object):
    def __init__(self, head, tail, label):
        self._head = head
        self._tail = tail
        self.label = label

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    @property
    def nodes(self):
        return self.head, self.tail

    def __repr__(self):
        return '<Edge %s>' % self.label
