# Single Inheritance :


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("Name of the employee is : ", self.name)
        print("Age of the employee is : ", self.age)

# e = Employee("Alice", 30)
# e.info()

class Trainer(Employee):
    def __init__(self, name, age, role):
        Employee.__init__(self, name, age)
        self.role = role 

    def info(self):
        Employee.info(self)
        print("Role of the employee is : ", self.role)

t = Trainer("Max", 25, "Python Trainer")
t.info()


# Multilevel Inheritance :


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("Name of the employee is : ", self.name)
        print("Age of the employee is : ", self.age)

# e = Employee("Alice", 30)
# e.info()

class Trainer(Employee):
    def __init__(self, name, age, role):
        Employee.__init__(self, name, age)
        self.role = role 

    def info(self):
        Employee.info(self)
        print("Role of the employee is : ", self.role)

# t = Trainer("Max", 25, "Python Trainer")
# t.info()

class Manager(Trainer):
    def __init__(self, name, age, role, salary):
        Trainer.__init__(self, name, age, role)
        self.salary = salary

    def info(self):
        # return super().info() 
        # print("Salary of the employee is : ", self.salary) 
        Trainer.info(self)
m = Manager("John", 25, "Project Manager", 50000)
m.info()  
        