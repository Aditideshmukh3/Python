# READ mode : (by default mode)
# f = open ('abc.txt', 'r') - shows error as file is not present
# f = open ('abc.txt', 'r') - doesnt show error
# print(f)

# WRITE mode :
# f = open ('abc.txt', 'w') - shows output
# f = open ('abcd.txt', 'w') - creates new file
# print(f)

# CREATE mode :
# f = open ('abcd.txt', 'x') - shows error as file is already created
# print(f)

# f = open('abc.txt', 'r') - shows error as the file is open in read mode
# f = open('abc.txt', 'w') - shows input in the file
# f = open('abc.txt', 'w')
# r = f.write("Hello this is my first file handling") - shows output as indexing in numerical
# print(r)

# f = open('abc.txt', 'w')
# r = f.write("good afternoon") - if we put another input, the first input gets deleted
# print(r)

# APPEND mode :
# f = open('abc.txt', 'a') 
# - adds text at the end of previous text
# r = f.write("\nHello World")
# print(r)
# f.close()
# f.write("\nHello World") - when code is wriiten after close mode, other operations cannot be performed

# f = open('abc.txt', 'r')
# print(f.read()) - shows data of the file in terminal
# print(f.read()) - gives blank space after first output
# print(f.read())
# print(f.tell()) - shows cursor position
# print(f.seek(0)) - shows cursor position at given value

# f = open('abc.txt', 'r')
# print(f.readline()) - reads code per line
# print(f.readlines()) - gives whole output in list

