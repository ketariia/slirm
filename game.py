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

class GameEnvironment:
    def __init__(self, factory):
        self.factory = factory

    def play(self):
        shape = self.factory()
        shape.draw()
        shape.erase()

class GnomesAndFaires:
    @staticmethod
    def get_factory():
        return random.choice([ShapeFactory.create_circle, ShapeFactory.create_square, ShapeFactory.create_triangle])

    def __init__(self):
        self.env = GameEnvironment(GnomesAndFaires.get_factory)

    def run(self):
        for i in range(7):
            self.env.play()

if __name__ == '__main__':
    game = GnomesAndFaires()
    game.run()
