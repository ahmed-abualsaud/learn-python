print('\n')

# calculate function f(x) = x^2 for x between 0 and 9
f = [x**2 for x in range(10)]

print(f)

# calculate function f(x) = x^3 + 2x^2 + 1 for x between 0 and 9
f = [x**3 + 2*x**2 + 1 for x in range(10)]

print(f)

#==================================================================================================

print('\n')

# calculate function f(x) = x^2 for x between 0 and 9 but the map function and the lambada functions
f = list(map(lambda x: x**2, range(10)))

print(f)


# calculate function f(x) = x^3 + 2x^2 + 1 for x between 0 and 9 but the map function and the lambada functions
f = list(map(lambda x: x**3 + 2*x**2 + 1, range(10)))

print(f)

# you can calculate any function you want

#==================================================================================================

print('\n')

# get all paired combinations between the lists [1,2,3] and [3,5,7]
p = [(x,y) for x in [1,2,3] for y in [3,5,7]]

print(p)

# get all paired combinations that have different values between the lists [1,2,3] and [3,5,7]
p = [(x,y) for x in [1,2,3] for y in [3,5,7] if x!=y]

print(p)

#==================================================================================================

print('\n')

# get all paired combinations between the lists ['ahmed','mohamed','omar', 'mona'] and ['doctor','engineer','lawyer']
p = [(x,y) for x in ['ahmed','mohamed','omar', 'mona'] for y in ['doctor','engineer','lawyer']]

print(p)

print('\n')

# get all paired combinations that have different values between the lists ['ahmed','mohamed','omar', 'mona'] and ['doctor','engineer','lawyer']
p = [(x,y) for x in ['ahmed','mohamed','omar', 'mona'] for y in ['doctor','engineer','lawyer'] if x != 'omar' and y != 'lawyer']

print(p)

#==================================================================================================

print('\n')

# this will create a matrix/2d list with 5 columns and 7 rows and all values o f the matrix are equal to zero 0
m = [[0 for i in range(5)] for j in range(7)]

print(m)