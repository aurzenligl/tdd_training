'''Types may be replaced with their subtypes without altering any of the desirable properties of type'''

class Rectangle(object):
    def __init__(self, height=0, width=0):
        self._height = height
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def area(self):
        return self.height * self.width

class Square(Rectangle):
    def __init__(self, edge=0):
        super(Square, self).__init__(edge, edge)

    @Rectangle.height.setter
    def height(self, value):
        self._height = value
        self._width = value

    @Rectangle.width.setter
    def width(self, value):
        self._height = value
        self._width = value

def copy(lhs, rhs):
    lhs.width = rhs.width
    lhs.height = rhs.height

rect1 = Square()
rect2 = Rectangle(2,4)
copy(rect1, rect2)
assert rect2.area == 16
try:
    assert rect1.area == 16
except Exception as e:
    print(type(e), str(e))













'''
Square is a Rectangle, but it's not all that Rectangle is.
We cannot exchange Square to Rectangle in program and expect it to behave properly.

We just don't use subclassing in such case. We may still have base class which
allows calculating area, bounds, drawing shape, serializing it, etc.
'''

class Shape(object):
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

class Square(Shape):
    def __init__(self, edge):
        self.edge = edge

    def area(self):
        return self.edge ** 2

def foo(shape):
    print(shape.area())

foo(Square(2))
foo(Rectangle(4,5))
