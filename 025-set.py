print('\n')

# repeated items will be removed from the set, and the set will contain only unique items.
# it will also sort the items in the set in an ascending order.
s = {1, 2, 2, 3, 4, 5, 3, 4, 5, 6, 7, 8, 9, 1, 6, 7, 8, 9}

print(s)


# with strings the set will contain only unique strings, but it will not sort the strings in an ascending order, 
# it will print the items in random order so each time you print the set of strings you will get a deferent order.
ss = {'a', 'b', 'c', 'd', 'b', 'h', 'z', 'i', 'e', 'k', 'e', 'd', 'w', 'u', 'q', 'v', 'p', 'r'}

print(ss)

#==================================================================================================

print('\n')

sss = {'spain', 'france', 'china', 'egypt', 'saudi arabia'}

print(sss)


ssss = {'spain', 'france', 'china', 'egypt', 'saudi arabia', 'china', 'france'}

print(ssss)

#==================================================================================================

print('\n')

se = {1, 2, 2, 3, 4, 5, 3, 4, 'e', 'k', 'e', 'd', 'w', 'u'}

# convert set to list
l = list(se)

print(se, l)

#==================================================================================================

print('\n')

ls = [1, 2, 2, 3, 4, 5, 3, 4, 5, 6, 7, 8, 9, 1, 6, 7, 8, 9]

# convert list to set
# it will remove the repeated items from the list and will sort the items in an ascending order.
sett = set(ls)

print(sett)

#==================================================================================================

print('\n')

n = {i for i in range(10)}

# will print {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(n)

# will print {0, 3, 6, 9, 12, 15, 18, 21, 24, 27}
n = {i*3 for i in range(10)}

print(n)

#==================================================================================================

print('\n')

s1 = {i for i in range(10)}
s2 = {i for i in range(5)}

print("s1:", s1)
print("s2:", s2)

print('\n')

# it will print the union of the two sets, which is a set that contains all the unique items from both sets.
print("s1 | s2:", s1 | s2)
print("s2 | s1:", s2 | s1)

print('\n')

# it will print the union of the two sets, which is a set that contains all the unique items from both sets.
print("s1.union(s2):", s1.union(s2))
print("s2.union(s1):", s2.union(s1))

print('\n')

# it will not print the union of the two sets, it will print the first set if it is not empty, otherwise it will print the second set.
print("s1 or s2:", s1 or s2)
print("s2 or s1:", s2 or s1)

#==================================================================================================

print('\n')

# it will print the intersection of the two sets, which is a set that contains all the unique items that are present in both sets.
print("s1 & s2:", s1 & s2)
print("s2 & s1:", s2 & s1)

print('\n')

# it will print the intersection of the two sets, which is a set that contains all the unique items that are present in both sets.
print("s1.intersection(s2):", s1.intersection(s2))
print("s2.intersection(s1):", s2.intersection(s1))

print('\n')

# it will not print the intersection of the two sets, it will print the second set if the first set is not empty, otherwise it will print the first set.
print("s1 and s2:", s1 and s2)
print("s2 and s1:", s2 and s1)

#==================================================================================================

print('\n')

# it will print the difference of the two sets, which is a set that contains all the unique items that are present in the first set but not in the second set.
print("s1 - s2:", s1 - s2)
print("s2 - s1:", s2 - s1)

print('\n')

# it will print the difference of the two sets, which is a set that contains all the unique items that are present in the first set but not in the second set.
print("s1.difference(s2):", s1.difference(s2))
print("s2.difference(s1):", s2.difference(s1))

print('\n')

# it will print the symmetric difference of the two sets, which is a set that contains all the unique items that are present in either set but not in both sets.
print("s1 ^ s2:", s1 ^ s2)
print("s2 ^ s1:", s2 ^ s1)

print('\n')

# it will print the symmetric difference of the two sets, which is a set that contains all the unique items that are present in either set but not in both sets.
print("s1.symmetric_difference(s2):", s1.symmetric_difference(s2))
print("s2.symmetric_difference(s1):", s2.symmetric_difference(s1))

print('\n')

# it will remove all the unique items that are present in the second set from the first set, and it will not return anything.
# print("s1.difference_update(s2):", s1.difference_update(s2))