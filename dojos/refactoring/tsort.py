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

def tsort(depvects):
    nodes = []
    for depvec in depvects:
        name = depvec[0]
        deps = depvec[1:]
        node = Node(name, deps)
        nodes.append(node)

    known = set()
    index = 0
    while index < len(nodes):
        if not rotate(nodes, index, known):
            index += 1

    out = []
    for node in nodes:
        depvect = []
        depvect.append(node.name)
        depvect.extend(node.dependencies)
        out.append(depvect)
    return out
