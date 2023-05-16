import random

class Shape:
    def draw(self):
        pass

    def erase(self):
        pass

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

class ShapeFactory:
    @staticmethod
    def create_circle():
        return Circle()

    @staticmethod
    def create_square():
        return Square()

    @staticmethod
    def create_triangle():
        return Triangle()

def shapeNameGen(n):
    for i in range(n):
        shape_factory = random.choice([ShapeFactory.create_circle, ShapeFactory.create_square, ShapeFactory.create_triangle])
        yield shape_factory()

if __name__ == '__main__':
    for shape in shapeNameGen(7):
        shape.draw()
        shape.erase()
