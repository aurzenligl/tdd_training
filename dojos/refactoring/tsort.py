class Node():
    def __init__(self, name, dependencies):
        self.name = name
        self.dependencies = dependencies

def rotate(nodes, index, known):
    node = nodes[index]
    for dep in node.dependencies:
        if dep not in known:
            found = (candidate for candidate in nodes[index + 1:] if candidate.name == dep).next()
            found_index = nodes.index(found)
            nodes.insert(index, nodes.pop(found_index))
            return True
    known.add(node.name)
    return False

def to_nodes(depvects):
    return [Node(depvec[0], depvec[1:])  for depvec in depvects]

def to_depvects(nodes):
    return [[node.name] + node.dependencies for node in nodes]

def tsort(depvects):
    nodes = to_nodes(depvects)
    known = set()
    index = 0
    while index < len(nodes):
        if not rotate(nodes, index, known):
            index += 1
    return to_depvects(nodes)
