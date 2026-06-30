print('\n')

x = ['ahmed', 22, 44.6, True]
y = ['omar', 23, 41.6, False]

# list concatination: append y to the end of x
z = x + y

print(z)

#==================================================================================================

# concatinate x with itself 3 times x + x + x
print(x*3)

# print list of 10 integer zeros
print([0]*10)

# print list of 10 float zeros
print([0.0]*10)

# print list of 10 boolean (False)
print([False]*10)

#==================================================================================================

# print list of 8 zeros
a=0
u=[a]*8

print(u)

# print list of 8 empty lists
a=[]
u=[a]*8

print(u)

# print list of 8 zeros lists 
a=[0]
u=[a]*8

print(u)


# print 2d matrix of 8 rows and 3 columns, you can print it like this directly: print([[0]*3]*8)
a=[0]*3
u=[a]*8

print(u)
print([[0]*3]*8)

#==================================================================================================

# get the number of elements in the list, the elements in the list can be numbers, strings, floats, lists or any other types.
v=[0]*3
u=[[0]*3]*8

print(len(u), len(v))

#==================================================================================================

a=[5,6,7,1,2,10,3,4,8,9]

# sum works only for integer of floats elements of the list
summation = sum(a)

length = len(a)

average = summation/length

# minimum of of numbers or alphabetic letters, not working for multi-type lists = [1,'a']
maximum = max(a)

# minimum of of numbers or alphabetic letters, not working for multi-type lists = [1,'a']
minimum = min(a)

print(summation)
print(length)
print(average)
print(maximum)
print(minimum)

print(min(['a', 'b', 'c']), max(['a', 'b', 'c']))
