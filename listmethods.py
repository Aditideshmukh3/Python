# l = [12, 34.5, "String", True, 456] - lists can be created empty
# print(l)
# print(type(l))

# l = [12, 34.5, "String", True, 456]
# print(l)
# print(l[0]) - shows the index value i.e - 12

# l = [12, 34.5, 10, 20, 30, "String", True, 456]
# print(len(l)) - shows the elements no. in list
# print(l[5]) - shows error as index is available from 0-4
# print(l[::-1]) - list also get reversed
# print(l[:100]) - shows all the elements from list as end is 100
# print(l[100:0]) no element is positioned at 100th so shows empty list

# t = {1, 2, 3, 45, 1, "hello"}
# print(list(t)) - tuple gets converted to set {}
# print(list(t)) - tuple gets converted to list[]

# t = "Python"
# print(list(t)) - shows result in seperate individual letters

# t = 23
# print(list(t)) - interger is not iterable

# t = {"key":"value", "name":"john"}
# print(list(t)) - only key is shown in the output

# l = [12, 34.5, 10, 20, 30, "String", True, 456]
# print(l + 1) - shows error as int cannot be added in list
# print(l+[1]) - adds the value as int is converted to list via []
# print(1-[1]) - shows error as there is no any value to be subtracted
# print(l * 2) - multiplies the list elements by given no
# print(12 in l) - membership operators (true)
# print(12 not in l) - membership operators (false)

# l = [12, 34.5, 10, 20, 30, "String", True, 456]
# print(min(1)) - shows error as list has str as well as int
# l = [12, 34.5, 10, 20, 30, 456]
# print(min(l)) - shows minimum value from list - 10
# print(max(l)) - shows maximum value from list - 456

# l = ["Apple", "ball", 'Cat', "Zebra", "Python", "Moon"]
# print(min(l)) - Apple
# print(max(l)) - ball 
# when list has string(alphabets only) then the min & max function works as per ASCII codes
# ASCII Values = (A-Z = 65-90) & (a-z = 97-122)

# l = [10, 29, 30, 40, 10, "Python"]
# l[3] = 120 - value of index-3 gets replaced by 120
# l.insert(3, 120) - value gets inserted at given index without deleting any value
# result = l.count(10) - shows the count of specific no. (10 - '2')
# result = l.index(10) shows index value and in repeated shows the index of 1st value
# l.append(120) - value gets added at the end of the list & only takes 1 argument
# t = {120, 45, 34}
# l.extend(t) - adds values without any brackets at the end
# print(l)

# l = [10, 29, 30, 40, 10, "Python"]
# l.pop() - deletes the elements from the end
# l.remove(29) - removes the particular mentioned value
# del l[3] - delets the element index wise
# print(l)

# l = [10, 29, 30, 40, 10, "Python"]
# # l.reverse() - reverse the list
# # l = [10, 29, 30, 40, 10]
# # l.sort() - sort the list from ascending to descending order (only int)
# # l.sort(reverse=True) sort the list from descending to ascending as mentioned - True
# # l.sort(reverse=False) - by default value (A - D)
# l1 = l.copy()
# print(l)
# print(l1)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = [7, 8, 9]

# # l4 = l1+l2+l3
# # l4 = [l1, l2, l3]
# print(l4)


# ASSIGNMENT :
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]] - From this whole list, access the single element i.e. 6 

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = [7, 8, 9]
# l4 = [l1, l2, l3]
# print(l4)
# print = l4[1][2]
