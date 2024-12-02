class Animal:
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        print("Running on four legs")

class Bird(Animal):
    def move(self):
        print("Flying in the sky")

class Fish(Animal):
    def move(self):
        print("Swimming in the water")

# Create objects and call the move() method
dog = Dog()
bird = Bird()
fish = Fish()

dog.move()
bird.move()
fish.move()
