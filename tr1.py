from __future__ import generators
import random

class Shape(object):
    def factory(type):
        if type == 'Circle': return Circle()
        if type == 'Square': return Square()
        if type == 'Triangle': return Triangle()
        assert 0, 'Bad shape creation: ' + type
    factory = staticmethod(factory)

class Circle(Shape):
    def draw(self):
        print('Circle.draw')

    def erase(self):
        print('Circle.erase')

class Square(Shape):
    def draw(self):
        print('Square.draw')

    def erase(self):
        print('Square.erase')

class Triangle(Shape):
    def draw(self):
        print('Triangle.draw')

    def erase(self):
        print('Triangle.erase')

def shapeNameGen(n):
    types = Shape.__subclasses__()
    for i in range(n):
        yield random.choice(types).__name__

if __name__ == '__main__':
    shapes = [ Shape.factory(i) for i in shapeNameGen(7)]
    for shape in shapes:
        shape.draw()
        shape.erase()