import numpy as np

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

c = np.random.choice(l) # randomly choose 1 element from the list
print('the randomly chosen element is:', c)

c = np.random.choice(l, 3) # randomly choose 3 element from the list and return them in a 1*3 matrix
print('the randomly chosen 3 elements are:', c)

np.random.shuffle(c) # shuffle the elements of the matrix
print('shuffled matrix:', c)


#========================================================================================================
print('\n')


s = np.random.sample(5) # return randomly chosen 5 elements with values between 0 and 1 and return them in a 1*5 matrix
print('the randomly chosen sample is:\n', s)

s = np.random.sample((3, 4)) # return randomly chosen 3*4 matrix with values between 0 and 1
print('the randomly chosen 3*4 sample matrix is:\n', s)

np.random.shuffle(s) # shuffle the elements of the matrix
print('shuffled matrix:', s)

s = np.random.sample((3, 4, 2)) # return randomly chosen 3*4*2 tensor with values between 0 and 1
print('the randomly chosen 3*4*2 sample tensor is:\n', s)

#========================================================================================================
print('\n')


z = np.zeros(5) # create 1*5 matrix of zeros
print('zeros 1*5 matrix:', z)

z = np.zeros((5, 3)) # create 5*3 matrix of zeros
print('zeros 5*3 matrix:\n', z)

z = np.zeros((5, 3, 2)) # create 5*3*2 tensor of zeros
print('zeros 5*3*2 tensor:\n', z)


#========================================================================================================
print('\n')


o = np.ones(5) # create 1*5 matrix of ones
print('ones 1*5 matrix:', o)

o = np.ones((5, 3)) # create 5*3 matrix of ones
print('ones 5*3 matrix:\n', o)

o = np.ones((5, 3, 2)) # create 5*3*2 tensor of ones
print('ones 5*3*2 tensor:\n', o)


#========================================================================================================
print('\n')


i = np.eye(5) # create 5*5 identity matrix
print('5*5 identity matrix:\n', i)

i = np.eye(5, 3) # create 5*3 identity matrix
print('5*3 identity matrix:\n', i)

i = np.eye(3, 5) # create 3*5 identity matrix
print('5*3 identity matrix:\n', i)

i = np.eye(3, 5, 2) # create 3*5 identity matrix with 1 starting the third column
print('5*3 identity matrix:\n', i)


#========================================================================================================
print('\n')


f = np.full(5, 35) # create 1*5 matrix filled with 35
print('1*5 matrix filled with 35:\n', f)

f = np.full((5, 3), 20) # create 5*3 matrix filled with 20
print('5*3 matrix filled with 20:\n', f)

f = np.full((5, 3, 3), 20) # create 5*3*3 tensor filled with 10
print('5*3*3 tensor filled with 10:\n', f)


#========================================================================================================
print('\n')


ar = np.arange(18) # get 1*18 matrix with values between 0 and 17
print('1*18 matrix:\n', ar)

ar = ar.reshape(3, 6) # reshape the matrix to 3*6 matrix
print('reshape the matrix of 1*18 to 3*6 matrix:\n', ar)

ar = np.arange(27) # get 1*27 matrix with values between 0 and 26
print('1*27 matrix:\n', ar)

ar = ar.reshape(3, 3, 3) # reshape the matrix to 3*3*3 matrix
print('reshape the matrix of 1*27 to 3*3*3 matrix:\n', ar)