# For one user :
# john = [3000, 4000, 2000, 1000]
# print(john[0] + john[1:] + john[2] + john[3]) - gives addition of elements but not a suitable format

# total_expense = 0 - works as indexing
# for i in john:
#     total_expense += i - works as TE = TE + i ( 0 + 3000), (3000+7000)
#     print(total_expense) - if want only final ouput, write print statement outside the for loop

# For two user : 
# john = [3000, 4000, 2000, 1000]
# max = [4500, 6700, 2300, 4000]

# This process is not valid as the code gets lenghty and cannot be performed for numerous people
# total_expense = 0
# for i in john:
#     total_expense += i
# print(total_expense)

# total_expense = 0
# for i in max:
#     total_expense += i
# print(total_expense)

# Creating code using function :
# SYNTAX : 
# 1. function definition - defines
# 2. function execution - output/logic
# 3. function calling - important step

# def function_name():
#     function execution/logic
# function_name() - function calling

# john = [3000, 4000, 2000, 1000]
# max = [4500, 6700, 2300, 4000]
# def expense(name:str):
#     """This function returns total expense"""  - this is docstring
#     total_expense = 0 
#     for i in name:
#         total_expense += i
#     print(total_expense)
# expense(john)
# expense(max)

# 1. FUNCTION WITHOUT PARAMETERS () :
# def Message():
#     print("Hello, this is my first python function")
#     print(20+45)
# Message()


# 2. FUNCTION WITH PARAMETERS (a,b) :
# addition of two numbers - 
# def add(a,b):
#     print(a+b)
# add(10,40)
# add(40,70)

# taking value from user -
# n = int(input("Enter first number : "))
# n1 = int(input("Enter second number : "))
# def add(a, b):
#     print("Addition of two numbers is :", a+b)
# add(n, n1)

# def sum(a, b, c):
#     print(a+b)
# sum(20, 60)

# 3. FUNCTION WITH DEFAULT PARAMETERS (a,b=10) :
# Execution of functions is always from bottom to top ↑
# def sum(a=40, b=10):
#     print(a+b)
# sum(20, 60)

# def sum(a, b=10):
#     print(a+b)
# sum(20, 60)

# 4. FUNCTION WITH RETURN STATEMENT :
# def sum(a,b):
#     return a + b
# result = sum(20,80)
# print(result) 

# def values(a, b, c, d, e, f):
#     return a, b, c, d, e, f
# result = values(10, "hello", "python", 12.3, 56, 78)
# print(result)

# *args function : gives multiple arguments without multiple parameters
# def numbers(*a):
#     print(a)
# numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# addition of all the elements in list :
# def numbers(*a):
#     sum = 0
#     for i in a:
#         sum += i
#     print("Addition of all numbers :", sum)
# numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# **kwargs function : keywords arguments - dictionary - key/value pairs
# def msg(**a):
    # print(a)
# msg(n =10, b="world") - gives values as dictionary

# Using both *args in different ways :
# def test(*a, b, c, d, e): - when *args is given at first, all the elements goes in it, which leads to error
#     print(a, b, c, d, e)
# test(1, 2, 3, 4, 5)

# def test(a, b, c, d, *e): - when *args is given at last, elements will be shown properly
#     print(a, b, c, d, e)
# test(1, 2, 3, 4, 55, 65, 75, 85, 95)

# def test(*a, b, c, d, e, f):
#     print(a, b, c, d, e)
# test(1, 2, 3, 4, b=55, c=65, d=75, e=85, f=95) 

# Using both *args & **kwargs :
# def test(*a, **b):
#     print(a)
#     print(b)
# test(1, 2, 3, 4, 5, n= 1, n1= "hello")

# Lambda function : coding in single line or using single logic
# x = lambda a,b : a+b
# print(x(10,50))

# list comprehension (Converting tupple to list) : 
# t = (1, 2, 3, 4, 5)
# 1st method:
# list(t)

# 2nd method :
# l = []
# for i in t:
#     l.append(i)
# print(l)

# 3rd method :
# result = [i for i in t]
# print(result)

# result = [i**2 for i in t] - gives squares
# print(result)

# iterator and iterable :
# without for loop and indexing, if we want to acess one by one elements, then iter function is used

# a = "Hello"
# s = iter(a) - iterable
# print(next(s))  iterator
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))

# a = 12 - this function do not work on int, hence shows error
# s = iter(a)
# print(next(s))


