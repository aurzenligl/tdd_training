import sys

if sys.version < '3':
    from itertools import ifilter
else:
    ifilter = filter

from itertools import islice

class Node():
    def __init__(self, name, dependencies):
        self.name = name
        self.dependencies = dependencies

def rotate(nodes, index, known):
    node = nodes[index]
    for dep in node.dependencies:
        if dep not in known:
            found_index, found = next(ifilter(lambda x: x[1].name == dep,
                                      enumerate(islice(nodes, index + 1, None), start = index + 1)))
            nodes.insert(index, nodes.pop(found_index))
            return True
    known.add(node.name)
    return False

def tsort(text_nodes):
    nodes = [Node(text_node[0], text_node[1:])  for text_node in text_nodes]
    known = set()
    index = 0
    max_index = len(nodes)
    while index < max_index:
        if not rotate(nodes, index, known):
            index += 1
    out_nodes = [[x.name] + x.dependencies for x in nodes]
    return out_nodes
