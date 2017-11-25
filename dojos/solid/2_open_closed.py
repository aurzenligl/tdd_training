'Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification'

import math

class Square(object):
    def __init__(self, side):
        self.side = side

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

def sum_area(shapes):
    area = 0
    for shape in shapes:
        if isinstance(shape, Square):
            area += shape.side ** 2
        else:
            area += math.pi * (shape.radius ** 2)
    return area

def max_area(shapes):
    max_ = 0
    for shape in shapes:
        if isinstance(shape, Square):
            area = shape.side ** 2
            if area > max_:
                max_ = area
        else:
            area = math.pi * (shape.radius ** 2)
            if area > max_:
                max_ = area
    return max_


















'''
Both adding new shapes and new algorithms is difficult:
    - shapes: require changing all existing algorithms
    - algorithm: requires rewriting area calculation for all existing shapes

Let's use shape objects as placeholders for area algorithms.
'''

class Square(object):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

def sum_area(shapes):
    return sum(shape.area() for shape in shapes)

def max_area(shapes):
    return max(shape.area() for shape in shapes)

shapes = [
    Square(3),
    Circle(2),
    Circle(5),
    Square(6),
]

print(sum_area(shapes))
print(max_area(shapes))

'''Adding new algorithms and shapes is easy'''

class Rectangle(object):
    def __init__(self, sides):
        self.sides = sides

    def area(self):
        return self.sides[0] * self.sides[1]

def min_area(shapes):
    return min(shape.area() for shape in shapes)

shapes.append(Rectangle((2,3)))

print(sum_area(shapes))
print(min_area(shapes))
