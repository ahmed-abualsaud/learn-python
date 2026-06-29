# list can include many items from different types
lst = ['Ahmed', 22, 14.7, 1+8j, True, ['a', 1, False], ('test', 3.2), {1,2,'test'}, {'a':'yes', 'b':33, 'c':True}]

print('\n')

print(lst)

#==================================================================================================

# 3*4 matrix --> 2d list/array
matrix=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

print(matrix)

#==================================================================================================

# Split the string to it's characters: ['H', 'o', 'w', ' ', 'A', 'r', 'e', ' ', 'Y', 'o', 'u']
textList=list("How Are You")

print(textList)

#==================================================================================================

# List destruction: we can add each element in the list to variable.
# The number of variables must equals the number of elements in the list.
a,b,c = ['ahmed', 1, True]

print(a,b,c)

#==================================================================================================

lst = ['ahmed', 1, True]

#print the first element
print(lst[0])

#print the second element
print(lst[1])

#print the third element
print(lst[2])

#==================================================================================================

a = [0,1,2,3,4,5,6,7,8,9]

# Print the items starting from index 0 to index 2
print(a[:3])

# Print the items starting from index 0 to index 4
print(a[:5])

# Print the items starting from index 3 to index 7
print(a[3:8])

# Print the items starting from index 4 to the end of the list
print(a[4:])

# Print all items of the list except the last three elemets
print(a[:-3])

# Print the items of the list starting from index 3 to the forth item at the end of the list
print(a[3:-3])

#==================================================================================================
