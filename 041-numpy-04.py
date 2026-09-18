import numpy as np

l = np.linspace(0, 10, 3) # get 3 line-spaced numbers between 0 and 10
print('3 random numbers between 1 and 10:\n', l)

l = np.linspace(0, 30) # get 50 line-spaced numbers between 0 and 30 (50 is the default)
print('50 random numbers between 0 and 30:\n', l)

l = np.linspace(0, 30, 10) # get 10 line-spaced numbers between 0 and 30
print('10 random numbers between 0 and 30:\n', l)
print('reshaped to 3*4 matrix:\n', l.reshape(5, 2))


#========================================================================================================
print('\n')


d = np.diag([1,2,3,4]) # create 4*4 matrix and set the numbers 1,2,3,4 to it's diagonal
print('4*4 matrix with 1,2,3,4 in it\'s diagonal: \n',d)

d = np.diag(np.array([1,2,3,4])) # you can convert the list to 1*4 matrix
print('4*4 matrix with 1,2,3,4 in it\'s diagonal: \n',d)

d = np.diag([1,2,3,4], 2) # create 6*6 matrix (4+2) and set the numbers 1,2,3,4 to it's diagonal starting from index 2 (third row and column)
print('6*6 matrix with 1,2,3,4 in it\'s diagonal: \n',d)


#========================================================================================================
print('\n')


m = np.random.randint(0, 10, (3, 4)) # create a 3*4 matrix with values randomly chosen from the integer values between 0 and 9
print('3*4 matrix:\n', m)

cnz = np.count_nonzero(m)
print('number of non zero elements in the matrix are:', cnz)

cnz = np.count_nonzero(m > 5)
print('number of elements greater than 5 in the matrix are:', cnz)

cnz = np.count_nonzero(m > 5, axis=1)
print('number of elements greater than 5 in the matrix grouped per column/axis are:', cnz)


#========================================================================================================
print('\n')


m = np.random.randint(0, 10, (3, 4)) # create a 3*4 matrix with values randomly chosen from the integer values between 0 and 9
print('3*4 matrix:\n', m)

cnz = np.any(m)
print('check if any elements in the matrix are nonzero:', cnz)

cnz = np.any(m > 5)
print('check if any elements in the matrix are greater than 5:', cnz)

cnz = np.any(m > 10)
print('check if any elements in the matrix are greater than 10:', cnz)

cnz = np.any(m > 5, axis=1)
print('check if any elements are greater than 5 in the matrix grouped per column/axis are:', cnz)


#========================================================================================================
print('\n')


m = np.random.randint(0, 10, (3, 4)) # create a 3*4 matrix with values randomly chosen from the integer values between 0 and 9
print('3*4 matrix:\n', m)

cnz = np.all(m)
print('check if all elements in the matrix are nonzero:', cnz)

cnz = np.all(m > 5)
print('check if all elements in the matrix are greater than 5:', cnz)

cnz = np.all(m > 0)
print('check if all elements in the matrix are greater than 10:', cnz)

cnz = np.all(m > 2, axis=1)
print('check if all elements are greater than 2 in the matrix grouped per column/axis are:', cnz)


#========================================================================================================
print('\n')


a = np.random.randint(5, 20, 9).reshape(3, 3)

b = a > 10
c = a < 15

print('3*3 matrix:\n', a)
print('\n')
print('boolean map matrix for values greater than 10:\n', b)
print('matrix with values greater than 10:\n', a[b])
print('\n')
print('boolean map matrix for values less than 15:\n', c)
print('matrix with values less than 15:\n', a[c])


#========================================================================================================
print('\n')


a = np.arange(9).reshape(3, 3)
b = np.arange(9).reshape(3, 3)
c = b*2
d = np.isclose(a, b, rtol=0.1) # check if two matrices are close to each other regarding an error tolerance (rtol) = 0.1
e = np.isclose(a, c, rtol=0.1) # check if two matrices are close to each other regarding an error tolerance (rtol) = 0.1

print('first matrix:\n', a)
print('second matrix:\n', b)
print('third matrix:\n', c)
print('are matrix a and b close:\n', d)
print('are matrix a and c close:\n', e)