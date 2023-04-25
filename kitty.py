class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def eat(self):
        print(f"{self.name} is hungry and ready to eat.")
    def play(self):
        print(f"{self.name} is bored and looking for some fun.")
    def sharpen(self):
        print(f"{self.name} is scratching and sharpening its claws.")
        
kitty1 = Cat('Kotaru', 10)
kitty2 = Cat('Shotaru', 4)
kitty3 = Cat('Kaneda', 6)
    
kitty1.play()
kitty2.sharpen()
kitty3.eat()
