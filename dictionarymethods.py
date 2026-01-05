# d = {} - dict can be created empty
# d = {"Key" : "Value" , "Name" : "John" , "Age" : 21}
# print(d)
# print(type(d))

# d = {"key" : "value" , "name" : "John" , "age" : 21}
# print(d)
# print(d[0]) - indexing is not available in dict
# print(d["age"]) - access values using keys
# d["age"] = 22  - replaces the value by given value
# d["city"] = "Pune" - adds or updates the new value as well (no duplicate keys can be created)
# d = {"key" : "value" , "name" : "John" , "age" : 21 , "name" : "Max"}
# print(d) - print only unique value (eg. only one name & last value gets displayed)

# Datatype of keys is always recommended as string :
# d = {1234 : "John"} or {23.4 : "john} - int & float can be used but value identification is hard
# d = {* : "john"} or {$ : "john"} - no symbols can be used
# d = {(1, 2, 3, 4) : "john"} - tupples are allowed
# d = {[1, 2, 3, 4] : "john"} - list[], set{}, dict{" ": " "} isnt allowed
# print(d)

# there are no restriction of datatypes in values :
# d = {"name" : "john", "age" : 21, "skills" : ["SQL", "Python", "HTML"]} - list
# d = {"name" : "john", "age" : 21, "skills" : {"SQL", "Python", "HTML"}} - set
# d = {"name" : "john", "age" : 21, "skills" : ("SQL", "Python", "HTML")} - tupple
# print(d)
# d = {"name" : "john", "age" : 21, "skills" : {"Web" : "html", "DS" : "Python"}} - dictionary
# print(d)

# if want only "Python" in output, then we use :
# d = {"name" : "john", "age" : 21, "skills" : {"Web" : "html", "DS" : "Python"}}
# print(d['skills']['DS'])

# d = {"name" : "john", "age" : 21, "skills" : {"Web" : "html", "DS" : "Python"}}
# print(d)
# print("john" in d) - shows false as 'john' is not only in d
# print("john" in d['name']) - shows true
# print("age" in d) - shows value as key is mentioned

# d = {"name" : "john", "age" : 21, "skills" : {"Web" : "html", "DS" : "Python"}}
# print(d)
# # print(d.get("name")) - used to get the value from key without error (none as output)
# # del d["skills"] - deletes the whole key:value pair
# # d.pop("skills") - works only when key is mentioned and then deletes the whole key:value pair
# # pop removes values in - (set - 1st value), (list - last value), (dict - specific/mentioned value)
# # d.clear() - removes all the elements from d
# print(d)

# d = {"name" : "john", "age" : 21, "skills" : {"Web" : "html", "DS" : "Python"}}
# print(d)
# print(d.keys()) - only shows keys in output in the form of list
# print(d.values()) - only shows values in output in the form of list

# d = {"name" : "john", "age" : 21, "skills" : {"Web" : "html", "DS" : "Python"}}
# print(d)
# print(d+1) or (d-1) or (d*2) - shows error as datatypes are different
# d1 = {"key" : "value"}
# print(d+d1) - dict also do not get added

# d = {"name" : "john", "age" : 21, "skills" : {"Web" : "html", "DS" : "Python"}}
# print(d)
# # print(d.items()) - shows key:value pairs seperately in the list in the form of tuple
# # d.popitem() - last key:pair gets deleted
# print(d)