print('\n')

u = [1 , 2 , 3 , 4 , 5]
v = ['a','b','c','d','e']

# will create a deep copy of u and save it to x
x = u.copy()

# will create a deep copy of v and save it to y
y = v.copy()

print(x)

u[2] = 5

print(x, u)

y.extend(u)

print(y, v)

#==================================================================================================

print('\n')

e = [1 , 2]
r = ['a', 'b']

x = e
y = r

# will print [1, 2] ['a', 'b']
print(x, y)

e = [10, 11, 12]

# will print [1, 2] ['a', 'b'] as well because when we replace the list e with a totally new values: [10, 11, 12],
# this will not affect the list x, keeping x with the old values of list e [1 , 2]
print(x, y)

#==================================================================================================

print('\n')

lst = ['ahmed', 22, 7.3, False]

# create enumeration of the list that contains the index and the value of each item in the list
enum = enumerate(lst)

for index, value in enum:
    print("Value of the item in index: {index} is {value}".format(index=index, value=value) )

print('\n')

# start enumerating from index 1, which means the index of the first item in the list will be 1, not 0
enum = enumerate(lst, 1)

for index, value in enum:
    print("Value of the item in index: {index} is {value}".format(index=index, value=value) )

#==================================================================================================

print('\n')

aList = [1 , 2 , 3 , 4 , 5]
bList = ['a','b','c','d','e']

# zip function is binding or pairing two items together from two deferent list (a, b)
# you can suppose that the enumerate function is zipping the values of a list items to their indexes (index, value)
for a, b in zip(aList, bList):
    print(a, b)

print('\n')

dList = ['a','b','c']

# will iterate only 3 times because the minimum length of the both lists is 3
for a, d in zip(aList, dList):
    print(a, d)