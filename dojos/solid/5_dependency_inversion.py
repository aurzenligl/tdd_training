'''
1. High-level modules should not depend on low-level modules. Both should depend on abstractions.
2. Abstractions should not depend on details. Details should depend on abstractions.
'''

class XmlParser(object):
    def __init__(self, pedantic=False):
        self.pedantic = pedantic

    def parse(self, content):
        return ['', '']

def to_canonical(model):
    return model


def read(path):
    content = open(path).read()
    parser = XmlParser()
    model = parser.parse(content)
    canonical = to_canonical(model)
    return canonical






























'''
Having coded specific parser into read function takes away a nice customization point in "read" algorithm.

If this parser was somehow defined elsewhere and injected into function, we could:
    - construct XmlParser in different ways
    - use different parsers

In Python it's astonishingly easy to come up with an interface like this.
Since variables are not typed, we can get away without a formal interface specification.
We can even define concrete parsers long after "read" is defined.
'''

def read(path, parser):
    content = open(path).read()
    model = parser.parse(content)
    canonical = to_canonical(model)
    return canonical

'''
Now "read" doesn't depend on parser code. It depends on the interface instead,
which can be implemented in a variety of ways.
'''

class YmlParser(object):
    def parse(self, content):
        return ['', '']

class JsonParser(object):
    def parse(self, content):
        return ['', '']

with open('/tmp/file', 'w') as f:
    f.write('foo')

read('/tmp/file', XmlParser())
read('/tmp/file', XmlParser(pedantic=True))
read('/tmp/file', YmlParser())
read('/tmp/file', JsonParser())

'''
If you want to be explicit and communicate presence of interface, you can define
an (otherwise unnecessary) base class which has not implemented methods.
'''

class Parser(object):
    def parse(self, content):
        '''You can document interface contrace here'''
        raise NotImplementedError

'''
And this is the "inversion" part. XmlParser from the top of this file didn't
have to conform to any interface of Parser. User had to know where to find
XmlParser and how to use it. Now XmlParser (and others) does depend on interface.
Who defines the interface? The user. Hence the inversion: provider depends on the user.
'''

class XmlParser(Parser):
    def __init__(self, pedantic=False):
        self.pedantic = pedantic

    def parse(self, content):
        return ['', '']

class YmlParser(Parser):
    def parse(self, content):
        return ['', '']

class JsonParser(Parser):
    def parse(self, content):
        return ['', '']
