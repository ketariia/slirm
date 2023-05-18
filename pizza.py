class Pizza:
    def __init__(self, name):
        self.name = name
        self.ingredients = []

    def __str__(self):
        return f"{self.name}: {', '.join(self.ingredients)}"

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)


class PizzaDecorator(Pizza):
    def __init__(self, pizza):
        self.name = pizza.name
        self.ingredients = pizza.ingredients
        self.pizza = pizza

    def __str__(self):
        return str(self.pizza)


class Margherita(Pizza):
    def __init__(self):
        super().__init__("Margherita")
        self.add_ingredient("tomato sauce")
        self.add_ingredient("mozzarella cheese")


class Hawaiian(Pizza):
    def __init__(self):
        super().__init__("Hawaiian")
        self.add_ingredient("tomato sauce")
        self.add_ingredient("mozzarella cheese")
        self.add_ingredient("ham")
        self.add_ingredient("pineapple")


class Regina(Pizza):
    def __init__(self):
        super().__init__("Regina")
        self.add_ingredient("tomato sauce")
        self.add_ingredient("mozzarella cheese")
        self.add_ingredient("ham")
        self.add_ingredient("mushrooms")


class Vegetarian(Pizza):
    def __init__(self):
        super().__init__("Vegetarian")
        self.add_ingredient("tomato sauce")
        self.add_ingredient("mozzarella cheese")
        self.add_ingredient("mushrooms")
        self.add_ingredient("peppers")
        self.add_ingredient("onions")


class Garlic(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.add_ingredient("garlic")


class Olives(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.add_ingredient("olives")


class Spinach(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.add_ingredient("spinach")


class Avocado(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.add_ingredient("avocado")


class Feta(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.add_ingredient("feta")


class Pepperdews(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.add_ingredient("pepperdews")


hawaiian_pizza = Garlic(Olives(Spinach(Feta(Pepperdews(Margherita())))))
print(hawaiian_pizza)


