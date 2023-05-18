class Pizza:
    def __init__(self):
        self.description = "Unknown Pizza"

    def get_description(self):
        return self.description

    def get_cost(self):
        pass

class Margherita(Pizza):
    def __init__(self):
        Pizza.__init__(self)
        self.description = "Margherita"

    def get_cost(self):
        return 5.99

class Hawaiian(Pizza):
    def __init__(self):
        Pizza.__init__(self)
        self.description = "Hawaiian"

    def get_cost(self):
        return 8.99

class Regina(Pizza):
    def __init__(self):
        Pizza.__init__(self)
        self.description = "Regina"

    def get_cost(self):
        return 7.99

class Vegetarian(Pizza):
    def __init__(self):
        Pizza.__init__(self)
        self.description = "Vegetarian"

    def get_cost(self):
        return 6.99

class PizzaDecorator(Pizza):
    def __init__(self, pizza):
        Pizza.__init__(self)
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.pizza.get_cost()

class Garlic(PizzaDecorator):
    def __init__(self, pizza):
        PizzaDecorator.__init__(self, pizza)
        self.description = "Garlic"

    def get_description(self):
        return self.pizza.get_description() + ", Garlic"

    def get_cost(self):
        return self.pizza.get_cost() + 0.50

class Olives(PizzaDecorator):
    def __init__(self, pizza):
        PizzaDecorator.__init__(self, pizza)
        self.description = "Olives"

    def get_description(self):
        return self.pizza.get_description() + ", Olives"

    def get_cost(self):
        return self.pizza.get_cost() + 0.75

class Spinach(PizzaDecorator):
    def __init__(self, pizza):
        PizzaDecorator.__init__(self, pizza)
        self.description = "Spinach"

    def get_description(self):
        return self.pizza.get_description() + ", Spinach"

    def get_cost(self):
        return self.pizza.get_cost() + 1.25

class Avocado(PizzaDecorator):
    def __init__(self, pizza):
        PizzaDecorator.__init__(self, pizza)
        self.description = "Avocado"

    def get_description(self):
        return self.pizza.get_description() + ", Avocado"

    def get_cost(self):
        return self.pizza.get_cost() + 1.50

class Feta(PizzaDecorator):
    def __init__(self, pizza):
        PizzaDecorator.__init__(self, pizza)
        self.description = "Feta"

    def get_description(self):
        return self.pizza.get_description() + ", Feta"

    def get_cost(self):
        return self.pizza.get_cost() + 1.00

class Pepperdews(PizzaDecorator):
    def __init__(self, pizza):
        PizzaDecorator.__init__(self, pizza)
        self.description = "Pepperdews"

    def get_description(self):
        return self.pizza.get_description() + ", Pepperdews"

    def get_cost(self):
        return self.pizza.get_cost() + 1.50

my_pizza = Hawaiian()
my_pizza = Garlic(my_pizza)
my_pizza = Feta(my_pizza)
my_pizza = Pepperdews(my_pizza)
my_pizza = Spinach(my_pizza)
my_pizza = Olives(my_pizza)
print("My pizza: " + my_pizza.get_description())
print("Total cost: $" + str(my_pizza.get_cost()))
