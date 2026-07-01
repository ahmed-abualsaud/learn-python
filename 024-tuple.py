from operator import itemgetter

print('\n')

# data is fixed (no add, no remove, no modify) and cannot be changed later in the code.
a = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(a)

# a[0] = 10 # this will raise an error because you cannot change the items in the tuple after it is created.
# a.append(10) # this will raise an error because you cannot add items to the tuple after it is created.

# access the first and second items in the tuple, you access it with the index of the item you want to access, 
# and the index starts from 0. just like lists, but you cannot change the items in the tuple after it is created.
print(a[0], a[1])

# it will print the last two items in the tuple.
print(a[-1], a[-2])

# it will print the items from index 2 to index 4 (5 is not included)
print(a[2:5])

# it will print the minimum, maximum, and the sum of all the items in the tuple.
print(min(a), max(a), sum(a))

# convert list to tuple
t = tuple(['a', 'b', 'c'])

print(t)

# convert tuple to list
# t = list(t) # this converts t itself to list
l = list(t)
print(l)


# this allows you to create a tuple without using parentheses, but it is not recommended because it can be confusing.
f = 1,2,3,4,5,6,7,8,9,10

print(f)

# you can create a tuple with a single item, but you need to add a comma after the item, otherwise it will be considered as an integer or string.
g = (1,)
print(g, (1))

# this is a list of tuples, each tuple contains 3 items: name, country, and age.
info1 = [('ahmed', 'egypt', 30) , ('omar', 'syria', 36) , ('ibrahim', 'egypt', 23), ('mohamed', 'saudi arabia', 25)]

print(info1)

# this is a tuple of tuples, each tuple contains 3 items: name, country, and age.
info2 = (('ahmed', 'egypt', 30) , ('omar', 'syria', 36) , ('ibrahim', 'egypt', 23), ('mohamed', 'saudi arabia', 25))

print(info2)

# sort the list of tuples based on the first item in each tuple (name)
print(sorted(info1, key=itemgetter(0)))

# sort the tuple of tuples based on the first item in each tuple (name)
print(sorted(info2, key=itemgetter(0)))
