a = [0,1,2,3,4,5,6,7,8,9]

# change the value of item with index 2 to a string
a[2]='hello'

print('\n')

print(a)

#==================================================================================================

# remove items with indexs starting from 3 to 6
a[3:7]=[]

print(a)

#==================================================================================================

# note here: unlike the above example, when we set an empty list to a single itme we do not remove it but we set it's value to an empty list
a[0]=[]

print(a)

# if you want to delete the first item do this
# to delete the entire list you can use: del a
del a[0]

print(a)

# if you do not know the index of the items that you want to delete and you know it's value, you can use it to delete the item
a.remove(8)

print(a)

#==================================================================================================

x = ['ahmed', 22, 44.6, True]
y = ['omar', 23, 41.6, False]

z = [x, y]

# print the second element in the first list = 22
print(z[0][1])
# print the forst element in the second list = 'omar'
print(z[1][0])