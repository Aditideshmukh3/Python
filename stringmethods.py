# 1. slicing :
# s= "Python is easy to learn"
# print(s)
# print(type(s))
# print(len(s)) - lenth of sentence
# print(s[0])  - index
# print(s[-1])
# print(s[22])

# s = "Python is easy to learn"
# print(s)
# print(s[0 : 8])
# slicing: some portion of string
# s[start : end : step]
# print(s[0 : 25 : 2]) - positive
# print(s[-1 : -5]) - negative
# print(s[-5 : -1])

# s = "Python is easy to learn"
# print(s)
# print(s[1 :])
# print(s[ ::-1 ]) - reverse the string

# 2. basic operations :
# s = "python"
# s1 = " is easy to learn" - if want space, add after "
# print(s + s1)
# r = s + " " + s1
# print(r)
# print(s+"1")
# print(s-"1") - no substraction is performed 
# print(s*2) - multiplies the string

# 3. string methods :
# s = "     python    "
# print(s)
# print(len(s))
# # output = s.lstrip() - l(left) removes the left side space
# # output = s.rstrip() - r(right) removes the right side  space
# # output = s.strip() - removes both sides space
# print(output)
# print(len(output))

# getting input from user :
# s = input("Enter a value :")
# print(s)
# print(s+1) - shows error as its an string
# s = int(input("Enter a value :")) - shows value as its integer
# print(s)
# print(s+1)
# s = float(input("Enter a value :")) - shows decimal value
# print(s)
# print(s+1)

# s = "findDatafindData"
# result = s.find("a") - shows the index/position of the first a
# result = s.find("A") - shows -(negative) value when unavailable
# result = s.find("Data") - shows the position of word
# result = s.count('a') - counts the letter a in a sentence

# s = "find, Data, find Data"
# result = s.split(",")
# s =  "python is hard to learn"
# result = s.replace("hard" , "easy") - replaces the word
# print(result)
# s =  "python is hard to learn hard to learn hard to learn" 
# result = s.replace("hard" , "easy")
# print(result)
# s =  "python is hard to learn hard to learn hard to learn" 
# result = s.replace("hard" , "easy", +1) - here count is used and it changes only 1st word as +1 is used
# print(result)

# t = ("Python", "c", "c++", "Pandas")
# print(t)
# # s = " ".join(t) - " " joins the string with space
# # s = " * ".join(t) - " * " joins the string using symbol
# # s = " and ".join(t) - " and " joins the string with word
# print(s)

# s = "Hello World"
# # result = s.lower() - shows result in lower cases
# # result = s.upper() - shows result is upper cases
# # result = s.title() - shows first lettes of all the words in upper case
# # result = s.capitalize() - shows only first words first letter in upper case
# # result = s.swapcase() - swaps the upper to lower or lower to upper
# print(result)

# s = "Hello World"
# print(len(s))
# result = s.center(20, "*")
# print(result)
# print(len(result))

# s = "Python"
# print(s.isupper()) - shows if whole string is in uppercase in T/F format
# print(s.islower()) - shows if whole string is in lowercase in T/F format
# print(s.isalnum()) - shows if string has alphabets or numbers

# s = "1234"
# print(s.isalpha()) - shows only alphabets in the string
# print(s.isdigit()) - shows only digits in the string

# s = "Hello "
# print(s.istitle()) - shows true when 1st letter is capital
# print(s.isspace()) - shows ture only when whole string is empty

# s = "Learning python"
# print("n" in s)
# print("N" not in s) - membership operators (in & not in)

# s = "Learning python"
# print(s.startswith("L")) - shows the starting of sentence
# print(s.startswith("Learn")) 
# print(s.endswith("hon")) - shows the ending of sentence
# print(s.endswith("n"))
# can be used in emails, web urls

# s = "hello"
# print(s.index("l")) - shows the index number of letter
