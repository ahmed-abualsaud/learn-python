import numpy as np

a = np.arange(5)
b = np.empty(5)

print('first matrix:', a)
print('second matrix:', b)

np.multiply(a, 10, b) # multiply the matrix a by 10 then set the output to matrix b
print('second matrix multiplied by 10:', b)

np.power(a, 4, b) # set matrix a to power 4 then set the output to matrix b
print('second matrix powered to 4:', b)

p = np.multiply.reduce(a) # the product of all elements in the matrix
print('product of all elements of matrix a:', p)


#========================================================================================================
print('\n')


a = np.arange(5)
b = np.arange(5)
c = np.empty(5)

print('first matrix:', a)
print('second matrix:', b)

np.add(a, b, c) # add matrix a to matrix b and save the output to matrix c
print('matrix a + matrix c =', c)

s = np.add.reduce(a) # sum all elements of matrix a
print('sum of all elements of matrix a:', s)


#========================================================================================================
print('\n')


a = [1,2,3,4,5,6,7,8,9]

# accumulate() performs the operation step by step and stores every
# intermediate result instead of only the final one.
#
# Example:
# a = [0, 1, 2, 3, 4]
# b = [0,
#      0+1,
#      0+1+2,
#      0+1+2+3,
#      0+1+2+3+4]
#    = [0, 1, 3, 6, 10]
b = np.add.accumulate(a)

# accumulated multiplication (the same idea like the acumulated addition)
c = np.multiply.accumulate(a)

print('matrix a:', a)
print('matrix b (accumulated addition):', b)
print('matrix c (accumulated multiplication):', c)


#========================================================================================================
print('\n')


a = np.arange(10)
print('matrix a:', a)

# outer() applies the operation to every pair of elements from the two arrays.
# Each element in the first array is multiplied by every element in the second array.
# The result is a 2D matrix where:
#   result[i][j] = a[i] * a[j]
#
# Example:
# a = [1, 2, 3]
#
# Result:
# [[1*1, 1*2, 1*3],
#  [2*1, 2*2, 2*3],
#  [3*1, 3*2, 3*3]]
# =
# [[1, 2, 3],
#  [2, 4, 6],
#  [3, 6, 9]]

b = np.multiply.outer(a, a)  # every pair is multiplied
print('outer multiplication of a with a:\n', b)
print('\n')
b1 = np.add.outer(a, a)      # every pair is added
print('outer addition of a with a:', b1)
print('\n')
b2= np.subtract.outer(a, a)  # every pair is subtracted
print('outer subtraction of a with a:', b2)
print('\n')
b3 = np.maximum.outer(a, a)  # maximum of every pair
print('outer maximization of a with a:', b3)


#========================================================================================================
print('\n')


a = np.arange(12)
print('matrix a:', a)
print('length of matrix a:', len(a))
print('size of matrix a:', a.size)
print('shape of matrix a:', a.shape)
print('nuumber of dimensions of matrix a:', a.ndim)
print('data type of of matrix a:', a.dtype)

print('\n')

b = a.reshape(4, 3)
print('matrix b:\n', b)
print('length of matrix b:', len(b))
print('size of matrix b:', b.size)
print('shape of matrix b:', b.shape)
print('nuumber of dimensions of matrix b:', b.ndim)

print('\n')

c = a.reshape(6, 2)
print('matrix c:\n', c)
print('length of matrix c:', len(c))
print('size of matrix c:', c.size)
print('shape of matrix c:', c.shape)
print('nuumber of dimensions of matrix c:', c.ndim)


#========================================================================================================
print('\n')


print('data type:', np.array(['a', 'm']).dtype)
print('data type:', np.array(['ahmed', 'mohamed']).dtype)
print('data type:', np.array([1, 2]).dtype)
print('data type:', np.array([1.1, 2.2]).dtype)
print('data type:', np.array([True, False]).dtype)
print('data type:', np.array([1j, 2j]).dtype)