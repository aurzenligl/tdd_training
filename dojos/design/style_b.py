# code example from lxml project:
# https://github.com/lxml/lxml/blob/master/src/lxml/_elementpath.py

def prepareStar(following, tag):
    def findElems(result):
        for elem in result:
            for e in elem.iterchildren('*'):
                yield e
    return findElems

def prepare_self(_, __):
    def select(object_):
        return object_
    return select

def PrepareDescendant(Next, Token):
    Token = Next()
    if Token[0] == "*":
        Star = "*"
    elif not Token[0]:
        Star = Token[1]
    else:
        raise SyntaxError("invalid descendant")
    def Sequence(Result):
        for E in Result:
            for Element in E.iterdescendants(Star):
                yield Element
    return Sequence





















'''
A bit of consistency goes a long way. Consistency allows to
spot patterns much more easily - be it differentiation between classes, modules,
functions or variables, or recognizing larger scale concepts established
within given application or library.

PEP8 is a proposition on how Python code could be styled, it's a good idea
to take a look at it and evaluate.
'''

def prepare_star(next, token):
    def select(result):
        for elem in result:
            for e in elem.iterchildren('*'):
                yield e
    return select

def prepare_self(next, token):
    def select(result):
        return result
    return select

def prepare_descendant(next, token):
    token = next()
    if token[0] == "*":
        tag = "*"
    elif not token[0]:
        tag = token[1]
    else:
        raise SyntaxError("invalid descendant")
    def select(result):
        for elem in result:
            for e in elem.iterdescendants(tag):
                yield e
    return select
