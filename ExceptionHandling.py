# a = 10
# b = 0 - commented to show exception handling
# a = 5 - gives correct output

# try:
    # print(a/b)
# except:
    # print("number cannot be divided by zero")


# a = 10
# b = 0
# try:
#     print(a/b)
# except Exception as e: - gives error type
#     print(e)

# print("hello")


# a = 10
# b = 2
# try:
#     print(a/b)
# except Exception as e:
#     print(e)
# finally: - always executes and is optional
#     print("this always executes")

# print("hello")


# a = 10
# b = 5
# try:
#     print(a/b)
#     try:
#         f = open('abc.txt', 'r')
#         print(f.read())
#         f.close()
#     except:
#         print("error in file reading")
# except:
#     print("zero division error")