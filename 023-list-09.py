from operator import itemgetter, methodcaller


print('\n')

info = [('ahmed', 'egypt', 30) , ('omar', 'syria', 36) , ('ibrahim', 'egypt', 23), ('mohamed', 'saudi arabia', 25)]

# sort the list based on the user name
s = sorted(info, key=itemgetter(0))

print(s)

# sort the list based on the country name
s = sorted(info, key=itemgetter(1))

print(s)

# sort the list based on the age
s = sorted(info, key=itemgetter(2))

print(s)


# sort the list based on the country name and if two or more users are from the same country sort them based on their names
s = sorted(info, key=itemgetter(1,0))

print(s)

#==================================================================================================

print('\n')

info = ['ahmed' , 'omar', 'ibrahim', 'mohamed']

# sort the list based on the number of h's in each item in the list
s = sorted(info, key=methodcaller('count', 'h'))

# it will print: ['omar', 'ahmed', 'ibrahim', 'mohamed']
print(s)

# sort the list based on the number of i's in each item in the list
s = sorted(info, key=methodcaller('count', 'i'))

# it will print: ['ahmed', 'omar', 'mohamed', 'ibrahim']
print(s)

#==================================================================================================

print('\n')

info = ['ahmed', 'lamiaa', 'ali', 'mostafa', 'abdelrahman']

# sort the list based on the number of a's in each item in the list
s = sorted(info, key=methodcaller('count', 'a'))

# it will print: ['ahmed', 'ali', 'mostafa', 'lamiaa', 'abdelrahman']
print(s)