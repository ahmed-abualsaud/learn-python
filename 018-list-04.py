print('\n')

a=[5,6,7,1,2,10,3,4,8,9]
b=['a', 'd', 'i', 'b', 'b', 'z']

# create a sorted copy of the original list
sortedList = sorted(a)

print(a, sortedList)

# sort a itself, it returns nothing
a.sort()
print(a)

#==================================================================================================

# sort the list in a reversed order
reversedList = sorted(a, reverse=True)

print(reversedList, sorted(b, reverse=True))

# reverse the list itself
a.reverse()

print('reversed list:'.title(), a)

#==================================================================================================

x = [('ahmed', 30), ('omar', 33), ('ibrahim', 27)]

sortedListByName = sorted(x, key=lambda e: e[0])
sortedListByAge = sorted(x, key=lambda e: e[1])
sortedListByAgeInReversedOrder = sorted(x, key=lambda e: e[1], reverse=True)

print('\n')
print(x)
print(sortedListByName)
print(sortedListByAge)
print(sortedListByAgeInReversedOrder)

#==================================================================================================

string = '1,2,3,4,5,6,7,8,9,10'

# split string by separator ',' and implement only 5 splits
splittedList = string.split(sep=',', maxsplit=5)

print('\n')
print(splittedList)

#==================================================================================================

users = ['ahmed', 'omar', 'ibrahim', 'yousif']

# check if an element in the list
if 'omar' in users:
    print('omar exists in the list of users')

print('ahmed' in users)

#==================================================================================================

listA = [1, 2, 3]
listB = ['a', 'b', 'c']
# add listA and listB to listC (list concatination)
listC = listA + listB

print('\n')
print(listA)
print(listB)
print(listC)

# add listB to the end of listA itself
listA.extend(listB)

print(listA)