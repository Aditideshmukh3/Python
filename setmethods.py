# s = {12, "Python", True, 1, "hello", 12.4, 12}
# print(s)
# print(type(s)) - here value of 1 is also considered as true in output (same for 0 = false).

# s = {12, "Python", True, 1, "hello", 12.4, 12}
# print(s)
# print(s[0]) - Indexing & slicing is not available

# s = {12, "Python", True, 1, "hello", 12.4, 12}
# print(s)
# s.add(400)
# s.add('100')
# s.add(1) - adds value as true
# print(s)

# s = {12, "Python", True, 1, "hello", 12.4, 12}
# print(s)
# # t = (120, 300) - tuple adds value but in ( )
# # t = {120, 300} - shows error
# # t = [120, 300] - shows error
# # t = "good" - single string gets added in the list
# # t = {"good" : "value"} - its an combined pair, so it shows error
# s.add(t)
# print(s)
# s.add(120,300) - this function only adds one argument, not multiple 
# print(s)

# s = {12, "Python", True, 1, "hello", 12.4, 12}
# print(s)
# # s.update('hello', 45) - integer is not iterable, so it shows error for int.
# # s.update('hello') - each character/letter gets add seperately (only unique values)
# # t = (23, 45, "hello") - elements gets added properly (tuple)
# # t = {23, 45, "hello"} - elements gets added properly (set)
# # t = [23, 45, "hello"] - elements gets added properly (list)
# # t = {"good":"value"} - only key ("good") gets added
# s.update(t)
# print(s)

# s = {12, "Python", True, 1, "hello", 12.4, 12}
# print(s)
# # s1 = s.copy() - this is used when you dont want to change the whole original data when processing other methods
# # s.pop() - this feature removes the 1st element from the set (available in set,list,dict)
# print(s)

# s = {12, "Python", True, 1, "hello", 12.4, 12}
# print(s)
# s.remove("Python") - removes the mentioned value & only takes one argument
# s.remove(200) - shows error when value in not available in list
# s.discard(200) - used when you dont want error but want to remove the value
# s.discard(12, 1) - only takes one argument, so shows error
# s.clear() - deletes all the values in set
# print(s)

# a = 12 - only iterable value gets displayed (set)
# a = "String" - shows result but each letter as an different element
# a = ["String", 34, 56] - shows result (set)
# a = {"key" : "value"} -only key is shown
# print(a)
# result = set(a)
# print(result)

# s = {10, 30, 30, 4, 5, 6}
# s1 = {1, 2, 30, 4, 7, 8}
# print(s.intersection(s1)) - shows only commom values from both sets
# print(s.union(s1)) - shows all the elements combined from both sets except common & duplicate
# print(s.symmetric_difference(s1)) - opposite to intersection (doesnt show commom elements)
# print(s.difference(s1)) - shows values that are not common (only from S)
# print(s1.difference(s)) - shows values that are not commom (from S1)

# s = {"a", "b", "c"}
# y = {"f", "e", "d", "b", "a", "c"}
# print(s.issubset(y)) - shows if elements in s are available in y (true)
# print(y.issubset(s)) - shows if elements in y are avaliable in s (false)

# y = {"f", "e", "d", "b", "a", "c"}
# print("f" in y) - shows true
# print("f" not in y) - shows false


# ASSIGNMENT -
# s = "Pythonpycharm" - reverse the string 
# s = "Pythonpycharm"
# print(s[::-1]) - slicing method (start : & end : are empty and step as -1)

# t = "Pythonprogramming" - access only unique elements
# t = "Pythonprogramming"
# result = set(t) - set method (as it automatically removes duplicates)
# print(result)