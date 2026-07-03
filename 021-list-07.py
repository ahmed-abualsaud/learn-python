print('\n')

# bind iterator to the list
i = iter(['ahmed', 22, 7.3, False])

# print the first item in the list
print(next(i))

# print the second item in the list
print(next(i))

# print the third item in the list
print(next(i))

# print the forth item in the list
print(next(i))

# throw error because their are no more items
# print(next(i))

#==================================================================================================

print('\n')

rng = range(10)
it = iter(rng)

# print every item in the output list of the range function
for x in rng:
    print(next(it))

#==================================================================================================

print('\n')

x = [1,2,3,4,5]

# copy list x to y
y = x

# will print 1 because we make a shallow copy y from the list of x
print(y[0])

# copy list y to z
z = y

# will print 2 because we make a shallow copy z from the list of y
print(z[1])

#==================================================================================================

print('\n')

u = [1 , 2 , 3 , 4 , 5]
v = ['a','b','c','d','e']


x = u
y = v

# add y to the end of x
x.extend(y)

# it will print [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']
print(x)

#==================================================================================================

print('\n')

# any changes to the values of x will be reflected to the value of u as well
x[0] = 9

# it will print 9 because it is affected by the change of the value of index 0 in list x
print(u[0], u)

v[3] = 'h'

# both print 'h'
print(v[3], y[3])

del v[1]

# the itemd with index 1 in the list v will be deleted from list y as well
print(y)
