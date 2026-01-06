# Hybrid Inheritance Example in Python :

# Base class: University (A)
class University:
    def __init__(self, name):
        self.name = name

    def details(self):
        print("Welcome to", self.name)


# Single Inheritance: Science stream (B)
class Science(University):
    def __init__(self, name, stream1):
        University.__init__(self, name)
        self.stream1 = stream1

    def details(self):
        print("Science Stream : ", self.stream1)
        return super().details()


# Single Inheritance: Commerce stream (C)
class Commerce(University):
    def __init__(self, name, stream2):
        University.__init__(self, name)
        self.stream2 = stream2

    def details(self):
        print("Commerce Stream : ", self.stream2)
        return super().details()


# Multiple Inheritance: Engineering branch (D)
class Engineering(Science, Commerce):
    def __init__(self, name, stream1, stream2, branch):
        Science.__init__(self, name, stream1)
        Commerce.__init__(self, name, stream2)
        self.branch = branch

    def details(self):
        print("Engineering Branch : ", self.branch)
        return super().details()


# Single Inheritance: Department (E)
class Department(Engineering):
    def __init__(self, name, stream1, stream2, branch, dept):
        Engineering.__init__(self, name, stream1, stream2, branch)
        self.dept = dept

    def details(self):
        print("Department : ", self.dept)
        return super().details()


# Multilevel Inheritance: Section (F)
class Section(Department):
    def __init__(self, name, stream1, stream2, branch, dept, section):
        Department.__init__(self, name, stream1, stream2, branch, dept)
        self.section = section

    def details(self):
        print("Section : ", self.section)
        return super().details()


s = Section("Pune University","Science","Commerce","Computer Engineering","IT Department","A Section")
s.details()