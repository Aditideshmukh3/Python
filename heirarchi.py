# Hierarchical Inheritance :

class Pet:
    def __init__(self, species, name):
        self.species = species
        self.name = name

    def details(self):
        print("I am pet")

class Cat(Pet):
    def __init__(self, species, name, age):
        Pet.__init__(self, species, name)
        self.age = age  

    def details(self):
        print("My age is : ", self.age)
        return super().details()

class Dog(Pet):        
    def __init__(self, species, name, breed):
        Pet.__init__(self, species, name)
        self.breed = breed  

    def details(self):
        print("My breed is : ", self.breed)
        return super().details()


c = Cat("cat", "Kitty", 1)
c.details()

d = Dog("Dog", "Tommy", "Labrador")
d.details()