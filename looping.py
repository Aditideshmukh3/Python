# l = [10, 20, 30, 40, 50, 60, 70]
# any datatype can be used - {}, [],()
# to access one-by-one elements from list, we can not use indexing as the code can be too long
# print (l[0])
# print (l[1])

# FOR LOOP SYNTAX : (For loop runs over each element and stops at the end of the sequence)
# for item in collection:
#     # execution
#     print(item)

# l = [10, 20, 30, 40, 50, 60, 70]
# for i in l:
    # print(i) - prints item in output
    # print(l) - prints collection (i.e list) in output

# l = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]
# for i in l:
    # print(i, end="\n") - gives output in next line/new line
    # print(i, end=" ") - gives output in single line with space in each element 
    # print(i, end="\t") - works as tab key - gives output in single line with 4 space in each element
    # print(i, end=" * ") - gives output in single line with symbol in between each element

# break function :
# l = [10, 20, 30, 40, 50]
# for i in l:
#     print(i)
#     if i == 30:
        #  break - to stop the particular loop

# continue function : 
# l = [10, 20, 30, 40, 50]
# for i in l:
#     if i == 30:   
#         continue
#     print(i)

# t = (10, 20, 30, 40, 50)
# for i in t:
#     print(i)
# else:
#     print("hello")

# l = (10, 20, 30, 40, 50) - for loop works on tuple 
# s = "Python is easy" - for loop works on string but on new line
# s = 123 - for loop doesnt work on int/float
# s = True - foor loop doesnt work on boolean
# s = {1, 2.5, 3, 6, 5} - for loop works on set but changes the sequence
# s = {"key":"value" , "name":"john" , "age":23} - for loop works on dict and only gives key values
# for i in s: 
    # print(i)
# s = {"key":"value" , "name":"john" , "age":23} - to get values in dict, modify print function
# for i in s: 
#     print(i , "=", s[i] )

# range function : (works as slicing)
# for i in range(10): - gives values from 0 -9
# for i in range(1,11):  gives values from 1-10
# for i in range(1, 101, 2) - gives alternate numbers
    # print(i, end=" ")

# l = [10, 20, 30, 40, 50, 60, 70]
# for i in range(10,70): - gives output from 10 to 69 (which is wrong)
#     print(i, end=" ")
# for i in range(7):
#     print(l[i], end=" ") - gives output from 10-70 as print function is modified
# l = [10, 20, 30, 40, 50, 60, 70, 10, 20, 30, 40, 50, 60, 70, 10, 20, 30, 40, 50, 60, 70]
# for i in range(len(l)): len function is used when so many elements are available in list
    # print(l[i], end=" ")
# l = [10, 20, 30, 40, 50, 60, 70, 10, 20, 30, 40, 50, 60, 70]
#  for i in range(len(l)):
#     print(i, ":", l[i]) - gives indexing of elements (0=10, 1=20)

# ----------------------------------------------------------------------------------------------------------------

# WHILE LOOP SYNTAX :
# initilization
# while(condition):
#     execution
#     increment/decrement - compulsory 

# print numbers from 1 to 10 :
# i = 1 - any value we want can be given ( if want 0-10 then i=0)
# while (i <= 100):
#     print(i)
#     i += 1

# alternate numbers (i += 2) :
# i = 1
# while (i <= 100):
#     print(i)
#     i += 2

# i = 1
# while (i <= 10):
#     i += 1
#     print(i) - if print function is used below increment, then it prints 2-11 as increment function gets performed first

# i = 1
# while (i <= 10):
#     print(i)
#     i += 1
    # if i ==5: 
        # break - breaks/stops the loop at 4

# i = 1
# while (i <= 10): 
#     i += 1
#     if i ==5:
#         continue - continues the loop without 5
#     print(i) 

# increment using list :
# l = [10, 20, 30, 40, 500, 600, 700]
# i = 0
# # # while (i < len(l)): - if elements gets increased, there wont be any problem as len is used
# #     print(l[i])
# #     i += 1

# decrement using list :
# l = [10, 20, 30, 40, 500, 600, 700]
# i = len(l) - 1      
# while i >= 0:        
#     print(l[i])
#     i -= 1



