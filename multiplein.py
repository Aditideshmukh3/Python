# Multiple Inheritance :

class Father:
    def __init__(self, eyes, hair):
        self.eyes = eyes
        self.hair = hair

    def info(self):
        print("Eyes color : ", self.eyes)
        print("Hair type : ", self.hair)

class Mother:
    def __init__(self, height):
        self.height = height

    def info(self):
        print("Height is : ", self.height)

class Child(Father, Mother):
    def __init__(self, eyes, hair, height, name, talent):
        Father.__init__(self, eyes, hair)
        Mother.__init__(self, height)
        self.name = name
        self.talent = talent

    def info(self):
        Father.info(self)
        Mother.info(self)
        print("Name of child is : ", self.name)
        print("IQ of child is : ", self.talent)

s = Child("Brown", "curly", "5.7", "John", "200")
s.info()



    
        