# QUESTION 1 : Write a Python program to verify a 10-digit contact number. 
# If digits = 10 → "Number is verified", else → "Invalid number".

# ANSWER :
# contact = input("Enter your contact number: ")

# if len(contact) == 10 and contact.isdigit():
#     print("Number is verified")
# else:
#     print("Invalid number")

# --------------------------------------------------------------------------------------------------------------

#QUESTION 2 : Print multiplication table from 1 to 10 using for loop :

# ANSWER :
# n = int(input("Enter any number: "))

# for i in range(1, 11):
#     print(n, "x", i, "=", n*i)

# --------------------------------------------------------------------------------------------------------------

#QUESTION 3 : Write a Python code to create any number’s table from 1–10 using while loop (increment).

# ANSWER :
# n = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(n, "x", i, "=", n * i)
#     i += 1   

# -----------------------------------------------------------------------------------------------------------------

# QUESTION 4 : Write a Python code to create any number’s table from 10–1 using while loop (decrement).

# ANSWER :
# n = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(n, "x", i, "=", n * i)
#     i += 1   

# --------------------------------------------------------------------------------------------------------------

# QUESTION 5 : Write a Python program to separate elements of a mixed list into numbers, strings, and other data types.
# FOR LOOP :

# ANSWER :
# l = ['string', 20, 21, 22, 34.5, True, 1, 0, 12.4, False, 'python']

# numbers = []
# texts = []
# others = []

# for item in l:
#     if type(item) in [int, float] :
#         numbers.append(item)
#     elif type(item) == str:
#         texts.append(item)
#     else:
#         others.append(item)

# print("Number list:", numbers)
# print("Text list:", texts)
# print("Other data type list:", others)

# ------------------------------------------------------------------------------------------------------------------

# QUESTION 6 : Write a Python program to separate elements of a mixed list into numbers, strings, and other data types.
# WHILE LOOP :

# ANSWER :
# l = ['string', 20, 21, 22, 34.5, True, 1, 0, 12.4, False, 'python']

# numbers = []
# texts = []
# others = []

# i = 0
# while i < len(l):
#     item = l[i]
#     if type(item) in (int, float):
#         numbers.append(item)
#     elif type(item) is str:
#         texts.append(item)
#     else:
#         others.append(item)
#     i += 1

# print("Number list:", numbers)
# print("Text list:", texts)
# print("Other data type list:", others)

# -----------------------------------------------------------------------------------------------------------------

# QUESTION 7 : Write a Python code to count the frequency of each character in the string s = "aaaaaaaabbbbcccdddddddeeeeeeeee"

# ANSWER :
# s = "aaaaaaaabbbbcccdddddddeeeeeeeeee"
# unique_characters = ""  

# for character in s:
#     if character not in unique_characters:       
#         print(character, "-", s.count(character))
#         unique_characters += character  

# --------------------------------------------------------------------------------------------------------------  

# QUESTION 8 : Write a Python function that takes multiple numbers as arguments and returns them as a list (*args).

# ANSWER :
# def numbers(*a):  
#     num_list = list(a)  
#     return num_list

# result = numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print("Number list :", result)

# --------------------------------------------------------------------------------------------------------------
