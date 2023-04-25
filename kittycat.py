class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce_self(self):
        print(f"My name is {self.name}, I am {self.age} years old:3")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

kitty1 = Cat("Mittens", 5)

kitty2 = Cat("Snowball", 2)

kitty3 = Cat("Pusheen", 3)
