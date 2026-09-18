import numpy as np

theta = np.deg2rad(30)
a = np.sin(theta)
b = np.cos(theta)
c = np.tan(theta)

print('sin({theta}) =', a, '\ncos({theta}) =', b, '\ntan({theta}) =', c, '\n')

theta = np.deg2rad(60)
a = np.sin(theta)
b = np.cos(theta)
c = np.tan(theta)

print('sin({theta}) =', a, '\ncos({theta}) =', b, '\ntan({theta}) =', c, '\n')


#========================================================================================================
print('\n')


print('round(3.7):', np.round(3.7))
print('floor(3.7):', np.floor(3.7))
print('ceil(3.7):', np.ceil(3.7))

print('\n')

print('round(3.3):', np.round(3.3))
print('floor(3.3):', np.floor(3.3))
print('ceil(3.3):', np.ceil(3.3))


#========================================================================================================
print('\n')


print('3^5 =', np.power(3, 5))
print('3^2 =', np.power(3, 2))
print('30%7 =', np.mod(30, 7))
print('30%5 =', np.mod(30, 5))


#========================================================================================================
print('\n')

l = np.random.random(3) # get 3 random variables between 0, 1 in 1*3 matrix
print('random list:', l)

l = np.random.rand(3) # get 3 random variables between 0, 1 in 1*3 matrix
print('random list:', l)

m = np.random.random((2,3)) # get a 2*3 matrix of random numbers
print('random matrix :\n', m)

print('\n')

print('random matrix multiplied by 10 :\n', m*10)
print('random matrix multiplied by 10 then add 10 to it :\n', m*10 + 10)

print('2*3 random matrix using rand function:\n', np.random.rand(2,3))


#========================================================================================================
print('\n')


i = np.random.randint(10, 20, 5) # get 5 random integers between 10 and 19
print('five random integers between 10 and 20:', i)

m = np.random.randint(5, 15, (3,3)) # get a 3*3 matrix of random numbers with value between 5, 14
print('random 3*3 matirx:\n', m)

print('\n')

t = np.random.randint(5, 15, (3,3,4)) # get a 3*3*4 tensor of random numbers with value between 5, 14
print('random 3*3*4 matirx:\n', t)

print('\n')

a = np.random.randint(1,60,25)
b = np.reshape(a,(5,5)) # convert 1*n matrix to u*v matrix if possible, otherwise it throws an error.

print('25 numbers list:', a)
print('5*5 reshaped 25 numbers list:', b)


#========================================================================================================
print('\n')
print('Unifrom Distribution:')


r = np.random.uniform(1, 10) # get a random number that uniformally distributed betweeen 1 and 9
print('random number :', r)

l = np.random.uniform(1, 20, 10) # get 10 random numbers that uniformally distributed betweeen 1 and 19
print('10 random numbers :', l)


#========================================================================================================
print('\n')
print('Normal Distribution:')


n = np.random.normal(1, 20, 10) # get 10 random numbers that normally distributed betweeen 1 and 19
print('10 random numbers :\n', n)


#========================================================================================================
print('\n')
print('Gamma Distribution:')


n = np.random.gamma(1, 20, 10) # get 10 random numbers that have gamma distribution betweeen 1 and 19
print('10 random numbers :\n', n)
