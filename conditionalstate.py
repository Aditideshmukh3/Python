# if condition:
#     execution

# a = 10
# if (a > 0):
#     print("A is positive") - if the condition is true, output is executed
# a = -10
# if (a > 0):
#     print("A is positive") - if the condition is false, output is not executed

# a = -10
# if (a > 0):
#     print("A is positive") 
# condition can't be given to 'else'
# else:
#     print("A is negative")

# a = int(input("Enter any number :"))
# if (a > 0):
#     print("A is positive")
# elif compulsory needs condition and can be used multiple times
# elif (a == 0):
#     print("A is zero")
# else:
#     print("A is negative")

# QUESTION : write a program for number is even or odd :
# a = int(input("Enter any number : "))
# if (a / 2 == 0) - / can't be used here (gives output as odd to everything)
# if (a % 2 == 0):
#     print("A is even")
# else:
#     print("A is odd")

# QUESTION : Write a Python program to store input number in even or odd list and print both.
# a = int(input("Enter a number: "))
# even = []
# odd = []
# if (a % 2 == 0):
#     even.append(a)
# else:
#     odd.append(a)
# print("Even list:", even)
# print("Odd list:", odd)

# AND & OR function :
# username = input("Enter your username : ")
# password = input("Enter your password : ")
# if username == 'aditi' and password == '1234' :
#     print("User verified")
# else:
#     print("User not verified")
#                    AND
# if username == 'aditi' or password == '1234' :
#     print("User verified")
# else:
#     print("User not verified")


# ASSIGNMENT : Write a python program for grade system :

# marks = int(input("Enter your marks : "))
# if (marks >= 90 and marks < 100) :
#     print("Grade: A")
# elif (marks >= 80 and marks < 90) :
#     print("Grade: B")
# elif (marks >= 70 and marks < 80) :
#     print("Grade: C")
# elif (marks >= 60 and marks < 70) :
#     print("Grade: D")
# elif (marks >= 50 and marks < 60) :
#     print("Grade: E")
# else:
#     print("FAIL")

# Nested if else function :
# a = 15
# if (a >= 0):
#     if (a > 0):
#         print("A is positive")
#     else:
#         print("A is zero")
# else: 
#     print("A is negative") 

# pass function : A placeholder statement in Python that does nothing; used to maintain syntactic correctness.
# a = 100
# b = 22
# if a > b:
#     pass
#     print("Hello")

# membership operators :
# l = [1, 2, 3, 4, 5]
# if 4 in l:
#     print("Present")
# else: 
#     print("Absent")
