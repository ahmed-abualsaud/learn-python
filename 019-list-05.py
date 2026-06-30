print('\n')

a=[5,6,7,1,2,10,3,4,8,9]

# append single item at the end of the list
a.append(22)
a.append('17')

print(a)

#==================================================================================================

# insert string at index 3 in the list
a.insert(3, 22)

print(a)

#==================================================================================================

# counts how many times the element 22 exists in the list
print(a.count(22))

#==================================================================================================

# get the index of element 10
print(a.index(10))

#==================================================================================================

# pop (remove and fetch) the last element in the list
# if the list is empty it will throw an error
print(a.pop(), a)

# pop the first element in the list and remove the element with value 1 in the same list a
print(a.pop(0), a.remove(1), a)

#==================================================================================================

# create new range of 10 items from 0 --> to 9
rng = range(10)

# create list from this range
x = list(rng)

print(x)

# print 14 item from 0 to 13
print(list(range(14)))

# print list starting from item 3 to item 10: [3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(3, 11)))

# print list starting from item 3 to item 10 with step of value 2 skip one number between two consecutive numbers: [3, 5, 7, 9]
print(list(range(3, 11, 2)))

print(list(range(5, 101, 5)))