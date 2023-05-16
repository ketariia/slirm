import random

class Shape(object):
    types = []

def factory(type):
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

    if type == 'Circle':
        return Circle()
    if type == 'Square':
        return Square()
    if type == 'Triangle':
        return Triangle()

    assert 0, 'Bad shape creation: ' + type

def shapeNameGen(n):
    for i in range(n):
        yield factory(random.choice(['Circle', 'Square', 'Triangle']))

if __name__ == '__main__':
    for shape in shapeNameGen(7):
        shape.draw()
        shape.erase()
